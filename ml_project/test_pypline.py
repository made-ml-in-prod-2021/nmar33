import pandas as pd
from utils import fake_data_generator


def test_fake_data_generator():
    fake_data_generator(path_fake_data='./data/fake_dataset/fake_dataset.csv')
    dataset = pd.read_csv('./data/fake_dataset/fake_dataset.csv')
    check_columns = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
                         'avg_glucose_level', 'bmi', 'work_Govt_job', 'work_Never_worked',
                         'work_Private', 'work_Self-employed', 'work_children',
                         'smoking_formerly smoked', 'smoking_never smoked', 'smoking_smokes',
                         'stroke']
    assert list(dataset.columns) == check_columns

