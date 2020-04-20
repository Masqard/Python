num = int(input('Number: '))
my_list = [7, 5, 3, 3, 2]
a = my_list.count(num)
for element in my_list:
    if a > 0:
        i = my_list.index(num)
        my_list.insert(i+a, num)
        break
    else:
        if num > element:
            b = my_list.index(element)
            my_list.insert(b, num)
            break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)
print(my_list)
