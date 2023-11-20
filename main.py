from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.applications.efficientnet import decode_predictions
from tensorflow.keras.utils import get_file 
import numpy as np



class Item(BaseModel):
    url: HttpUrl

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Welcome!'}


def load_model():
    model = EfficientNetB0(weights='imagenet')
    return model


def preprocess_image(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x


@app.post("/prediction/")
async def get_net_image_prediction(item: Item):
    if item.url == "":
        print(item.url)
        return {"message": "No image link provided"}
    
    img = image.load_img(get_file('image', str(item.url)),target_size=(224, 224))
  

    x = preprocess_image(img)
    

    model = load_model()
    pred = model.predict(x)
    classes = decode_predictions(pred, top=1)[0]
    for i in classes:
        model_prediction = str(i[1])
        model_prediction_confidence_score = str(i[2])

        return {"model-prediction": model_prediction, "model-prediction-confidence-score": model_prediction_confidence_score}
    
