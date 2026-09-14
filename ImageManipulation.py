import cv2
from pathlib import Path


PICTURES_DIR = Path(__file__).parent / "Program" / "Pictures"
CLEAN_IMAGES_DIR = PICTURES_DIR / "CleanImages"


def _clean_image(image_path, output_name):
    image_path = Path(image_path)
    image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    resized_image = cv2.resize(
        image,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC,
    )
    contrast_image = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8),
    ).apply(resized_image)
    blurred_image = cv2.GaussianBlur(contrast_image, (5, 5), 0)
    thresh_binary = cv2.adaptiveThreshold(
        blurred_image,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11,
    )
    thresh_binary = cv2.copyMakeBorder(
        thresh_binary,
        20,
        20,
        20,
        20,
        cv2.BORDER_CONSTANT,
        value=255,
    )

    CLEAN_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(CLEAN_IMAGES_DIR / output_name), thresh_binary)


def answerkey(image_path):
    _clean_image(image_path, "CleanimageAnswerKey.png")


def answersheet(image_path):
    _clean_image(image_path, "CleanimageAnswerSheet.png")