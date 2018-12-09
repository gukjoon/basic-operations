import numpy as np

def perp(a) :
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = np.dot( dap, db)
    num = np.dot( dap, dp )
    return (num / denom.astype(float))*db + b1

def hough_find_intersections(tensor, lines):
  _, row1, col1 = tensor.shape
  intersections = []
  for line in lines:
    other_lines = [other for other in lines if not other == line]
    for other_line in other_lines:
      inter_x, inter_y = seg_intersect(
        np.array(line[0]), 
        np.array(line[1]), 
        np.array(other_line[0]),
        np.array(other_line[1]))
      intersections += [(round(inter_x, 5), round(inter_y, 5))]
  
  # Filter for inside image
  return set([i for i in intersections if i[0] >= 0 and i[1] >= 0 and i[0] <= row1 and i[1] <= col1])
