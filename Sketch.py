import cv2
image = cv2.imread("/User/Desktop/Machine Learning/Sketch/Sketch_images/m.jpg")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#IMAGE PROCESSING
#THIS WILL CONVERT IMAGE TO NEGATIVE FORM BY MINUSING gray_image VALUE WITH 255
inverted = 255-gray_image

#BLURING IMAGE(Many blure filter are there but using GaussianBlur)
blurred = cv2.GaussianBlur(inverted,(21,21),0)
invertedblur = 255-blurred
pencilsketch = cv2.divide(gray_image,invertedblur,scale = 256.0)

cv2.imwrite("/User/Desktop/Machine Learning/Sketch/Sketch_images/6.jpg",pencilsketch)
