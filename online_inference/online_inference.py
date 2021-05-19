import os
import sys
import logging
import logging.config

from fastapi import FastAPI


from src.model import predict_model, load_model
from src.enities import DataRequest, read_configs
from src.data import data_load_online





config_path = os.getenv('CONFIG_PATH', default='./configs/config_lr.yaml')
cnfg = read_configs(config_path)
logging.basicConfig(
    stream=sys.stderr,
    level=logging.DEBUG
)
std_formatter = logging.Formatter(**cnfg.log_config.formatter_config)
log_handler = logging.FileHandler(cnfg.paths.log_path)
log_handler.setFormatter(std_formatter)
logger = logging.getLogger('logger_all')
logger.addHandler(log_handler)
logger.propagate = False
logger.setLevel(logging.DEBUG)
logger.info('Логирование начато')
logger.info('Загрузка модели...')
model = load_model(cnfg.paths.output_model_path)
model_type = cnfg.train_config.model_type
logger.info('Загрузка модели окончена')

app = FastAPI()


@app.get('/')
def main():
    return {
        'msg': 'online inference',
        'version': '0.0.05'
    }


@app.get('/status')
def check_status():
    return {
        'model_type':model_type, 
        'model_status':(model is not None)
    }

@app.get('/logs')
def read_logs():
    logs = ''
    with open(cnfg.paths.log_path, 'r') as file:
        for line in file:
            logs += line.strip() + '      '
    return logs

@app.post('/predict')
def predict(data_request: DataRequest):
    logger.info('Обработка данных')
    status = check_status()
    if status['model_status']:
        data = data_load_online(data_request)
        predict = predict_model(
            model_path=None, data_path='online_inference', 
            predict_path=None, data_online=data, model=model
        )
        predict = int(predict[0])
        logger.info('Данные обработаны')
        return  {'id': data_request.id, 'predict': predict}
    else:
        logger.error('Модель не найдена')
        return 'Модель не найдена'

