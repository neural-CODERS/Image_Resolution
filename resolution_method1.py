from PIL import Image
image = "image1.png"
img = Image.open(image)
width, height = img.size
print("The image resolution  is", width, "x", height)
