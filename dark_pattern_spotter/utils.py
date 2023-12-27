import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from collections import OrderedDict

def load_dicts(model: AutoModelForSequenceClassification, checkpoint: OrderedDict) -> None:
    model_dict = model.state_dict()
    pretrained_dict = {key: val for key, val in checkpoint.items() if key in model_dict}
    model_dict.update(pretrained_dict)
    model.load_state_dict(model_dict)


def text_to_tensor(text: str, tokenizer: AutoTokenizer, max_length: int) -> torch.Tensor:
    return torch.Tensor(
        tokenizer.encode(text, max_length=max_length, pad_to_max_length=True)
    ).to(torch.long)
