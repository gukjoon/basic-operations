from PIL import ImageMath
from PIL import Image
import torchvision.transforms as transforms
import torch

class ModelRunLoader:
  def __init__(self, files_generator, transforms_in):
    self.file_gen = list(files_generator)
    self.transform = transforms.Compose(transforms_in)

  def __getitem__(self, index):
    # TODO: this is a dupe of file_to_image
    # Better to have injection?
    image = Image.open(self.file_gen[index].result)
    if not image.mode == 'RGB' and not image.mode == 'RGBA':
      image = ImageMath.eval('im/256', {'im':image}).convert('RGB')
    if image.mode == 'RGBA':
      background = Image.new('RGBA', image.size, (255,255,255))
      image = Image.alpha_composite(background, image).convert('RGB')
    return self.transform(image)

  def name_for(self, index):
    return self.file_gen[index].name

  def __len__(self):
    return len(self.file_gen)


def run_loader(files_generator):
  transforms_in = [
    transforms.Resize((224,224)),
    transforms.ToTensor()
  ]
  
  dataset = ModelRunLoader(files_generator, transforms_in)

  return dataset
