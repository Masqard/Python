class Storage:
    storage = []

    @staticmethod
    def show_depot():
        print('Наличие товара на складе: ')
        for el in Storage.storage:
            print(el)


    @staticmethod
    def move_dep(name, count, name_dep):
        if Storage.valid(name, count, name_dep):
            for el in Storage.storage:
                for key, val in el.items():
                    if name == val:
                        if count <= el['кол-во']:
                            el['кол-во'] -= count
                            if el['кол-во'] == 0:
                                Storage.storage.remove(el)
                            return print(f'Позиция: {name}, кол-во: {count} перемещена в подзразделение: {name_dep}')
                        else:
                            return print('Такого количества нет на складе')
            return print('Такого товара нет на складе')


    @staticmethod
    def valid(name, count, name_dep):
        if not(isinstance(name, str)):
            print('Данные введены некорректно. Наименование должно быть строчным')
            return False
        elif not(isinstance(count, int)):
            print('Данные введены некорректно. Количество должно быть числом')
            return False
        elif not(isinstance(name_dep, str)):
            print('Данные введены некорректно. Название подразделения должно быть строчным')
            return False
        return True

class OfficeEq:
    office_eq = []


    @staticmethod
    def show_office_eq():
        for el in OfficeEq.office_eq:
            print(el)


    @staticmethod
    def move_depot():
        Storage.storage.extend(OfficeEq.office_eq)
        print('Оргтехника перемещена на склад')

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

class Printer(OfficeEq):
    def __init__(self, name, price, count):
        super().__init__(name, price, count)
        OfficeEq.office_eq.append({
            'наименование': self.name,
            'цена': self.price,
            'кол-во': self.count
        })


class Scanner(OfficeEq):
    def __init__(self, name, price, count):
        super().__init__(name, price, count)
        OfficeEq.office_eq.append({
            'наименование': self.name,
            'цена': self.price,
            'кол-во': self.count
        })


class Xerox(OfficeEq):
    def __init__(self, name, price, count):
        super().__init__(name, price, count)
        OfficeEq.office_eq.append({
            'наименование': self.name,
            'цена': self.price,
            'кол-во': self.count
        })

x1 = Xerox('Xerox', 25122, 2)
x2 = Xerox('Canon', 33441, 1)
s1 = Scanner('HP', 12333, 3)
p1 = Printer('Toshiba', 14222, 4)
OfficeEq.show_office_eq()
OfficeEq.move_depot()
Storage.show_depot()
Storage.move_dep('Xerox', 1, 'Бухгалтерия')
Storage.show_depot()
Storage.move_dep('HP', '5', 'Отдел сбыта')
Storage.move_dep(123, 5, 'Отдел сбыта')
Storage.move_dep('HP', 5, 123)