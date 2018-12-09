def input_file(file_iter):
  # pass along generator
  for i in file_iter:
    yield PipelineSuccess(i.name, i)
