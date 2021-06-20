import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB


def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


def predict_model(model_path, data_path, predict_path, data_online=None, model=None):
    if data_path == 'online_inference':
        model = model
        data = data_online
        predict = model.predict(data)
        return predict
    else :
        model = load_model(model_path)
        data = pd.read_csv(data_path, index_col=0)
        predict = model.predict(data)
        pd.DataFrame(predict).to_csv(predict_path, index=False)

