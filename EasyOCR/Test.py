import easyocr

reader = easyocr.Reader(['da'],gpu=False)

result = reader.readtext('EasyOCR\\TestResizedGrayScale2.jpg',detail=0, paragraph=True)
print(result)