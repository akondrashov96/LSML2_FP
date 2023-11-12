# LSML2_FP
Final Project for LSML 2 course

## Task

In this final project, we create a service for spelling correction for english language.

## Setup and Models

To perform this task, we chose [T5-lage-spell model](https://huggingface.co/ai-forever/T5-large-spell) (description found here : https://habr.com/ru/companies/sberdevices/articles/763932/) and a smaller model (T5-small) to make the main job.

**UPDATE**: due to unimpressive results obtained after training and attempts to distill the model, we chose to proceed by simply quantising the weights of T5-large-spell model.

## Procedure

We begin by loading the models and creating datasets. We will be using two datasets: `bea60k`, containing about 60k sentences for training the model and `jfleg` for distillation. Afterwards we assess the trained models quality.

**UPDATE**: model quality was not very good, so we just chose to perform quantisation of the large model.

## Metric

To evaluate the quality of the model, we suggest the following metric: we compare the original sentence ($x$), it's correction ($y$) and model predicted correction ($\hat y$). Let's call it "Error correction rate". To calculate it, we use the following formula:

$$Error\ correction\ rate = \cfrac{\sum \mathbb{I}(\hat y = y)}{\#\ of\ errors}$$

We first compare $x$ and $y$ to determine the indices of corrected words. The model does not deal with missing or extra whitespaces, the word count is always the same. Afterwards, we compare (at specified indices), whether the correction and predicted correction match. If yes, the error correction increases by one, if not, nothing happens. After comparing all words, we divide the matches by total number of errors. We also track the number of false positives (needless corrections) in a separate key.

## Results

**UPDATE**: it turned out, that the quality of t5-small model is too low to use to for production purposes (due to insufficient training, or maybe we messed up the procedure). So, we decided to perform quantization of the large model and use it in production.

The large model shows quite good correction quality. Moreover, quantization helped to reduce model size from 2.8 GB to just 0.8 GB without losing quality. 
