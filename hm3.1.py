def func (*args):

    try:
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        result = num_1 / num_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return 'Wrong number! u can`t use null'
    return result

print(f'result {func()}')
