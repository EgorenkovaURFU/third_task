# This application to identify images

The application developed with FastAPI.
You can clone this repository, install requirements and run app with comand 'uvicorn main:app'

Then, you can use curl to pass photo with url to identify photo.

Example:

curl -X 'POST' 'http://127.0.0.1:8000/prediction/' -H 'Content-Type: application/json' -d '{"url": "https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg"}'

Result:

{"model-prediction":"Egyptian_cat","model-prediction-confidence-score":"0.5804819"}