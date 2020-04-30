with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    gross = []
    poor = []
    list = my_file.read().split('\n')
    for i in list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        gross.append(i[1])
print(f'Оклад меньше 20k: {poor}, средний оклад: {sum(map(float, gross)) / len(gross)}')

