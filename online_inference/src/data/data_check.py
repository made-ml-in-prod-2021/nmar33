

'''
from pydantic import BaseModel


class DataRequest(BaseModel):
    id: int
    gender: str
    age: int
    hypertension: int
    heart_disease: int
    ever_married: str
    work_type: str
    avg_glucose_level: int
    bmi: int
    smoking_status: str

data_input = DataRequest()
'''

def data_check(data_input):
    data_correct = True
    data_correct *= (data_input.gender in {'Male', 'Female'})
    data_correct *= (0 <= data_input.age <= 250)
    data_correct *= (set([data_input.hypertension, data_input.heart_disease]) <= {0, 1})
    data_correct *= (data_input.ever_married in {'Yes', 'No'})
    data_correct *= (0 <= data_input.bmi <= 100)
    data_correct *= (0 <= data_input.avg_glucose_level <= 400)
    return data_correct