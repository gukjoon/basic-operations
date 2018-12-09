import torchvision.transforms as transforms

def tensor_to_image(tensor):
  return transforms.ToPILImage()(tensor)

    # img_io = BytesIO()
    # pil_image.save(img_io, 'PNG')
    # img_io.seek(0)  
