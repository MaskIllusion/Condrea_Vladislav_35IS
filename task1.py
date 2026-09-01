def is_number(value):
    try:
        float(value)  
        return True
    except ValueError:
        return False

user_input = input("Введите число: ")
if is_number(user_input):
    print(f"Вы ввели число: {float(user_input)}")
else:
    print("Ошибка!")