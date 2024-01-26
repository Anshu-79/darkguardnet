import torch
from transformers import BertModel
from typing import Union, Tuple, List

from dark_pattern_classifier.consts import CHECKPOINT_DIR, MAX_LENGTH, CATEGORY_MAPPING
from dark_pattern_classifier.model import generate_model, generate_tokenizer
from dark_pattern_classifier.utils import load_dicts, encoder

def make_prediction(input_text: str) -> str:
    """
    Initializes the model, runs it and returns the most probable category.
    """

    model = generate_model()
    tokenizer = generate_tokenizer()
    checkpoint = torch.load(CHECKPOINT_DIR)
    load_dicts(model, checkpoint)

    with torch.no_grad():
        model.eval()
        encoded_text = encoder(input_text, tokenizer, MAX_LENGTH)
        input_ids = encoded_text['input_ids']
        attention_mask = encoded_text['attention_mask']

        output = model(input_ids, attention_mask)
        _, pred = torch.max(output, dim=1)
        return CATEGORY_MAPPING[int(pred)]
        

def make_predictions(input_list: List[str]) -> List[str]:
    """
    Simply runs make_prediction() for a sequence of values and returns the result as a list.
    """
    return [make_prediction(text) for text in input_list]
