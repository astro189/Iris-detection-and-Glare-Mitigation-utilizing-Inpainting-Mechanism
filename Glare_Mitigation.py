import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

url=r"C:\Users\Shirshak\Desktop\Eye Glare Mitigation\Photos\Screenshot 2023-11-08 031645.png"
img=cv.imread(url)
img_name=os.path.basename(url)
init_shape=img.shape

img=cv.resize(img,(150,120))
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,thresh=cv.threshold(gray,0,255,cv.THRESH_OTSU+cv.THRESH_BINARY_INV)
contours,_=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

filtered_contours = [contour for contour in contours if cv.contourArea(contour) < 100 and cv.contourArea(contour)>10]

contour_mask = np.zeros_like(thresh)
cv.drawContours(contour_mask, filtered_contours, -1, (255), thickness=cv.FILLED)

# cv.drawContours(image=contour_mask, contours=filtered_contours, contourIdx=-1, color=(0, 255, 0), thickness=1, lineType=cv.LINE_AA)
radius=[]
for cnt in filtered_contours:
  rect=cv.minAreaRect(cnt)
  radius.append(rect[1][0])


inpainting_result = cv.inpaint(img, contour_mask,3, cv.INPAINT_TELEA)

inpainting_result=cv.resize(inpainting_result,(init_shape[1],init_shape[0]))

cv.imwrite(f'Corrected Images/corrected_img {img_name}.jpg',inpainting_result)
cv.imshow('Corrected Image',inpainting_result)
cv.waitKey(0)
