while True:
    try:
        n = int(input("Введите количество элементов в списке: "))
        if n<=0:
            print ("Ошибка: число должно быть положительным, попробуйте снова.")
        else:
            break
    except ValueError:
        print ("Ошибка: введите целое число.")
print ("Введите элементы списка (по одному числу): ")
elements = []
for i in range(n):
    while True:
        try:
            number = float(input(f"Введите элемент списка {i+1}: "))
            elements.append(number)
            break
        except ValueError:
            print ("Это не число или введено больше 1 числа, попробуйте ещё раз")
negatives = [x for x in elements if x<0]
positives = [x for x in elements if x >= 0]
Z = negatives + positives
print ("Список с определённой последовательностью: ", Z)
