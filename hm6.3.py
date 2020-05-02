class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    pass

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position('Василий', 'Пупкин','Администратор сайта', 50000, 17682.01)
print(f'Его зовут: {a.get_full_name()}')
print(f'Василий, занимает позицию - {a.position},')
print(f'а получается Василий : {a.get_total_income()} рубликов')