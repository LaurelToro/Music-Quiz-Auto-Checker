import docx2txt



# extract text
text = docx2txt.process("Projekt Quiz/Musik quiz Oktober.docx")

CleanText=text.replace('\n', ' ').replace('_', ' ').strip().lower()

list_of_words = set(CleanText.split())

print(text)
print(CleanText)
print(list_of_words)

