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