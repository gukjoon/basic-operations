import io

def image_to_bytes_exif(img, original):
  exif = original.info.get('exif')
  stream = io.BytesIO()
  if exif:
    img.save(stream, 'JPEG', exif=exif)
  else:
    img.save(stream, 'JPEG')
  stream.seek(0)
  def read_file():
    return stream.read()
  gen = iter(read_file, b'')
  return gen
