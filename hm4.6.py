from itertools import count


a = 0
for el in count(int(input('Стартовая цифра: '))):
    if a > 10:
        break
    print(el, end = ' ')
    a += 1