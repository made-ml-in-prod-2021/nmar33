import pandas as pd
from sklearn.model_selection import train_test_split


def data_load(path_raw_data, test_size, random_state,
              path_save_train, path_save_test):
    data = pd.read_csv(path_raw_data)
    data = data.dropna()
    work_type_data = pd.get_dummies(data['work_type'], prefix='work')
    smoking_status = pd.get_dummies(data['smoking_status'], prefix='smoking')
    data_prepared = data[['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'avg_glucose_level', 'bmi']]
    data_prepared = pd.concat([data_prepared, work_type_data, smoking_status], axis=1).drop(columns=['smoking_Unknown'])
    data_prepared['gender'] = data_prepared['gender'].map(lambda x: int(x == 'Male'))
    data_prepared['ever_married'] = data_prepared['ever_married'].map(lambda x: int(x == 'Yes'))
    data_prepared['stroke'] = data['stroke']
    train, test = train_test_split(data_prepared, test_size=test_size,
                                   random_state=random_state)
    train.to_csv(path_save_train)
    test.to_csv(path_save_test)
    return train, test
