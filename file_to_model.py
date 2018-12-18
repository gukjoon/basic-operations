import torch

def file_to_model(file, network):
  state_dict = torch.load(next(file).result)
  print(state_dict)
  print(network)
  network.load_state_dict(state_dict)
  return network
