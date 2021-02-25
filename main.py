import cv2 as cv
import numpy as np
import os

"""
Detects and removes iFunny watermark from images
"""

def detect_mark(img):
    watermark = cv.imread('assets/watermark.png', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(img, watermark, cv.TM_CCOEFF_NORMED)

    threshold = .90

    # Add regions that have confidence above or at 90%
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    if locations:
        return True
    else:
        return False

def main():

    # Add images to a list
    image_list = []
    for root, dirs, files in os.walk("./images"):
        for filename in files:
            temp = filename.split('.')
            image_list.append(tuple(temp))

    for image in image_list:
        if image[1] not in ["jpg", "png"]:
            continue

        img = cv.imread("images/{}".format(image[0] + "." + image[1]), cv.IMREAD_COLOR)

        # Don't crop or store image if there is no logo
        if (detect_mark(img)):
            cropped_image = img[0:img.shape[0]-20, 0:img.shape[1]]
            cropped_image_filename = "{}_nomark{}".format(image[0], "." + image[1])
            cv.imwrite("images/{}".format(cropped_image_filename), cropped_image)
        else:
            continue




if __name__ == "__main__":
    main()