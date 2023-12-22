import torch
from typing import Union, Tuple, List

from consts import CHECKPOINT_DIR, MAX_LENGTH
from model import generate_model, generate_tokenizer
from utils import load_dicts, text_to_tensor


def make_prediction(input_text: str) -> torch.Tensor:
    """
    Initializes the model, runs it and returns the output tensor.
    """

    model = generate_model()
    tokenizer = generate_tokenizer()
    checkpoint = torch.load(CHECKPOINT_DIR, map_location='cpu')
    load_dicts(model, checkpoint)

    with torch.no_grad():
        model.eval()
        input_tensor = text_to_tensor(input_text, tokenizer, MAX_LENGTH)
        
        input_tensor = input_tensor.unsqueeze(0)
        output = model(input_tensor)
        logits = output.logits
        return logits


def is_dark_pattern(input_text: str, return_probabilites: bool = False) -> Union[bool, Tuple[bool, float]]:
    """
    Converts the output tensor obtained from make_prediction() into a boolean.
    """
    
    logits = make_prediction(input_text)
    final_tensor = logits.argmax(dim=-1)
    
    is_dp = bool(final_tensor)

    if return_probabilites:
        probabilities = logits.squeeze(0).tolist()
        confidence = (max(probabilities) - min(probabilities)) / 10
        
        return is_dp, confidence
    
    return is_dp

    
def are_dark_patterns(input_list: List[str], return_probabilites: bool = False) -> List[Union[bool, Tuple[bool, float]]]:
    """
    Simply runs is_dark_patterns() for a sequence of values and returns the result as a list.
    """

    predictions = []
    for text in input_list:
        prediction = is_dark_pattern(text, return_probabilites=return_probabilites)
        predictions.append(prediction)
    
    return predictions
