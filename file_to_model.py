import torch

def file_to_model(f):
  return torch.load(f.result)
