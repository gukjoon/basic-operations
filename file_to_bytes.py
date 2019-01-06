import os

def file_to_bytes(file):
  f = file.name
  def read_file():
    return file.read(1024)
  return iter(read_file, b'')
