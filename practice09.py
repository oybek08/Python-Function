def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        print("Xatolik: Mablag yetarli emas.")
        return balance

def check_balance(balance):
    print("Balansingiz:", balance)

balance = 0.0

while True:
    print("1. Balansni korish")
    print("2. Depozit kiritish")
    print("3. Pul yechish")
    print("4. Chiqish")
    
    tanlov = input("Tanlovni kiriting (1-4): ")
    
    if tanlov == "1":
        check_balance(balance)
    elif tanlov == "2":
        miqdor = float(input("Qancha miqdor kiritmoqchisiz? "))
        balance = deposit(balance, miqdor)
    elif tanlov == "3":
        miqdor = float(input("Qancha pul yechmoqchisiz? "))
        balance = withdraw(balance, miqdor)
    elif tanlov == "4":
        print("Dastur tugadi.")
        break
    else:
        print("Notogri Qayta urinib koring.")