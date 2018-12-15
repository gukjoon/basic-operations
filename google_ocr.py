from google.cloud import vision
from google.cloud.vision import types
import json

client = vision.ImageAnnotatorClient()

def google_ocr(file):
  image = types.Image(content=file.read())
  response = client.document_text_detection(image=image)
  return [response.full_text_annotation.text.encode('UTF-8')]
