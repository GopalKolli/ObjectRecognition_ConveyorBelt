from PIL import Image

template = Image.open("template.png")
template = template.crop((16,226,494,288))
template.show()
