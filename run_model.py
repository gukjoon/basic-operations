import torch
from PIL import ImageMath
import torchvision.transforms as transforms

class ModelRunLoader:
  def __init__(self, image_generator, transforms_in):
    self.image_gen = list(image_generator)
    self.transform = transforms.Compose(transforms_in)

  def __getitem__(self, index):
    image = self.image_gen[index].result
    return self.transform(image)

  def name_for(self, index):
    return self.image_gen[index].name

  def __len__(self):
    return len(self.image_gen)

# auto batches
def run_model(images_generator, network):
  transforms_in = [
    transforms.Resize((224,224)),
    transforms.ToTensor()
  ]
  batch_size = 8
  # TODO: heh. deletes all errors? not great
  filtered_images = (i for i in images_generator if isinstance(i, PipelineSuccess))
  dataset = ModelRunLoader(filtered_images, transforms_in)
  loader = torch.utils.data.DataLoader(
    dataset,
    batch_size=batch_size
    # num_workers=2
  )
  if torch.cuda.is_available():
    network = network.cuda()

  for i, tensor in enumerate(loader):
    if torch.cuda.is_available():
      tensor = tensor.cuda()    
    preds = network(tensor)
    if isinstance(preds, tuple):
      preds = preds[0]
    for j, out_tensor in enumerate(preds):
      idx = i * batch_size + j
      name = dataset.name_for(idx)
      print(idx, name)
      yield PipelineSuccess(name, out_tensor.cpu())
