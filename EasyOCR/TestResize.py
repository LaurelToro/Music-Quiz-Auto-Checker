import cv2
import numpy as np
 
# Load the image
image = cv2.imread("EasyOCR\\TestEdgeDetection.jpg")
 
# Define new width and height
new_width = 600
new_height = 500
 
# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

image = resized_image

#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh_binary = cv2.threshold(
    resized_image, 120, 255, cv2.THRESH_BINARY)



cv2.imwrite("EasyOCR\\TestResizedGrayScale3.jpg", thresh_binary)