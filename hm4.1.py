from sys import argv

name, time, rate, bonus = argv

time = int(time)
rate = int(rate)
bonus = int(bonus)
res = time * rate + bonus
print(f'заработная плата сотрудника:  {res}')


