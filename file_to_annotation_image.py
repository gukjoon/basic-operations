from PIL import Image
from PIL import ImageFile
from PIL import ImageMath  
# TODO: danger
ImageFile.LOAD_TRUNCATED_IMAGES = True

def file_to_annotation_image(file):
  # Create a copy
  image = Image.open(file)
  if image.mode == 'RGBA':
    r, g, b, a = image.split()
    image = Image.merge('RGB', (a, a, a))
  return image
