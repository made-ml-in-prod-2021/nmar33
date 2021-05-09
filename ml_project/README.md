В работе использовались данные
https://www.kaggle.com/fedesoriano/stroke-prediction-dataset

Установка (Windows):  

    python -m venv .venv
    .venv\Scripts\activate.bat
    pip install -r requirements.txt

Установка (Linux):  

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Запуск train/predict модели:
  Логистическая регрессия:

    python train_pipeline.py --config_path ./configs/config_lr.yaml
    python model_predict.py --config_path ./configs/config_lr.yaml
    
  Логистическая регрессия:

    python train_pipeline.py --config_path ./configs/config_nb.yaml
    python model_predict.py --config_path ./configs/config_nb.yaml    


