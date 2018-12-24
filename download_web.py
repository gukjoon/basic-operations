import requests
from urllib.parse import urlparse

def download_web(url):
  res = requests.get(url, stream=True)
  name = urlparse(url).path
  if res.status_code == requests.codes.ok:
    yield PipelineSuccess(
      name,
      res.iter_content(chunk_size=1024)
    )
  else:
    print(res.status_code)
