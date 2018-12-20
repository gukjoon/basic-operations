import pandas

def extract_labels(file_gen, id_extractor):
  for obj in file_gen:    
    file = obj.result
    in_data = pandas.read_csv(file)
    for idx, i in in_data.iterrows():
      id_raw = i[0]
      label_raw = i[1]
      yield PipelineSuccess(id_extractor % id_raw, label_raw)
