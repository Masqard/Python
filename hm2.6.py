items = []

my_dict = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед': []
}
goods = int(input('Введите количеств позиций: '))
n = 1
while goods >= n:
    item = input('название товара: ')
    my_dict['название'].append(item)
    price = input('введите цену: ')
    my_dict['цена'].append(price)
    quantity = input('введите кол-во товара: ')
    my_dict['количество'].append(quantity)
    unit = input('Введите единицу измерения: ')
    my_dict['ед'].append(unit)
    ite = (n, {'название': item, 'цена': price, 'количество': quantity, 'ед': unit})
    items.append(ite)
    n += 1

    for el in items:
        print(el)

print(my_dict)