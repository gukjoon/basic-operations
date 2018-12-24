import json

def label_map_to_bytes(label_map):
  return [json.dumps(label_map).encode('utf-8')]
