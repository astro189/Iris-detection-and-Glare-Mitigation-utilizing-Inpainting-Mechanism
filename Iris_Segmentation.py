import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def iris_segmentation(image_path):

    eye_image = cv.imread(image_path)
    init_shape=eye_image.shape

    eye_image=cv.resize(eye_image,(150,120))

    gray=cv.cvtColor(eye_image,cv.COLOR_BGR2GRAY)
    blurred=cv.GaussianBlur(gray,(3,3),2,2);

    edges = cv.Canny(blurred,50,100)
    circles = cv.HoughCircles(
        edges,
        cv.HOUGH_GRADIENT,
        dp=1,
        minDist=50,
        param1=100,
        param2=30,
        minRadius=10,
        maxRadius=30
    )
    contour_mask = np.zeros((eye_image.shape[0],eye_image.shape[1]),np.uint8)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:

            # cv.circle(eye_image, (i[0], i[1]), i[2], (0, 255,0), 2)
            # cv.circle(eye_image, (i[0], i[1]), 2, (0, 0, 255), 3)
            cv.circle(contour_mask, (i[0], i[1]), i[2], (255, 255,255), -1)



    eye_image=cv.bitwise_and(eye_image,eye_image,mask=contour_mask)
    gray=cv.cvtColor(eye_image,cv.COLOR_BGR2GRAY)

    _,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
    contours,_=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
    thresh=cv.cvtColor(thresh,cv.COLOR_GRAY2BGR)


    for contour in contours:

        epsilon = 0.02 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)

        if len(approx) >= 8:
          cv.drawContours(contour_mask, [approx], 0, (0, 0, 255), 5)

    erosion=cv.erode(thresh,np.ones((2,2),np.uint8),iterations=1)
    dilate=cv.dilate(cv.bitwise_not(thresh),np.ones((2,2),np.uint8),iterations=1)
    dilate=cv.bitwise_not(dilate)
    # remove=cv.subtract(gray,dilate)
    eye_image=cv.subtract(eye_image,thresh)
    eye_image=cv.resize(eye_image,(init_shape[1],init_shape[0]))
    # plt.imsave('/content/iris_detected.jpg',eye_image)

    #plt.imshow(cv.bitwise_not(dilate),cmap='gray')
    plt.imshow(eye_image,cmap="gray")
    return eye_image

url=r'C:\Users\Shirshak\Desktop\Eye Glare Mitigation\Corrected Images\corrected_img.jpg'
eye_image=iris_segmentation(url)
img_name=os.path.basename(url)

cv.imwrite(f"Segmented Images/Segmented image {img_name}",eye_image)
cv.imshow('Segmented Image',eye_image)
cv.waitKey(0)
