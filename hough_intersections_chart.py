import json
from matplotlib import pyplot as plt
from PIL import Image
import io

def hough_intersections_chart(tensor, hough_intersections):
  ch, row1, col1 = tensor.shape
  if (ch == 1):
    cmap = 'gray'
  else:
    cmap = 'rgb'
  nd = threshold(tensor.view((row1,col1)).detach().numpy())

  fig = plt.figure()
  ax1 = fig.add_subplot(111)
  ax1.imshow(nd, cmap=cmap)
  for p1, p2 in hough_intersections:
    ax1.plot(p1, p2, markersize=20, marker='o')
  ax1.axis((0, col1, row1, 0))
  ax1.set_axis_off()

  # Draw to image
  buf = io.BytesIO()
  fig.savefig(buf, format='png')
  buf.seek(0)
  pil_image = Image.open(buf)
  plt.close()
  return pil_image
