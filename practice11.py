def calculate_tax(salary: float) -> float:
    if salary > 5_000_000:
        tax_rate = 0.20 
    else:
        tax_rate = 0.13  
    return salary * tax_rate

def calculate_net_salary(salary: float) -> float:
    tax = calculate_tax(salary)
    return salary - tax

maosh = 6_000_000
soliq = calculate_tax(maosh)
sof_maosh = calculate_net_salary(maosh)

print(f"Jami maosh: {maosh} so'm")
print(f"Hisoblangan soliq: {soliq} so'm")
print(f"Sof maosh: {sof_maosh} so'm")