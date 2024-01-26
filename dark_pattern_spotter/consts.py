import os
import torch

# Change this to the path where the project is stored
PARENT_DIR = "D:/Programming/"

pretrained_model_name = "roberta-large"
iteration = 4
checkpoint_filename = f"{pretrained_model_name}_{iteration}.pth"
CHECKPOINT_DIR = os.path.join(PARENT_DIR, "DPBH-Team_Veritas/dark_pattern_spotter/pretrained_models", checkpoint_filename)
MAX_LENGTH = 32

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
