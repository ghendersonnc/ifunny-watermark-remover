import cv2 as cv
import numpy as np
import matplotlib
import os

"""
This is NOT an AI or ML program
This does NOT detect the presence of any sort of watermark
This simply removes the bottom 20 pixels from an image
"""

# Add image names to a 2D array
imageList = []
for root, dirs, files in os.walk("./images"):
    for filename in files:
        temp = filename.split('.')
        imageList.append(tuple(temp))

for im in imageList:
    # Skip any non jpg/png images
    if im[1] not in ['jpg', 'png']:
        continue
    
    img = cv.imread("./images/{}".format(im[0] + "." + im[1]), cv.IMREAD_COLOR)

    croppedImage = img[0:img.shape[0]-20, 0:img.shape[1]]

    croppedImageFileName = "{}_noifunny{}".format(im[0], "." + im[1])

    # Add images to a new folder
    cv.imwrite("./cropped_images/{}".format(croppedImageFileName), croppedImage)

