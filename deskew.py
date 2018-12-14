import skimage.transform
import math
import torchvision.transforms as transforms
import numpy as np

def sort_rect(l):
  mlat = sum(x[0] for x in l) / len(l)
  mlng = sum(x[1] for x in l) / len(l)
  def algo(x):
    return (math.atan2(x[0] - mlat, x[1] - mlng) + 2 * math.pi) % (2*math.pi)
  l.sort(key=algo)

def deskew(original, dest):
  sort_rect(dest)
  original_tensor = transforms.Compose([
    transforms.ToTensor()
  ])(original)

  _, height, width = original_tensor.shape
  src = np.array([[width, height], [width, 0], [0, 0], [0, height]])
  width_translate = width / 224.0
  height_translate = height / 224.0

  dst = np.array(dest) * np.array([width_translate, height_translate])

  tform = skimage.transform.ProjectiveTransform()
  tform.estimate(src, dst)
  warped = np.uint8(skimage.transform.warp(original, tform) * 255)

  image = transforms.ToPILImage()(warped)

  target_width = np.maximum(
                    np.linalg.norm(np.array(dest[1]) - np.array(dest[2])),
                    np.linalg.norm(np.array(dest[0]) - np.array(dest[3]))
                 )
  target_height = np.maximum(
                    np.linalg.norm(np.array(dest[0]) - np.array(dest[1])),
                    np.linalg.norm(np.array(dest[2]) - np.array(dest[3]))
                  )
  new_width = width
  new_height = target_height * (width / target_width)
  return transforms.Resize((int(new_height), int(new_width)))(image)
