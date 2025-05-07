arr = [1,4,5,8,2,3, 19,23, 44]
x = int(input("Enter a number: "))
for i in arr:
    if i == x:
        res = ('содержит')
    else:
        res = ("не содержит")
print(res)