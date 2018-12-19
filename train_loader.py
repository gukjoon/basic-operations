from PIL import ImageMath
from PIL import Image
import torchvision.transforms as transforms
import torch

class TrainLoader:
  def __init__(self, image_generator, label_generator, transforms_in):
    self.image_gen = list(image_generator)
    self.label_gen = list(label_generator)
    print('isize', len(self.image_gen))
    print('lsize', len(self.label_gen))
    if not len(self.image_gen) == len(self.label_gen):
      print('MISMATCH IN INPUTS')
      raise ValueError('mismatch in inputs')
    self.transform = transforms.Compose(transforms_in)

  def __getitem__(self, index):
    image = self.image_gen[index]
    image = Image.open(self.file_gen[index].result)
    if not image.mode == 'RGB' and not image.mode == 'RGBA':
      image = ImageMath.eval('im/256', {'im':image}).convert('RGB')
    if image.mode == 'RGBA':
      background = Image.new('RGBA', image.size, (255,255,255))
      image = Image.alpha_composite(background, image).convert('RGB')

    label = self.label_gen[index]
    label = Image.open(file)
    if label.mode == 'RGBA':
      r, g, b, a = label.split()
      label = Image.merge('RGB', (a, a, a))
    return (self.transform(image), self.transform(label))

  def __len__(self):
    return len(self.image_gen)

def train_loader(images_generator, labels_generator):
  dataset = TrainLoader(images_generator, labels_generator, [
    transforms.Resize((224,224)),
    transforms.ToTensor()
  ])

  trainloader = torch.utils.data.DataLoader(
    dataset, 
    batch_size=8
    # num_workers=2
  )
  return trainloader
