def is_strong_password(password: str) -> bool:
    return len(password) > 8

parol = "12345677"
natija = is_strong_password(parol)

if natija:
    print("Parol kuchli ")
else:
    print("Parol kuchsiz ")