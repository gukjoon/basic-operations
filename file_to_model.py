import torch

def file_to_model(f, basenetwork):
  state_dict = torch.load(next(f).result)
  return basenetwork.load_state_dict(state_dict)
