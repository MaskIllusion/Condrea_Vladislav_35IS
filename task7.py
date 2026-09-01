word = "Программирование"

try:
    number = int(input("Введите номер буквы: "))
    print(word[number])
except:
    print("Ошибка! Неверный номер.")