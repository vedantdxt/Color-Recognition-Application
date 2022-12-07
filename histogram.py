import cv2
from PIL import Image
from matplotlib import pyplot as plt

im = Image.open(r"flower.jpg")
im.show()

# reads an input image
img = cv2.imread('flower.jpg',0)

# histogram of an image
plt.hist(img.ravel(),256,[0,256])
plt.show()
