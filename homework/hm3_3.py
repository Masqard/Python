# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

m = [randint(0, 15) for _ in range(111)]
print(f'Массив - {m}')

num_mas = 0
for i in m:
    if m.count(num_mas) < m.count(i):
        num_mas = m.index(i)
    else:
        break
    print('Элемент массива уникален, ищем другой')

print(f'Число {m[num_mas]}, встречается {m.count(num_mas)} раза')