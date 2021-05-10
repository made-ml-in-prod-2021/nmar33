import numpy as np
import pandas as pd


def fake_data_generator(n=1000, path__fake_data='fake_dataset.csv' ):
    fake_data_columns = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
                         'avg_glucose_level', 'bmi', 'work_Govt_job', 'work_Never_worked',
                         'work_Private', 'work_Self-employed', 'work_children',
                         'smoking_formerly smoked', 'smoking_never smoked', 'smoking_smokes',
                         'stroke']

    N = n

    gender = np.random.randint(low=0, high=2, size=(N, 1))
    age = np.random.uniform(low=0, high=100, size=(N, 1))
    hypertension = np.random.randint(low=0, high=2, size=(N, 1))
    heart_disease = np.random.randint(low=0, high=2, size=(N, 1))
    ever_married = np.random.randint(low=0, high=2, size=(N, 1))
    avg_glucose_level = np.random.uniform(low=50, high=160, size=(N, 1))
    bmi = np.random.uniform(low=20, high=60, size=(N, 1))
    work_Govt_job = np.random.randint(low=0, high=2, size=(N, 1))
    work_Never_worked = np.random.randint(low=0, high=2, size=(N, 1))
    work_Private = np.random.randint(low=0, high=2, size=(N, 1))
    work_Self_employed = np.random.randint(low=0, high=2, size=(N, 1))
    work_children = np.random.randint(low=0, high=2, size=(N, 1))
    smoking_formerly = np.random.randint(low=0, high=2, size=(N, 1))
    smoking_never = np.random.randint(low=0, high=2, size=(N, 1))
    smoking_smokes = np.random.randint(low=0, high=2, size=(N, 1))
    stroke = np.random.randint(low=0, high=2, size=(N, 1))

    fake_data = np.concatenate([gender, age, hypertension, heart_disease, ever_married,
                                avg_glucose_level, bmi, work_Govt_job,
                                work_Never_worked, work_Private,
                                work_Self_employed, work_children,
                                smoking_formerly, smoking_never,
                                smoking_smokes, stroke
                                ], axis=1)

    fake_data = pd.DataFrame(fake_data, columns=fake_data_columns)
    fake_data.to_csv(path__fake_data, index=False)





