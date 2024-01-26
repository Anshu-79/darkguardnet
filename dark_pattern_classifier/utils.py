import torch
from transformers import BertModel, BertTokenizer
from collections import OrderedDict

from dark_pattern_classifier.consts import device

def load_dicts(model: BertModel, checkpoint: OrderedDict) -> None:
    model_dict = model.state_dict()
    pretrained_dict = {key: val for key, val in checkpoint.items() if key in model_dict}
    model_dict.update(pretrained_dict)
    model.load_state_dict(model_dict)


def encoder(text: str, tokenizer: BertTokenizer, max_length: int) -> torch.Tensor:
    return tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=max_length,
        return_token_type_ids=False,
        padding='max_length',
        return_attention_mask=True,
        truncation=True,
        return_tensors='pt').to(device)
