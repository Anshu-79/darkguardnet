import os

CWD = os.getcwd()
pretrained_model_name = "roberta-large"
iteration = 4
checkpoint_filename = f"{pretrained_model_name}_{iteration}.pth"
CHECKPOINT_DIR = os.path.join(CWD, "pretrained_models", checkpoint_filename)
MAX_LENGTH = 32