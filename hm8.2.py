class Error:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def divison_null(a, b):
        try:
            return (a / b)
        except:
            return (f"Деление на ноль недопустимо")

divison = Error(10,30)
print(Error.divison_null(10, 0))
print(Error.divison_null(10, 2))


