import cv2 as cv

slabs = []
for i in range(2):
    images = []
    for j in range(2):
        effect = int(input("Select effect for {},{} : ".format(i,j)))
        img = cv.imread("output" + str(effect) + ".jpg")
        images.append(img)
    slab = cv.hconcat(images)
    slabs.append(slab)
combined = cv.vconcat(slabs)

cv.imwrite("combined.jpg", combined)