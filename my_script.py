import numpy as np
from skimage.io import imread
from my_library import segment_image

# load image
image = imread('blobs.tif')

# segment image
labels = segment_image(image)

# count objects
number_of_objects = labels.max()
print('Number of objects', number_of_objects)
