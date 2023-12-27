from transformers import BertTokenizer, BertModel
from torch import nn
from consts import pretrained_model_name, DROPOUT, NUM_LABELS


class DarkPatternClassifier(nn.Module):

    def __init__(self, dropout=DROPOUT):
        super(DarkPatternClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(pretrained_model_name)
        self.drop = nn.Dropout(dropout)
        self.out = nn.Linear(self.bert.config.hidden_size, NUM_LABELS)

    def forward(self, input_ids, attention_mask):
        _, pooled_output = self.bert(input_ids=input_ids, attention_mask=attention_mask, return_dict=False)
        output = self.drop(pooled_output)
        return self.out(output)

def generate_model():
    model = DarkPatternClassifier()
    return model

def generate_tokenizer():
    return BertTokenizer.from_pretrained(pretrained_model_name)
