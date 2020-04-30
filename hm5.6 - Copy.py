my_dict =dict()
with open ('text_6.txt', 'r') as object:
    lines = object.readlines()
    for line in lines:
        splitted_line = line.split()
        subj = splitted_line[0]
        sum_les = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
        my_dict[subj] = sum_les
    print(my_dict)
