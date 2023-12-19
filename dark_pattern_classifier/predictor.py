import torch

from consts import CHECKPOINT_DIR, MAX_LENGTH
from model import generate_model, generate_tokenizer
from utils import load_dicts, text_to_tensor


def make_prediction(model, tokenizer, input_text) -> torch.Tensor:
    with torch.no_grad():
        model.eval()
        input_tensor = text_to_tensor(input_text, tokenizer, MAX_LENGTH)
        
        input_tensor = input_tensor.unsqueeze(0)
        output = model(input_tensor)
        logits = output.logits
        return logits


def is_dark_pattern(input_text, return_probabilites=False):
    
    model = generate_model()
    tokenizer = generate_tokenizer()
    checkpoint = torch.load(CHECKPOINT_DIR, map_location='cpu')
    load_dicts(model, checkpoint)

    logits = make_prediction(model, tokenizer, input_text)
    final_tensor = logits.argmax(dim=-1)
    
    is_dp = bool(final_tensor)

    if return_probabilites:
        probabilities = logits.squeeze(0).tolist()
        confidence = (max(probabilities) - min(probabilities)) / 10
        
        return is_dp, confidence
    
    return is_dp

    
def are_dark_patterns(input_list, return_probabilites=False):
    predictions = []
    for text in input_list:
        prediction = is_dark_pattern(text, return_probabilites=return_probabilites)
        predictions.append(prediction)
    return predictions

