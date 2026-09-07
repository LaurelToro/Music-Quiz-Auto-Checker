from PIL import Image, ImageEnhance, ImageFilter
import pytesseract



#Load billeder
Submit = Image.open('Projekt Quiz/1000009018.jpg')


#Hent tekst fra billederne
textSub = pytesseract.image_to_string(Submit)
print(textSub)

#Clean teksten for at fjerne linjeskift og ekstra mellemrum
CleanText1=textSub.replace('\n', ' ').strip().lower()

#Split teksten i ord
SubmittedWords = CleanText1.split()

print(CleanText1)

#Find de ord, der er ens og de ord, der ikke er ens
#same_words = set(SubmittedWords) & set(AnswerWords)
#unsimilar_words = set(SubmittedWords) - set(AnswerWords)

#Print resultaterne
#if same_words:
    #print("The texts have the following words in common:", same_words)

#if unsimilar_words:
    #print("The texts have the following words that are not in common:", unsimilar_words)
