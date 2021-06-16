from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from constants import (
    DEFAULT_ARGS,
    DATA_VOLUME_PATH,
    DIR_DATA_RAW,
    PROD_MODEL_PATH,
    DIR_PREDICT,
)


with DAG(
    dag_id="03_prod_model_predict",
    default_args=DEFAULT_ARGS,
    schedule_interval="@daily",
    start_date=days_ago(0, 7),
) as dag:

    start_predict = DummyOperator(task_id="start_predict")

    model_predict = DockerOperator(
        image="airflow-predict",
        command=f"--prod_model_dir {PROD_MODEL_PATH} --data_raw {DIR_DATA_RAW} --predict_dir {DIR_PREDICT}",
        network_mode="bridge",
        do_xcom_push=False,
        task_id="model_predict",
        volumes=[f"{DATA_VOLUME_PATH}:/data"],
    )

    end_predict = DummyOperator(task_id="end_predict")

    start_predict >> model_predict >> end_predict
