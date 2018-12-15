import torch.optim as optim
import torch.nn as nn
import torch.onnx
import torch

from torch.autograd import Variable
from tensorboardX import SummaryWriter

# class ProgressiveLoader:
#   def __init__(self, image_generator, transforms_in):
#     self.image_gen = list(image_generator)
#     self.transform = transforms.Compose(transforms_in)

#   def __getitem__(self, index):
#     image = self.image_gen[index].result
#     print(image)
#     return self.transform(image)

#   def name_for(self, index):
#     return self.image_gen[index].name

#   def __len__(self):
#     return len(self.image_gen)


def train(images_generator, labels_generator, network, loss_function, optimizer_f, epochs):
  # optimizer, scheduler = optimizer_f(network)
  # filtered_images = (i for i in images_generator if isinstance(i, PipelineSuccess))  
  # dataset = ProgressiveLoader(filtered_images, transforms_in)
  # trainloader = torch.utils.data.DataLoader(
  #   dataset, 
  #   batch_size=batch_size
  #   # num_workers=2
  # )

  # data_size = len(trainloader)
  # for epoch in range(epochs):  # loop over the dataset multiple times
  #   for i, data in enumerate(trainloader, 0):
  #     iteration = (epoch * data_size) + i
  #     # get the inputs
  #     inputs, labels = data
  #     inputs, labels = inputs.cuda(), labels.cuda()
  #     # forward + backward + optimize
  #     outputs = network(inputs)
  #     loss = criterion(outputs, labels)
  #     loss.backward()
  #     # print statistics
  #     if (iteration % self.nbatch_size) == 0:
  #       optimizer.step()
  #       # zero the parameter gradients
  #       optimizer.zero_grad()

  #   # adjust lr every epoch
  #   if self.scheduler:
  #     self.scheduler.step() 
  yield network


# class LoggingContext:
#   def __init__(self, epoch, i, iteration, network, outputs, loss):
#     self.epoch = epoch
#     self.i = i
#     self.iteration = iteration
#     self.network = network
#     self.outputs = outputs
#     self.loss = loss

# class Trainer:

#   def __init__(self, dataset, network, criterion, optimizer_f, nbatch_size, loggers):
#     # loss function
#     self.criterion = criterion
#     self.network = network.cuda()
#     self.optimizer, self.scheduler = optimizer_f(network)
#     # optim.Adam(network.parameters(), lr=0.00001)
#     # self.optimizer = optim.SGD(network.parameters(), lr=0.001, momentum=0.9)
#     self.loader = torch.utils.data.DataLoader(dataset, batch_size=4,
#                                           shuffle=False, num_workers=2)
#     self.loggers = loggers

#     writer = SummaryWriter(comment='Net1')
#     for logger in loggers:
#       logger.writer = writer
#       logger.data_size = len(self.loader)

#     self.nbatch_size = nbatch_size

#   def train(self, epochs):
#     optimizer = self.optimizer
#     criterion = self.criterion
#     trainloader = self.loader
#     network = self.network

#     data_size = len(trainloader)
#     for epoch in range(epochs):  # loop over the dataset multiple times
#       for i, data in enumerate(trainloader, 0):
#         iteration = (epoch * data_size) + i
#         # get the inputs
#         inputs, labels = data
#         inputs, labels = inputs.cuda(), labels.cuda()
#         # forward + backward + optimize
#         outputs = network(inputs)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         # print statistics
#         if (iteration % self.nbatch_size) == 0:
#           optimizer.step()
#           # zero the parameter gradients
#           optimizer.zero_grad()

#         context = LoggingContext(epoch, i, iteration, network, outputs, loss)
#         for t in self.loggers:
#           t.run(context)

#       # adjust lr every epoch
#       if self.scheduler:
#         self.scheduler.step()

#   def save(self, f):
#     torch.save(self.network.state_dict(), f)

#   def save_onnx(self, f):
#     dummy_input = Variable(torch.randn(4, 3, 224, 224)).cuda()
#     torch.onnx.export(self.network, dummy_input, f, verbose=True)

#   def save_pth(self, f):
#     torch.save(self.network, f)
