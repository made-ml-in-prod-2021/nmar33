В работе использовались данные
https://www.kaggle.com/fedesoriano/stroke-prediction-dataset


    docker pull nmar33/online_inference

Запуск без Docker:
  Windows:  

    python -m venv .venv
    .venv\Scripts\activate.bat
    pip install -r requirements.txt
    python setup.py

  Linux:  

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python setup.py
    
  Генерация запросов:
    python make_requests.py


/predict
 python train_pipeline.py --config_path ./configs/config_lr.yaml
    python model_predict.py --config_path ./configs/config_lr.yaml
    
  Логистическая регрессия:

    python train_pipeline.py --config_path ./configs/config_nb.yaml
    python model_predict.py --config_path ./configs/config_nb.yaml    


