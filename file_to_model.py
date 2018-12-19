import torch

def file_to_model(file, network):
  state_dict = torch.load(next(file).result)
  network.load_state_dict(state_dict)
  return network
