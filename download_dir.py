import os
import pandas
import requests

def download_dir(file_gen, id_col, url_col):
  for file in file_gen:
    file = file.result
    in_data = pandas.read_csv(file)
    for idx, i in in_data.iterrows():
      name = file.name + "/" + str(i[id_col]) + ".dat"
      url = i[url_col]
      if str(url).startswith("http"):
        print("Downloading " + url)
        res = requests.get(url, stream=True)
        if res.status_code == requests.codes.ok:
          yield PipelineSuccess(
            file.base, 
            name,
            res.iter_content(chunk_size=1024)
          )
        else:
          print(res.status_code)
