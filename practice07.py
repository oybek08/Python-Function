def ask_question(question: str, correct_answer: str):
    user_answer = input(question + " ")
    if check_answer(user_answer, correct_answer):
        print("Togri javob!")
    else:
        print(" Notogri.Togri javob", correct_answer)

def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer.strip().lower() == correct_answer.strip().lower()

ask_question("Ozbekiston poytaxti nima?", "Toshkent")
ask_question("5 + 7 =", "12")