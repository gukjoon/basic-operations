import zipfile

def unzip(file_generator):
  for file in file_generator:
    with zipfile.ZipFile(file.result.name, 'r') as zipped
      for name in zipped.namelist():
        yield PipelineSuccess(file.name + '/' + name, zipped.open(name, 'rb'))
