from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from constants import DEFAULT_ARGS, DATA_VOLUME_PATH, DIR_DATA_RAW, \
      DIR_PROCESSED_DATA, VALID_DATA_SIZE, RANDOM_STATE, DIR_MODELS, DIR_METRIC


with DAG(
      dag_id="02_train_pipeline",
      default_args=DEFAULT_ARGS,
      schedule_interval="@weekly",
      start_date=days_ago(0, 7),
) as dag:

      start_preprocess = DummyOperator(task_id="start_preprocess")

      data_preprocess = DockerOperator(
      image="airflow-preprocess",
      command=f"--input_dir {DIR_DATA_RAW} --output_dir {DIR_PROCESSED_DATA}",
      network_mode="bridge",
      do_xcom_push=False,
      task_id="preprocess_data",
      volumes=[f"{DATA_VOLUME_PATH}:/data"],
      )


      end_preprocess = DummyOperator(task_id="end_preprocess")
      start_train_val_split = DummyOperator(task_id="start_train_val_split")

      data_train_val_split  = DockerOperator(
      image="airflow-train-val-split",
      command=f"--input_dir {DIR_PROCESSED_DATA} --val_size {VALID_DATA_SIZE} --rnd_state {RANDOM_STATE}",
      network_mode="bridge",
      do_xcom_push=False,
      task_id="data_train_val_split",
      volumes=[f"{DATA_VOLUME_PATH}:/data"],
      )

      end_train_val_split = DummyOperator(task_id="end_train_val_split")

      airflow_model_train  = DockerOperator(
      image="airflow-model-train",
      command=f"--input_dir {DIR_PROCESSED_DATA} --output_dir {DIR_MODELS}",
      network_mode="bridge",
      do_xcom_push=False,
      task_id="model_train",
      volumes=[f"{DATA_VOLUME_PATH}:/data"],
      )

      end_model_train = DummyOperator(task_id="end_model_train")


      airflow_model_validate  = DockerOperator(
      image="airflow-model-validate",
      command=f"--model_dir {DIR_MODELS} --data_dir {DIR_PROCESSED_DATA} --metric_dir {DIR_METRIC}",
      network_mode="bridge",
      do_xcom_push=False,
      task_id="model_validate",
      volumes=[f"{DATA_VOLUME_PATH}:/data"],
      )

      end_model_validate  = DummyOperator(task_id="end_model_validate")

      start_preprocess >> data_preprocess >> end_preprocess >> start_train_val_split >> \
            data_train_val_split >> end_train_val_split >> airflow_model_train >> end_model_train \
                  >> airflow_model_validate >> end_model_validate
      
