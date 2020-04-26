from itertools import cycle


b = 0
my_list = [55, 'ABC', 123, 'abc', None]
for el in cycle(my_list):
    if b > 10:
        break
    print(el,end = ' ')
    b += 1