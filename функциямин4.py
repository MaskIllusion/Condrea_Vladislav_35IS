def min(a, b):
    if a < b:
        return a
    else:
        return b

def min4(a, b, c, d):
    w = min(a, b)
    w = min(w, c)
    w = min(w, d)
    return w

try:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = int(input("Введите число c: "))
    d = int(input("Введите число d: "))
    
    print("Минимальное число:", min4(a, b, c, d))
except ValueError:
    print("Ошибка! Введите ЦЕЛЫЕ ЧИСЛА!")