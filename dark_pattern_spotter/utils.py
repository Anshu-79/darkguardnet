import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from collections import OrderedDict

from dark_pattern_spotter.consts import device

def load_dicts(model: AutoModelForSequenceClassification, checkpoint: OrderedDict) -> None:
    model_dict = model.state_dict()
    pretrained_dict = {key: val for key, val in checkpoint.items() if key in model_dict}
    model_dict.update(pretrained_dict)
    model.load_state_dict(model_dict)


def text_to_tensor(text: str, tokenizer: AutoTokenizer, max_length: int) -> torch.Tensor:
    tensor = torch.Tensor(
        tokenizer.encode(text, max_length=max_length, padding='max_length')
    ).to(torch.long)
    return tensor.to(device)
