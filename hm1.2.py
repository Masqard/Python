time = int(input("Введите время в секундах: "))
hour = time // 3600
minute = (time - hour * 3600) // 60
seconds = (time - (hour * 3600 + minute * 60))
print(f'Введеное число секунд в формате чч:мм:сс - это: {hour}:{minute}:{seconds}')