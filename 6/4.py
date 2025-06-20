numbers = [6, -52, 52, 8, 9, 7, 2]
first_positive = next(x for x in numbers if x > 0)
last_negative = next(x for x in reversed(numbers) if x < 0)
print(f"Первый положительный: {first_positive}")
print(f"Последний отрицательный: {last_negative}")