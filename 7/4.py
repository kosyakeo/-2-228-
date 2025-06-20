sessions = [
    ["A1", 2023, 5, 60],
    ["B2", 2023, 6, 45],
    ["C3", 2023, 7, 90],
    ["D4", 2023, 8, 30],
    ["E5", 2023, 9, 120]
]
max_time = sessions[0]
min_time = sessions[0]
for s in sessions:
    if s[3] > max_time[3]:
        max_time = s
    if s[3] < min_time[3]:
        min_time = s
print(f"Самое долгое занятие: {max_time[0]} ({max_time[3]} минут)")
print(f"Самое короткое занятие: {min_time[0]} ({min_time[3]} минут)")