from transformers import AutoTokenizer, AutoModelForSequenceClassification
from consts import pretrained_model_name

model = AutoModelForSequenceClassification.from_pretrained(pretrained_model_name)
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)

def generate_model():
    return AutoModelForSequenceClassification.from_pretrained(pretrained_model_name)

def generate_tokenizer():
    return AutoTokenizer.from_pretrained(pretrained_model_name)
