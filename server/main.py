from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
import os
import io
import base64
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import torch
from transformers import T5ForConditionalGeneration, AutoTokenizer, AutoConfig, PreTrainedTokenizerFast

corrector = {}

#### Functions block

def load_model():

    '''
    A function to load T5 model and it's tokenizer from a file
    
    Input:
    None

    Output:
    tokenizer, model
    '''
    
    tokenizer = PreTrainedTokenizerFast(tokenizer_file="./src/tokenizer/tokenizer.json")

    model = torch.load("./src/models/quantized_T5-large.pt")
    model.eval()

    return tokenizer, model

def generate_correction(input_text, tokenizer, model):

    sentence = "grammar: " + input_text
    print(input_text)

    encodings = tokenizer(sentence, return_tensors="pt").input_ids
    generated_tokens = model.generate(encodings, max_length = 150)
    answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

    indices = [str(int(x != y)) for x, y in zip(input_text.split(), answer.split())]

    return(answer, indices)

asynccontextmanager
async def lifespan(app: FastAPI):
    
    # Load the ML model

    print("Loading model and tokenizer...")
    corrector['tokenizer'], corrector['model'] = load_model()
    yield

    corrector.clear()

app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory = "templates") 


#### App Endpoints

@app.get("/")
async def root(request: Request):
    # return {"Hello": "World"}

    return templates.TemplateResponse("index.html",
                                       {"request": request})

@app.get("/gen_correction")
async def gen_correction(# request: Request, 
                input_text: str):

    print("Correcting...")
    correction, indices = generate_correction(input_text, corrector['tokenizer'], corrector['model'])

    return {"correction": correction}

@app.post("/correction")
async def correction(request: Request,
                    input_text: str = Form(...)):
    
    print("Correcting...")
    correction, indices = generate_correction(input_text, 
                                              corrector['tokenizer'], 
                                              corrector['model'])
    print(list(zip(correction.split(), indices)))
    input_text = list(zip(input_text.split(), list(indices)))
    correction = list(zip(correction.split(), list(indices)))
    
    return templates.TemplateResponse("result.html", 
                                      {"request": request,
                                       "original": input_text,
                                       "correction": correction})