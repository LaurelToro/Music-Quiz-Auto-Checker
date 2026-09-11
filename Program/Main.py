import easyocr
import os
import time
from Imagetotext import ImagetoText
from ImageManipulation import answerkey, answersheet


def compare_results(answer_key_text, answer_sheet_text):
    answer_key = [" ".join(text.casefold().split()) for text in answer_key_text]
    answer_sheet = [" ".join(text.casefold().split()) for text in answer_sheet_text]
    total_answers = max(len(answer_key), len(answer_sheet))
    correct_answers = 0

    print("\n" + "=" * 70)
    print("SAMMENLIGNING")
    print("=" * 70)

    for answer_number in range(total_answers):
        expected = answer_key[answer_number] if answer_number < len(answer_key) else "Mangler"
        submitted = answer_sheet[answer_number] if answer_number < len(answer_sheet) else "Mangler"
        is_correct = expected == submitted and expected != "Mangler"

        if is_correct:
            correct_answers += 1
            result = "KORREKT"
        else:
            result = "FORKERT"

        print(f"{answer_number + 1}. {result}")
        print(f"   Svarnøgle: {expected}")
        print(f"   Svarark:   {submitted}")

    print("-" * 70)
    print(f"Resultat: {correct_answers}/{total_answers} korrekte")


Active=True

while Active:
    print("#######################################################################################################")
    print("Velkommen til Music Quiz Auto Checker!\n")
    print("Bare upload din svarnøgle og dit udfyldte svarark, og dette program vil automatisk tjekke det!\n")
    print("Der er en stor chance for at programmet tager fejl, håndskrift er besværligt at læse for en computer.")
    print("#######################################################################################################")
    print("Bare upload dine billeder i deres respektive mapper og fortæl hvad de hedder, (image.png fx) og gør det samme med dit svar")
    answer_key_name = input("Skriv navnet på din svarnøgle her: ")
    answer_sheet_name = input("Skriv navnet på dit svarark her: ")
    
    answerkey(answer_key_name)
    answersheet(answer_sheet_name)
    print("Billederne er behandlet.")
    time.sleep(2)
    answer_key_text, answer_sheet_text = ImagetoText()
    compare_results(answer_key_text, answer_sheet_text)
    print("Tekst er behandlet")
    #os.remove("Program\\Pictures\\CleanImages\\CleanimageAnswerKey.jpg")
    #os.remove("Program\\Pictures\\CleanImages\\CleanimageAnswerSheet.jpg")
    Active = False
    break



