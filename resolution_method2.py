def image_resolution(filemame):
  with open(filename,'rb') as img:
    img.seek(163)
    x = img.read(2)
    height = (x[0]<<8) + x[1]
    x = img.read(2)
    width = (x[0]<< 8) + x[1]
  print("Width X Height : ",width,"X",height)
 image_resolution("image_name.png")
