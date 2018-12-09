import os
from PIL import Image
from werkzeug.utils import secure_filename

def input_image(request, upload_folder):
  file = request.files['file']
  filename = secure_filename(file.filename)
  file_path = os.path.join(upload_folder, filename)
  file.save(file_path)
  img = Image.open(file_path)
  if not img.mode == 'RGB':
    img = ImageMath.eval('im/256', {'im':image}).convert('RGB')  
  os.remove(file_path)
  yield PipelineSuccess('image', img)
