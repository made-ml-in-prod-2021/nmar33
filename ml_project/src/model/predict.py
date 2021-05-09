import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB


def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


def predict_model(model_path, data_path, predict_path):
    model = load_model(model_path)
    data = pd.read_csv(data_path, index_col=0)
    predict = model.predict(data)
    pd.DataFrame(predict).to_csv(predict_path, index=False)

