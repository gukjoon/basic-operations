import torch

def image_to_tensor(image):
  tensor = transforms.ToTensor()(image)
  return tensor
