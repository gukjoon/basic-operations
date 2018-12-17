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
    self.transform = transforms.Compose(transforms_in)

  def __getitem__(self, index):
    image = self.image_gen[index]
    label = self.label_gen[index]
    return (self.transform(image), self.transform(label))

  def __len__(self):
    return len(self.image_gen)


def train(images_generator, labels_generator, network, optimizer, loss_function, epochs):
    network = network.cuda()
    optimizer, scheduler = optimizer
    images_generator = list(images_generator)
    labels_generator = list(labels_generator)
    file_names = set([f.name for f in images_generator]).intersection(set([f.name for f in labels_generator]))
    filtered_images = [file_to_image(i.result) for i in images_generator if i.name in file_names]
    filtered_labels = [file_to_annotation_image(i.result) for i in labels_generator if i.name in file_names]
    dataset = ProgressiveLoader(filtered_images, filtered_labels, [
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
    return network

#   def save_onnx(self, f):
#     dummy_input = Variable(torch.randn(4, 3, 224, 224)).cuda()
#     torch.onnx.export(self.network, dummy_input, f, verbose=True)

#   def save_pth(self, f):
#     torch.save(self.network, f)



