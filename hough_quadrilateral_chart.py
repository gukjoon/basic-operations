import json
from matplotlib import pyplot as plt
from PIL import Image
import io

def hough_quadrilateral_chart(tensor, hough_quadrilateral):
  ch, row1, col1 = tensor.shape
  if (ch == 1):
    cmap = 'gray'
  else:
    cmap = 'rgb'
  nd = threshold(tensor.view((row1,col1)).detach().numpy())

  fig = plt.figure()
  ax1 = fig.add_subplot(111)
  ax1.imshow(nd, cmap=cmap)
  p1, p2, p3, p4 = hough_quadrilateral
  ax1.plot((p1[0], p2[0]), (p1[1], p2[1]), '-r')
  ax1.plot((p2[0], p3[0]), (p2[1], p3[1]), '-r')
  ax1.plot((p3[0], p4[0]), (p3[1], p4[1]), '-r')
  ax1.plot((p4[0], p1[0]), (p4[1], p1[1]), '-r')
  ax1.axis((0, col1, row1, 0))
  ax1.set_axis_off()

  # Draw to image
  buf = io.BytesIO()
  fig.savefig(buf, format='png')
  buf.seek(0)
  pil_image = Image.open(buf)
  plt.close()
  return pil_image
