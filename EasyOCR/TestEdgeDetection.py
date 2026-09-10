import cv2
import numpy as np

image=cv2.imread('EasyOCR\\TestImg.jpg')

resized_image = cv2.resize(image,(600, 500))

# Load image in grayscale
img = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)


# Apply Sobel operator
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Horizontal edges
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Vertical edges
 
# Compute gradient magnitude
gradient_magnitude = cv2.magnitude(sobelx, sobely)
 
# Convert to uint8
gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)

_, thresh_binary = cv2.threshold(
    gradient_magnitude, 245, 255, cv2.THRESH_BINARY)

cv2.imwrite('EasyOCR\\TestEdgeDetection2.jpg', thresh_binary)