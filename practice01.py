def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Nolga bolish mumkin emas!"
    return a / b

a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")

if amal == '+':
    natija = add(a, b)
elif amal == '-':
    natija = subtract(a, b)
elif amal == '*':
    natija = multiply(a, b)
elif amal == '/':
    natija = divide(a, b)
else:
    natija = "Notogri amal kiritildi."

print(f"Natija: {natija}")