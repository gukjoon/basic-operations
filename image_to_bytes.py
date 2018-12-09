import io

def image_to_bytes(img):
  stream = io.BytesIO()
  img.save(stream, 'PNG')
  stream.seek(0)
  def read_file():
    return stream.read()
  gen = iter(read_file, b'')
  return gen
