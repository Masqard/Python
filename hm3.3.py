def func(num1, num2, num3):
    if num1 >= num3 and num2 >= num3:
        return num1 + num2
    elif num1 > num2 and num1 < num3:
        return num1 + num3
    else:
        return num2 + num3

print(f'Сумма чисел  - {func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')
