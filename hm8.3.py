class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Попробовать еще раз? Yes/No ')

                if y_or_n == 'Yes' or y_or_n == 'yes':
                    print(try_except.my_input())
                elif y_or_n == 'No' or y_or_n == 'no':
                    return f'Вы вышли'
                break

try_except = Error(1)
print(try_except.my_input())
