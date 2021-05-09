from src.model import predict_model
from src.enities import PiplineParams, read_configs
import sys
import logging
import logging.config
import click

@click.command()
@click.option("--config_path")
def main(config_path):
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
    logger.info('Начало обработки данных...')
    predict_model(cnfg.paths.output_model_path,
                  cnfg.paths.predict_dataset_path,
                  cnfg.paths.predict_path)
    logger.info('Обработка данных завершена')


if __name__ == '__main__':
    main()