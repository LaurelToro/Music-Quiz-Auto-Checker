import re
from itertools import zip_longest


def split_questions(text):
	questions = re.split(r"(?=\d+\s*:)", text)
	return [
		re.sub(r"^\d+\s*:\s*", "", question).strip()
		for question in questions
		if question.strip()
	]

def crosscheck(answer_contents, user_contents):
    answer_contents = split_questions(" ".join(answer_contents))
    user_contents = split_questions(" ".join(user_contents))
    results = []

    for question_number, (answer, user_answer) in enumerate(
        zip_longest(answer_contents, user_contents, fillvalue=""),
        start=1,
    ):
        if answer.strip().lower() == user_answer.strip().lower():
            results.append(f"Korrekt svar på spørgsmål nr: {question_number}: {answer}")
        else:
            results.append(f"Ikke korrekt svar på: {question_number}:")
            results.append(f"  Korrekt svar: {answer}")
            results.append(f"  Bruger svar: {user_answer}")

    return "\n".join(results)


