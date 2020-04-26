from functools import reduce

def my_func(el1, el2):
    return el1 * el2


print(f'Результат перемножения всех элементов списка: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')