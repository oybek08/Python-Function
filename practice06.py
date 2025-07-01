def is_valid_phone_number(phone: str) -> bool:
    return phone.isdigit() and len(phone) == 9

raqam1 = "901234567"
raqam2 = "9981234567"
raqam3 = "90a234567"

print(is_valid_phone_number(raqam1))  
print(is_valid_phone_number(raqam2))
print(is_valid_phone_number(raqam3))