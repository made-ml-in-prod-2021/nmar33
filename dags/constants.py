import os
import datetime
from airflow.models import Variable
from airflow.utils.dates import days_ago

DEFAULT_ARGS = {
      'owner': 'airflow',
      'email': ['airflow@example.com'],
      'email_on_failure': False,
      'email_on_retry': False,
      'retries': 1,
      'retry_delay': datetime.timedelta(minutes=1)
}

VOLUME_DATA_PATH = Variable.get('data_path')


DIR_DATA_RAW = '/data/raw/{{ ds}}'
DIR_PROCESSED_DATA = '/data/raw/{{ ds}}'
DIR_MODELS = '/data/models/{{ ds}}'
DIR_PREDICT = '/data/predict/{{ ds}}'

MODEL_PATH = Variable.get('model_path')