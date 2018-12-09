import skimage.io
from skimage import feature
from skimage import transform
import numpy as np
from skimage.filters import threshold_otsu
import itertools

def threshold(tensor):
  thresh = threshold_otsu(tensor)
  return tensor >= thresh

def find_lines(nd, row1, col1):
  h, theta, d = skimage.transform.hough_line(nd)
  lines = [
      ((0, 0), (0, col1)),
      ((row1, 0), (row1, col1)),
      ((0, 0), (row1, 0)),
      ((0, col1), (row1, col1))
  ]
  for _, angle, dist in zip(*skimage.transform.hough_line_peaks(h, theta, d, min_distance=20, min_angle=20, num_peaks=6)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - col1 * np.cos(angle)) / np.sin(angle)
    p1 = (0, y0)
    p2 = (col1, y1)
    
    lines += [(p1, p2)]
  return lines

def hough_find_lines(tensor):
  ch, row1, col1 = tensor.shape
  assert(ch == 1)
  nd = threshold(tensor.view((row1,col1)).detach().numpy())
  lines = find_lines(nd, row1, col1)
  return lines
