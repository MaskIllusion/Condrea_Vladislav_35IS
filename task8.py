try:
    file = open("hello.txt", "r", encoding="utf-8")
    print(file.read())
    file.close()
except:
    print("Ошибка! Файл не найден.")