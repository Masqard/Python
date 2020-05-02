class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} завелась родимая!'
    def stop(self):
        return f'{self.name} Заглохгла :('
    def turn_right(self):
        return f'{self.name} повернул(а) направо'
    def turn_left(self):
        return f'{self.name} повернул(а) налево'


class TownCar(Car):
    pass

    def show_speed(self):
        print(f'текущая скорость {self.name} - {self.speed}')

        if (self.speed) > 60:
            return f'скорость {self.name} более 60, сбавь!'
        else:
            return f'скорость {self.name} менее 60, поднажми!'


class SportCar(Car):
    pass

class WorkCar(Car):
    pass

    def show_speed(self):
        print(f'текущая скорость {self.name} - {self.speed}')

        if (self.speed) > 40:
            return f'скорость {self.name} более 40, у тебя не феррари,сбавь (день длинный, подождут!)'
        else:
            return f'скорость {self.name} менее 40, мы так никуда не успеем :(!'


class PoliceCar(Car):
    pass

Mazda = TownCar(55, 'белый', 'Mazda', False)
Ferrari = SportCar(188, 'красный', 'Ferrari', False)
Buick = WorkCar(85, 'желтый', 'Buick', False)
Ford = PoliceCar(95, 'бело-синий', 'Ford', True)

print(f'повернул {Ferrari.turn_left()}')
print(f'{Mazda.stop()}')
print(f'{Mazda.go()} и едет  {Mazda.show_speed()}')
print(f'{Buick.name} - {Buick.color}')
print(f' {Ford.name} полицеская машина {Ford.is_police}')
print(f' {Buick.name} полицеская машина {Buick.is_police}')
print(f'{Buick.turn_right()} и едет {Buick.speed}')


