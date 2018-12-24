import requests
from urllib.parse import urlparse

def download_web(url):
  dl = 0
  def progress(data):
    nonlocal dl 
    dl += len(data)
    if dl % 100000 == 0:
      print(dl)
    return data

  res = requests.get(url, stream=True)
  name = urlparse(url).path
  if res.status_code == requests.codes.ok:
    with_progress = (progress(data) for data in res.iter_content(chunk_size=1024))
    yield PipelineSuccess(
      name,
      with_progress
    )
  else:
    print(res.status_code)
