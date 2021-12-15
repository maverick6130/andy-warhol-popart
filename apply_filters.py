import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Filter is defined as a tuple of [b,g,r]
# (x,y) where y is assigned to the light regions
# and x is assigned to the dark regions of the image
filters = [
    ([255,0,0],[255,255,0]), # blue-lightblue
    ([0,0,255],[0,255,255]), # red-yellow 
    ([255,0,0],[0,128,255]), #blue-orange
    ([255,0,255],[0,255,0]), #purple-green
]

path_to_img = input("Please enter the path to the image: ")
img = cv.imread(path_to_img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
normalized = cv.normalize(gray, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)
bw = cv.threshold(normalized, 127, 255, cv.THRESH_BINARY)[1]
w,h = bw.shape

for effect in range(len(filters)):
    output = np.zeros((w,h,3), np.uint8)
    output[bw==0] = filters[effect][0]
    output[bw==255] = filters[effect][1]
    cv.imwrite("output" + str(effect) + ".jpg", output)