class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        self.weigth = 25
        self.depth = 0.05
        mass = self._length * self._width * self.weigth * self.depth / 10
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {mass} т.')


mass = Road(20, 5000)
mass.mass()
