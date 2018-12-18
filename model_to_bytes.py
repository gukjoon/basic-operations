import torch
import io

def model_to_bytes(model):
  stream = io.BytesIO()
  torch.save(model.state_dict(), stream)
  stream.seek(0)
  def read_file():
    return stream.read()
  gen = iter(read_file, b'')
  return gen
