def add_pos(arr):
    res = 1
    for i in range (len(arr)):
        if i % 2 != 0:
            res *= arr[i]
    return res
print (add_pos([1,3,5,5,6]))