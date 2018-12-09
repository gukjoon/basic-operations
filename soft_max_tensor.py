import torchvision.transforms as transforms
import torch
import torchvision.transforms.functional as F
import torch.nn as nn

def soft_max_tensor(tensor):
  print(tensor)
  res = nn.LogSoftmax(0)(tensor).max(0)[1]
  print(res)
  a, b = res.shape
  return res.view(1, a, b).float()
