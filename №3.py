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
while True:
    try:
        C = float(input ("Введите число C: "))
        if C==0:
            print  ("Ошибка: число должно быть положительным или отрицательным, попробуйте снова.")
        else:
            break
    except ValueError:
        print ("Ошибка: введите число.")
count = 0
for element in elements:
    if element>=C:
        count+=1
print (f"Количество элементов, больших {C}: {count}")