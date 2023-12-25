import cv2 

image = cv2.imread('image1.jpg' , 0)
adaptive_mean_img = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,5)
adaptive_gaussian_img = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,5)
threshold1,bw_img = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

cv2.imshow('Original image' , image)
cv2.imshow('adaptive_men_img threshold' , adaptive_mean_img)
cv2.imshow('adaptive gaussian img - threshold' , adaptive_gaussian_img)
cv2.imshow('Binary threshold' , bw_img)

cv2.waitKey()
cv2.destroyAllWindows()
