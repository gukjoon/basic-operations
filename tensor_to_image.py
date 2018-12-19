import torchvision.transforms as transforms

def tensor_to_image(tensor):
  return transforms.ToPILImage()(tensor)
