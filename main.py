# i don't know why it can not able to find the imAGE PATH

# importing necessary libraries
import img2pdf
from PIL import Image
import os

# storing image path
img_path = "D:\\photos\new 2.jpg"

# storing pdf path
pdf_path = "D:\\100 days of python\Python projects\Image to pdf convertor\pdf_file\file.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.img_path)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")
