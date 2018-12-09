import torchvision.transforms as transforms

def grayscale(image):
  return transforms.Grayscale(3)(image)
