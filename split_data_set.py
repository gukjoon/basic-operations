import itertools

def split_data_set(input, start, end):
  return itertools.islice(input, start, end)
