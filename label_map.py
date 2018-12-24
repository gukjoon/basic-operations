
def label_map(label_gen):
  label_gen = [i.result.read().decode('utf-8').strip() for i in label_gen]
  label_set = sorted(set(label_gen))
  return {v: idx for idx, v in enumerate(label_set)}
