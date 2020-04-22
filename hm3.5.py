def sum ():
    sum_res = 0
    exit = False
    while exit == False:
        number = input('Print numbers or Q for exit: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                exit = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


sum()