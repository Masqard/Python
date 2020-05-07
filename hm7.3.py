class Cell:
    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value if (self.value - other.value) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value // other.value

    def make_order(self, cells_in_row):
         row = ' '
         for i in range(int(self.value / cells_in_row)):
           row += f'{"*" * cells_in_row} \\n'
         row += f'{"*" * (self.value % cells_in_row)}'
         return row

cell_1 = Cell(12)
cell_2 = Cell(15)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(4))