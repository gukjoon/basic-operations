# imported from gukjoon/basic-operations 3ebc4360c6f5ea427582e02e6f1f4d71c49fedbb
import torch.optim as optim
import torch.nn as nn
import torch.onnx
import torch

from torch.autograd import Variable
from tensorboardX import SummaryWriter
from torchvision import transforms


def train(trainloader, network, loss_function, optimizer, epochs):
  network = network.cuda()
  optimizer, scheduler = optimizer

  data_size = len(trainloader)
  
  for epoch in range(epochs):
    print('EPOCH: ', epoch)
    for i, data in enumerate(trainloader, 0):
      inputs, labels = data
      inputs, labels = inputs.cuda(), labels.cuda()
      outputs = network(inputs)
      loss = loss_function(outputs, labels)
      loss.backward()
      optimizer.step()
      optimizer.zero_grad()
  print('DONE')
  return network
