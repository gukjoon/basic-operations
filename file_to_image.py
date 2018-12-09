from PIL import Image
from PIL import ImageFile
from PIL import ImageMath  
# TODO: danger
ImageFile.LOAD_TRUNCATED_IMAGES = True

def file_to_image(file):
  # Create a copy
  image = Image.open(file)
  if not image.mode == 'RGB':
    image = ImageMath.eval('im/256', {'im':image}).convert('RGB')  
  return image
