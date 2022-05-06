

from typing import Dict
from fastapi import FastAPI, status
from pydantic import BaseModel

import logging
from logging.config import dictConfig
from log_config import log_config

from transformers import pipeline


dictConfig(log_config)
logger = logging.getLogger("my-project-logger")

app = FastAPI()
sa_model = pipeline("sentiment-analysis")


class SentimentRequest(BaseModel):
	in_text: str 

class SentimentResponse(BaseModel):
	sentiment : str
	score: float

@app.get('/', status_code=200)
def hello():
	return "Hello World"

@app.get('/healthcheck', status_code=200)
def perform_healthcheck():
	return {'healthcheck' : 'Everything OK!'}


@app.post("/predict", response_model=SentimentResponse)
async def predict(request : SentimentRequest):
	result = sa_model(request.in_text)
	return SentimentResponse (
		sentiment=result[0]['label'],
		score=result[0]['score'])

