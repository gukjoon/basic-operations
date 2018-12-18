def intersection(lhs, rhs):
  # rhs to set
  names = set(map(lambda x: x.name, rhs))
  for i in lhs:
    if i.name in names:
      yield i
