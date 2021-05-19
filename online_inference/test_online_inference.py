import pytest
from fastapi.testclient import TestClient

from online_inference import app

RIGHT_POST_0 = {
        "id": 9,
        "gender": "Female",
        "age": 17,
        "hypertension": 0,
        "heart_disease": 0,
        "ever_married": "Yes",
        "work_type": "Private",
        "avg_glucose_level": 100,
        "bmi": 40,
        "smoking_status": "never smoked"
    }

RIGHT_POST_1 = {
        "id": 11,
        "gender": "Male",
        "age": 150,
        "hypertension": 1,
        "heart_disease": 1,
        "ever_married": "Yes",
        "work_type": "Private",
        "avg_glucose_level": 100,
        "bmi": 40,
        "smoking_status": "smokes"
    }


client = TestClient(app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json()['msg'] == 'online inference'


def test_check_status():
    response = client.get('/status')    
    assert response.status_code == 200
    assert response.json() == {'model_type': 'LR', 'model_status': True}


def test_check_predict_0():
    response = client.post('/predict', json=RIGHT_POST_0)
    assert response.status_code == 200
    assert response.json() == {'id': 9, 'predict': 0}

def test_check_predict_1():
    response = client.post('/predict', json=RIGHT_POST_1)
    assert response.status_code == 200
    assert response.json() == {'id': 11, 'predict': 1}