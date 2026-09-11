import cv2
import numpy as np
from pathlib import Path


PICTURES_DIR = Path(__file__).parent / "Pictures"
CLEAN_IMAGES_DIR = PICTURES_DIR / "CleanImages"


def _clean_image(image_name, folder_name, output_name):
    image_path = PICTURES_DIR / folder_name / image_name
    image = cv2.imread(str(image_path))

    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

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
        gradient_magnitude, 225, 255, cv2.THRESH_BINARY)

    CLEAN_IMAGES_DIR.mkdir(exist_ok=True)
    cv2.imwrite(str(CLEAN_IMAGES_DIR / output_name), thresh_binary)


def answerkey(image_name):
    _clean_image(image_name, "Answerkey", "CleanimageAnswerKey.jpg")


def answersheet(image_name):
    _clean_image(image_name, "Answersheet", "CleanimageAnswerSheet.jpg")