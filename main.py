while True:
    S = input("Введите строку S: ")
    if S == "":
        print("Ошибка: ввод не должен быть пустым. Попробуйте снова.")
    else:
        break
while True:
    S0 = input("Введите строку S0: ")
    if S0 == "":
            print("Ошибка: ввод не должен быть пустым. Попробуйте снова.")
    else:
        break
if S0 in S:
    index = None
    for i in range(len(S) - len(S0) + 1):
        if S[i:i + len(S0)] == S0:
            index = i
            break
    if index is not None:
        nS = S[:index]+S[index+len(S0):]
        print ("Результат:", nS)
else:
    print ("Результат:", S)


