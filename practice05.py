secret_number = 7  

def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print(" 5000$ pul mukofoti yutdingiz 🎉")
    else:
        print("Xato. Yana urinib ko'ring.")

while True:
    user_input = input("1 dan 10 gacha son kiriting: ")
    
    if not user_input.isdigit():
        print("Iltimos, butun son kiriting.")
        continue

    guess = int(user_input)
    result = check_guess(secret_number, guess)
    print_result(result)

    if result:
        break