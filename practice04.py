def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

score = int(input(" balingni kirit "))
grade = get_grade(score)
print(" baho", grade)