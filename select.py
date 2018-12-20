def select(file_generator, str_filter):
  for file in file_generator:
    if(file.name.startswith(str_filter)):
      yield file
