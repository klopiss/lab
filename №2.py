while True:
    text = input("Введите текст: ")
    if text == "":
        print("Ошибка: ввод не должен быть пустым. Попробуйте снова.")
    else:
        break
words = text.split()
while True:
    number = input("Введите номер слова: ")
    if number == "":
        print ("Ошибка: ввод не должен быть пустым. Попробуйте снова.")
        continue
    try:
        number = int(number)
        if 1 <= number <= len(words):
            print(f"Слово под номером {number}: {words[number - 1]}")
            break
        else:
            print ("Ошибка: число не входит в диапазон")
    except ValueError:
        print ("Это не число, попробуйте ещё раз")
