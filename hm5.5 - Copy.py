def summ():
    try:
        with open('text_99.txt','w+') as file_obj:
            line = input('Введите цифры через пробел: ')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(float , my_numb )))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summ()