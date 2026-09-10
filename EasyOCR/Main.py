import easyocr

reader = easyocr.Reader(['da','en'],gpu=False)

result = reader.readtext('EasyOCR\\TestEdgeDetection2.jpg',detail=0, paragraph=True)
print(result)
