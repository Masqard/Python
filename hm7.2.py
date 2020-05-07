class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def square_coat(self):
        return round(self.width / 6.5 + 0.5)

    def square_costume(self):
        return round(self.height * 2 + 0.3)

    @property
    def square_all(self):
        square_all = round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3))
        return str(f'Общие затраты ткани на все - {square_all}')



class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = (self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Затраты на пальто - {self.square_coat}'


class Costume(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_costume = (self.height * 2 + 0.3)

    def __str__(self):
        return f'Затраты на костюм - {self.square_costume}'


coat = Coat(13, 2)
costume = Costume(3, 7)
print(coat)
print(costume)
print(costume.square_all)


