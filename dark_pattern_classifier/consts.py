import os
import torch

# Change this to the path where the project is located
PARENT_DIR = "D:/Programming/"

pretrained_model_name = "bert-base-cased"
checkpoint_filename = f"4_category_classifier.pth"
CHECKPOINT_DIR = os.path.join(PARENT_DIR, "DPBH-Team_Veritas/dark_pattern_classifier/training/models", checkpoint_filename)
MAX_LENGTH = 32
CATEGORY_MAPPING = {0: 'Misdirection', 1: 'Scarcity', 2: 'Social Proof', 3: 'Urgency'}
NUM_LABELS = 4
DROPOUT = 0.1

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
