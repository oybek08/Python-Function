def c_to_f(celsius: float) -> float:
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

s_c = 25  
s_f = c_to_f(s_c)
print(f"{s_c}°C = {s_f:.2f}°F")

f_f = 77 
f_c = f_to_c(f_f)
print(f"{f_f}°F = {f_c:.2f}°C")