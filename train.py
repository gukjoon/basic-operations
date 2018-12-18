# imported from gukjoon/basic-operations 3ebc4360c6f5ea427582e02e6f1f4d71c49fedbb
import torch.optim as optim
import torch.nn as nn
import torch.onnx
import torch

from torch.autograd import Variable
from tensorboardX import SummaryWriter
from torchvision import transforms

class ProgressiveLoader:
  def __init__(self, image_generator, label_generator, transforms_in):
    self.image_gen = list(image_generator)
    self.label_gen = list(label_generator)
    print('isize', len(self.image_gen))
    print('lsize', len(self.label_gen))
    if not len(self.image_gen) == len(self.label_gen):
      raise ValueError('mismatch in inputs')
    self.transform = transforms.Compose(transforms_in)

  def __getitem__(self, index):
    image = self.image_gen[index]
    label = self.label_gen[index]
    return (self.transform(image), self.transform(label))

  def __len__(self):
    return len(self.image_gen)


def train(images_generator, labels_generator, network, optimizer, loss_function, epochs):
  images_generator = (i.result for i in images_generator)
  labels_generator = (i.result for i in labels_generator)
  network = network.cuda()
  optimizer, scheduler = optimizer
  dataset = ProgressiveLoader(images_generator, labels_generator, [
      transforms.Resize((224,224)),
      transforms.ToTensor()
  ])

  trainloader = torch.utils.data.DataLoader(
    dataset, 
    batch_size=8
    # num_workers=2
  )
  
  data_size = len(trainloader)
  
  for epoch in range(epochs):
    for i, data in enumerate(trainloader, 0):
      inputs, labels = data
      inputs, labels = inputs.cuda(), labels.cuda()
      outputs = network(inputs)
      loss = loss_function(outputs, labels)
      loss.backward()
      optimizer.step()
      optimizer.zero_grad()
  print('DONE')
  yield network

#   def save_onnx(self, f):
#     dummy_input = Variable(torch.randn(4, 3, 224, 224)).cuda()
#     torch.onnx.export(self.network, dummy_input, f, verbose=True)

#   def save_pth(self, f):
#     torch.save(self.network, f)
