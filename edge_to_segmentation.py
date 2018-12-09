import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from skimage import morphology

def fill(data, start_coords, fill_value):
  xsize, ysize = data.shape
  (xloc, yloc) = start_coords
  orig_value = data[xloc, yloc]
  stack = set(((xloc, yloc),))
  if fill_value == orig_value:
    raise ValueError("Filling region with same value "
                 "already present is unsupported. "
                 "Did you already fill this region?")
  while stack:
    x, y = stack.pop()
    if data[x, y] == orig_value:
      data[x, y] = fill_value
      if x > 0:
        stack.add((x - 1, y))
      if x < (xsize - 1):
        stack.add((x + 1, y))
      if y > 0:
        stack.add((x, y - 1))
      if y < (ysize - 1):
        stack.add((x, y + 1))

def edge_to_segmentation(data, label):
  kernel = np.ones((30,30), np.uint8)
  label_arr = np.array(transforms.Grayscale(1)(label))
  label_arr = morphology.erosion(
    morphology.dilation(label_arr, kernel), 
    kernel
  )
  fill(label_arr, map(lambda x: int(x / 2), label_arr.shape), 255)
  return Image.fromarray(label_arr);
