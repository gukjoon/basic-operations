import torch
import torchvision.transforms as transforms

# auto batches
def run_model(loader, network):
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
