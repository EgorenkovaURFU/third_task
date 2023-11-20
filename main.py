from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
classifier = pipeline('sentiment-analysis')

@app.get('/')
async def root():
    return {'messager': 'Hello world!'}

@app.get('/predict/')
def predict():
    return classifier('I like machine learning engineering!')[0]



