import os
import datetime
from airflow.models import Variable
from airflow.utils.dates import days_ago

DEFAULT_ARGS = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=1),
}

DATA_VOLUME_PATH = Variable.get("data_volume_path")
PROD_MODEL_PATH = Variable.get("prod_model_path")

DIR_DATA_RAW = "/data/raw/{{ ds}}"
DIR_PROCESSED_DATA = "/data/processed/{{ ds}}"
DIR_MODELS = "/data/models/{{ ds}}"
DIR_PREDICT = "/data/predict/{{ ds}}"
DIR_METRIC = "/data/metrics/{{ ds}}"


VALID_DATA_SIZE = 0.33
RANDOM_STATE = 0
