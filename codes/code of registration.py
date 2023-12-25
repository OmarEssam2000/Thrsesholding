import cv2
import numpy as np
rotatedimg = cv2.imread("image1.img")
img = cv2.imread("image1.jpg")
orb_detector = cv2.ORB_create(5000)
kp1, d1 = orb_detector.detectAndCompute(rotatedimg,None)
kp2 , d2 = orb_detector.detectAndCompute(img,None)

matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = matcher.match(d1,d2)
matches.sort(key=lambda x: x.distace)
matches = matches[:int(len(matches) * 90)]
no_of_matches = len(matches)
p1 = np.zeros((no_of_matches) , 2)
p2 = np.zeros((no_of_matches) , 2)
for i in range(len(matches)):
    p1[i,:] = kp1[matches[i].queryIdx].pt
    p2[i,:] = kp2[matches[i].trainIdx].pt

homography, mask = cv2.findHomography(p1 , p2 , cv2.RANSAC)
transformed_img = cv2.warperspective(rotatedimg , homography , (255,255))
cv2.imshow('original' , img)
cv2.imshow('rotated' , rotatedimg)
cv2.imshow('align' , transformed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
