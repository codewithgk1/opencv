import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cat',img)

#Converting to greyscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

#Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

#Edge Cascade
edges = cv.Canny(blur,125,175)
# cv.imshow('Edges',edges)

#Dilating the image
dilated = cv.dilate(edges,(7,7),iterations=1)
# cv.imshow('Dilated',dilated)

#Eroding
eroded = cv.erode(dilated,(7,7),iterations=1)
# cv.imshow('Eroded',eroded)

#Resize
resize = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resize',resize)

#Cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)