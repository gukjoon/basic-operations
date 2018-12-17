import os
import pandas
import requests

def download_dir(file_gen):
  for file in file_gen:
    file = file.result
    in_data = pandas.read_csv(file)
    for idx, i in in_data.iterrows():
      name = file.name + "/" + str(i[0]) + ".dat"
      if str(i[1]).startswith("http"):
        print("Downloading " + i[1])
        res = requests.get(i[1], stream=True)
        if res.status_code == requests.codes.ok:
          yield PipelineSuccess(name, res.iter_content(chunk_size=1024))
        else:
          print(res.status_code)
