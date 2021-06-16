# airflow-examples

## Конфигурация
В файле [`docker-compose.yml`]
Необходимо указать путь, куда будут сохраняться модели и данные
  - AIRFLOW_VAR_DATA_VOLUME_PATH=/home/nm/MLP2/airflow_ml_dags

Также нужно указать путь для прод-модели, что бы не заморачиваться можно просто 
заменить 2021-06-11 на текущее число
  - AIRFLOW_VAR_PROD_MODEL_PATH=/data/models/2021-06-11

## Запуск docker compose 
~~~
docker compose up --build
~~~

## Остановка docker compose 
~~~
docker compose down
~~~

## Полная очистка системы от ВСЕХ докеров и ВСЕХ образов
~~~
!Если выполнить будут удалены абсолютно все докеры и образы, которые есть в системе!
sudo docker kill $(sudo docker ps -q); sudo docker rm $(sudo docker ps -a -q); sudo docker rmi $(sudo docker images -q); sudo docker ps -a ; sudo docker images
~~~

