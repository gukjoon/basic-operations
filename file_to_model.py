import torch

def file_to_model(f, basenetwork):
  state_dict = torch.load(next(f).result)
  basenetwork.load_state_dict(state_dict)
  return basenetwork
