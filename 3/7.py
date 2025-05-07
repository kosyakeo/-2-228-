def num_ordered(num):
    list_num = str(num)
    for i in range(len(list_num) - 1):
        if list_num[i] <= list_num[i-1]:
            return print('не расположены по убыванию')
    return print("расположены по убыванию")
num_ordered(7431)
num_ordered(7891)