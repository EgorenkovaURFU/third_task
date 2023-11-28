from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome!'}

def test_predict():
    response = client.post('/prediction/',
                           json={"url": "https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['model-prediction'] == 'Egyptian_cat'
    assert json_data['model-prediction-confidence-score'][:4] == '0.58'


