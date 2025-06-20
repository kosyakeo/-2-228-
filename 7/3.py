numbers = [666, -5, 23, 3, 52, 99, 52, 7, -12, -56, 0, -78]
result = [x for x in numbers if 10 <= x <= 99]
result.sort()
print(result)