import logging
import spacy
import os
from fastapi import FastAPI

from utils import job_classifier 

from schemas import UserMessage


# logging configuration
logging.basicConfig(
    filename="log_app.log",
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.DEBUG,
)


app = FastAPI()



@app.post("/job_classifier", tags=["job classifier"],description='Use job_classifier or job_classifier_acc as model name.')
def get_entities(item: UserMessage):
    text = item.text
    model_path = item.model_name +'/model-best'
    
    return [
        job_classifier(text,model_path)
    ]

