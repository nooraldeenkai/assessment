from fastapi import FastAPI
from app.ML.model import predict_pipeline
from app.ML.model import __version__ as model_version
from app.models.predict import  Input, Output

app = FastAPI()



#health check to log the app is working
@app.get("/")
def home():
    return {"healthcheck": "OK"}



#language endpoint that returns detected language 
@app.post("/language", response_model=Output)
def predict(payload: Input):
    language = predict_pipeline(payload.text)
    return {"language": language}