
def tensor_to_points(tensor):
  as_list = tensor.tolist()
  return [
    {
      'x': as_list[0],
      'y': as_list[1]
    },
    {
      'x': as_list[2],
      'y': as_list[3]
    },
    {
      'x': as_list[4],
      'y': as_list[5]
    },
    {
      'x': as_list[6],
      'y': as_list[7]
    }
  ]