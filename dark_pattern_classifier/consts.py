import os

CWD = os.getcwd()
pretrained_model_name = "bert-base-cased"
checkpoint_filename = f"4_category_classifier.pth"
CHECKPOINT_DIR = os.path.join(CWD, "training\\models", checkpoint_filename)
MAX_LENGTH = 32
CATEGORY_MAPPING = {0: 'Misdirection', 1: 'Scarcity', 2: 'Social Proof', 3: 'Urgency'}
NUM_LABELS = 4
DROPOUT = 0.1