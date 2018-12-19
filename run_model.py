import torch
from PIL import ImageMath
import torchvision.transforms as transforms

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
      background = Image.new('RGB', image.size, (255,255,255))
      image = Image.alpha_composite(background, image)
    return self.transform(image)

  def name_for(self, index):
    return self.file_gen[index].name

  def __len__(self):
    return len(self.file_gen)

# auto batches
def run_model(files_generator, network):
  transforms_in = [
    transforms.Resize((224,224)),
    transforms.ToTensor()
  ]
  batch_size = 8
  # TODO: heh. deletes all errors? not great
  dataset = ModelRunLoader(files_generator, transforms_in)
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
