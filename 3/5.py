def positive_nums_arr (arr):
    quantity_pos_nums = 0
    for i in arr:
        if i > 0:
            quantity_pos_nums += 1
    return quantity_pos_nums
print(positive_nums_arr([-1,2,-3,-4,52,1337,228,3423]))