def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    return age
age = calculate_age(2008,2025)
print(age)

if age < 18:
    print("Siz balogatga yetmagansiz")
else:
    print("Siz balogat yoshiga yetgansiz")
