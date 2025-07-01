def calculate_bmi(weight: float, height: float) -> float:
    
    return weight / (height ** 2)

def bmi_status(bmi: float) -> str:

    if bmi < 18.5:
        return 
    elif 18.5 <= bmi < 25:
        return 
    elif 25 <= bmi < 30:
        return 
    else:
        return
ogirlik = 55
boy = 1.80  

bmi = calculate_bmi(ogirlik, boy)
holat = bmi_status(bmi)

print(f"BMI: {bmi:.2f}")
print(f"Holati: {holat}")