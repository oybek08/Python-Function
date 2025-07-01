def is_palindrome(text: str) -> bool:
    return text == text[::-1]

print(is_palindrome("olma"))       
print(is_palindrome("12321"))  
print(is_palindrome("Uzbekistan")) 