import cv2
img = cv2.imread('image1.jpg',0)
threshold, OTSUimage = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(img , (5,5) , 0)
threshold , blurOTSUimage = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original' , img)
cv2.imshow('OTSU image' , OTSUimage)
cv2.imshow('blur OTSU image' , blurOTSUimage)

cv2.waitKey(0)
cv2.destroyAllWindows()