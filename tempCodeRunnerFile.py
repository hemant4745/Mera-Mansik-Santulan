import joblib
from fastapi import FastAPI
model =joblib.load('Mental_health_Model.pkl')
app=FastAPI()
@app.get('/')
def greet():
    return {'Welcome to Sheryians AI School Guys'}