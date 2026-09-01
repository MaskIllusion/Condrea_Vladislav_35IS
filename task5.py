food = {
    "Маша": "каша",
    "Петя": "котлеты",
    "Вова": "борщ"
}

name = input("Имя: ")

if name in food:
    print(f"{name} любит: {food[name]}")
else:
    print("Ошибка! Неизвестное имя.")