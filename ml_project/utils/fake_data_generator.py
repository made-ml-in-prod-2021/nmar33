import numpy as np
import pandas as pd


def fake_data_generator(n=1000, path_fake_data='fake_dataset.csv' ):
    fake_data_columns = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
                         'avg_glucose_level', 'bmi', 'work_Govt_job', 'work_Never_worked',
                         'work_Private', 'work_Self-employed', 'work_children',
                         'smoking_formerly smoked', 'smoking_never smoked', 'smoking_smokes',
                         'stroke']

    categorical_columns = ['gender', 'hypertension', 'heart_disease', 'ever_married',
                         'work_Govt_job', 'work_Never_worked',
                         'work_Private', 'work_Self-employed', 'work_children',
                         'smoking_formerly smoked', 'smoking_never smoked', 'smoking_smokes',
                         'stroke']

    N = n

    fake_data = {c: np.random.randint(low=0, high=2, size=(N, 1)) for c in categorical_columns}

    fake_data['age'] = np.random.uniform(low=0, high=100, size=(N, 1))
    fake_data['avg_glucose_level'] = np.random.uniform(low=50, high=160, size=(N, 1))
    fake_data['bmi'] = np.random.uniform(low=20, high=60, size=(N, 1))

    fake_data = [fake_data[column_name] for column_name in fake_data_columns]

    fake_data = np.concatenate(fake_data, axis=1)

    fake_data = pd.DataFrame(fake_data, columns=fake_data_columns)
    fake_data.to_csv(path_fake_data, index=False)


