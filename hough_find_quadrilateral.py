import numpy as np
import itertools
import math
import scipy

def intersection(s1, s2):
  """
  Return the intersection point of line segments `s1` and `s2`, or
  None if they do not intersect.
  """
  p, r = s1[0], s1[1] - s1[0]
  q, s = s2[0], s2[1] - s2[0]
  rxs = float(np.cross(r, s))
  if rxs == 0: return None
  t = np.cross(q - p, s) / rxs
  u = np.cross(q - p, r) / rxs
  if 0 < t < 1 and 0 < u < 1:
      return p + t * r
  return None

def colinear(a, b, c):
  x1, y1 = a
  x2, y2 = b
  x3, y3 = c
  return ((y2 - y1) / (x2 - x1)) == ((y3 - y1) / (x3 - x1))

def find_quadrilaterals(intersections, row1, col1):
  combos = list(itertools.combinations(intersections, 4))
  for c in combos:
    # filters out linear combinations first for speed
    triples = itertools.combinations(c, 3)
    lin_comb = any(colinear(a, b, c) for a, b, c in triples)
    if not lin_comb:
      ii = []
      segments = itertools.combinations(c, 2)
      for s1, s2 in itertools.combinations(segments, 2):
        inter = intersection(np.array(s1), np.array(s2))
        if not inter is None:
          inter = tuple(np.ndarray.tolist(inter))
          yield s1, s2, inter

def find_best(quads, nd):
  x = np.arange(nd.shape[1])
  y = np.arange(nd.shape[0])
  f = scipy.interpolate.interp2d(x, y, nd)
  num_points = 100

  acc = []
  for p in quads:
    (a, b, inter) = p
    score = 0
    for p0, p1 in ((a[0], b[0]), (a[0], b[1]), (a[1], b[0]), (a[1], b[1])):
        c1, r1 = p0
        c2, r2 = p1
        xvalues = np.linspace(c1, c2, num_points)
        yvalues = np.linspace(r1, r2, num_points)
        zvalues = f(xvalues, yvalues)
        length = np.linalg.norm(np.array(p0) - np.array(p1))
        pct = sum(sum(zvalues)) / 10000
        score += (pct * length)
    acc += [(a, b, score)]
  best = max(acc, key=lambda x: x[2])
  a, b, _ = best

  return [a[0], b[0], a[1], b[1]]

def hough_find_quadrilateral(tensor, intersections):
  _, row1, col1 = tensor.shape
  nd = threshold(tensor.view((row1,col1)).detach().numpy())  
  print(len(intersections))
  if len(intersections) > 21:
    raise ValueError("intersections too high " + str(len(intersections)))
  quads = set(find_quadrilaterals(intersections, row1, col1))
  print(len(quads))
  return find_best(quads, nd)
