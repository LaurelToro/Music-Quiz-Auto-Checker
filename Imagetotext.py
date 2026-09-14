import easyocr
from pathlib import Path


CLEAN_IMAGES_DIR = Path(__file__).parent / "Program" / "Pictures" / "CleanImages"

def ImagetoText():
    reader = easyocr.Reader(['da','en'],gpu=False)
    AnswerKeyText = reader.readtext(
        str(CLEAN_IMAGES_DIR / "CleanimageAnswerKey.png"),
        detail=0,
        paragraph=True,
    )
    AnswerSheetText = reader.readtext(
        str(CLEAN_IMAGES_DIR / "CleanimageAnswerSheet.png"),
        detail=0,
        paragraph=True,
    )
    return AnswerKeyText, AnswerSheetText

