import os
import sys
import json
import pandas as pd
import requests
import logging.config

from src.enities import read_configs

config_path = os.getenv('CONFIG_PATH', default='./configs/config_lr.yaml')

def main():
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
    logger.info('=======Make requests=======')

    data = pd.read_csv(cnfg.paths.raw_dataset_path)
    data = data.drop(cnfg.train_config.column_y, axis=1)
    data = data.drop('Residence_type', axis=1)
    data = data.dropna()
    data = data.to_dict("records")
    for d in data[50:75]:
        response = requests.post("http://localhost:8000/predict", json.dumps(d))
        logger.info(response.status_code)
        logger.info(response.json())

if __name__ == "__main__":
    main()





