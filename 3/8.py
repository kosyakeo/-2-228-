import random
arr = []
len_arr = random.randint(1,2)
stat = random.randint(0,100) * 3
for i in range(len_arr):
    arr.append (stat -3 * i)
print(arr)