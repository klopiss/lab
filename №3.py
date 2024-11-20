import random
while True:
    try:
        n = int(input("Введите количество элементов в списке: "))
        if n<=0:
            print ("Ошибка: число должно быть положительным, попробуйте снова.")
        else:
            break
    except ValueError:
        print ("Ошибка: введите целое число.")
elements = [random.randint(-10,10) for i in range(n)]
print("Созданный список:", elements)
while True:
    try:
        C = float(input ("Введите число C: "))
        break
    except ValueError:
        print ("Ошибка: введите число.")
count = 0
for element in elements:
    if element>=C:
        count+=1
print (f"Количество элементов, больших {C}: {count}")
negatives = []
positives = []
for x in elements:
    if x<0:
        negatives.append(x)
    else:
        positives.append(x)
Z = negatives + positives
print ("Список с определённой последовательностью: ", Z)