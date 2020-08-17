# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

x = [i for i in range(2, 100)]
y = [i for i in range(2, 9)]

for a in y:
    counter = 0
    for b in x:
        if b % a == 0:
            counter += 1
    print (f'Кратных числа {a} - равно {counter}')