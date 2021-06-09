from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from constants import DEFAULT_ARGS, DIR_DATA_RAW, DIR_DATA_VOLUME

with DAG(
      '01_data_download',
      default_args=DEFAULT_ARGS,
      schedule_interval='@daily',
      start_date=days_ago(0, 7),
) as dag:

      start_download = DummyOperator(task_id='start_download')

      data_download = DockerOperator(
            image='airflow-download',
            command=f'--output_dir {DIR_DATA_RAW}',
            network_mode='bridge',
            task_id='download_data',
            volumes=[f'{DIR_DATA_VOLUME}:/data'],
      )

      end_download = DummyOperator(task_id='end_download')

      start_download >> data_download >> end_download