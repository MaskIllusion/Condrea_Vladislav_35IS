password = input("Введите пароль: ")

if len(password) >= 4:
    print("Пароль принят")
else:
    print("Ошибка! Пароль должен быть минимум 4 буквы.")