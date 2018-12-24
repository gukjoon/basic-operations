def read_label(i):
    with open(i.result) as f:
        return f.read().strip()
    
def label_map(label_gen):
    label_gen = [read_label(i) for i in label_gen]
    label_set = sorted(set(label_gen))
    return {v: idx for idx, v in enumerate(label_set)}
