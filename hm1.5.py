profit = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))
if profit > costs:
    print(f'Фирма работает с прибылью.Рентабельность выручки составила {profit / costs:.2f} ')
    workers = int(input('Введите число сотрудников фирмы: '))
    print(f'Фирма работает с прибылью. Прибыль на одного сотрудника: {profit / workers:.2f} ')
elif profit == costs:
    print('Фирма работает в ноль')
else:
    print("Фирма работает в убыток")
