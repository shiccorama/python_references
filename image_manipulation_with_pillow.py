
## tutorials : https://pillow.readthedocs.io/en/stable/reference/ImageColor.html
image_manipulation_with_pillow.py

# first install the package :
# pip install Pillow

from PIL import image

# open the image
myImage = Image.open(r"path")

# show the image
myImage.show()

# crop image
cropBox = (10,200,300,600)  #(left, upper,right,lower)
newImage = myImage.crop(cropBox)

# show cropped image
newImage.show()


## difference between docstring and comments are:
""" this is doc string which define the function and its parameters
and can be in single or multiple lines.
It shows in help() and in __doc__ functions when recalls
"""
## of course, this is a commment

# next course (pylint)
