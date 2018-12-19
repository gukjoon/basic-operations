import torchvision.transforms as transforms

def image_to_tensor(image):
  return transforms.ToTensor()(image)
