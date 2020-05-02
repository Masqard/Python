class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Отрисовка маркером')


pen = Pen('Ручкой')
pencil = Pencil('Карандашом')
handle = Handle('Маркером')
pen.draw()
pencil.draw()
handle.draw()