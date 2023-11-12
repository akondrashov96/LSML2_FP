from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import os
import io
import base64
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import torch
from transformers import T5ForConditionalGeneration, AutoTokenizer, AutoConfig, PreTrainedTokenizerFast


app = FastAPI()
templates = Jinja2Templates(directory = "templates") 

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

    encodings = tokenizer(sentence, return_tensors="pt").input_ids
    generated_tokens = model.generate(encodings)
    answer = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

    return(answer)


#### App Endpoints

@app.get("/")
async def root(request: Request):
    # return {"Hello": "World"}

    return templates.TemplateResponse("index.html",
                                       {"request": request})

@app.get("/gen_correction")
async def gen_correction(# request: Request, 
                input_text: str):
    
    print("Loading model and tokenizer...")
    tokenizer, model = load_model()

    print("Correcting...")
    correction = generate_correction(input_text, tokenizer, model)

    return {"correction": correction}

@app.post("/correction")
async def correction(request: Request,
                    input_text: str = Form(...)):
    
    print("Loading model and tokenizer...")
    tokenizer, model = load_model()

    print("Correcting...")
    correction = generate_correction(input_text, tokenizer, model)
    
    return templates.TemplateResponse("result.html", 
                                      {"request": request,
                                       "original": input_text,
                                       "input_text": input_text,
                                       "correction": correction})