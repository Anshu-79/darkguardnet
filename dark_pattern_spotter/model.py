from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

from dark_pattern_spotter.consts import pretrained_model_name, device

model = AutoModelForSequenceClassification.from_pretrained(pretrained_model_name)
model = model.to(device)
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)

def generate_model():
    return model

def generate_tokenizer():
    return tokenizer
