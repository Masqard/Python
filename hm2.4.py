str =input('Enter string: ')
a = str.split(' ')
for i, el in enumerate(a, 1):
    if len(str) > 10:
        el = el [0:10]
        print(f'{i} - {el}')



