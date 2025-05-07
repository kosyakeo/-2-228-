new_dict = []
while True:
    i = input('eter something, press Enter for exit ')
    if i == '':
        break
    new_dict.append (i)
min_num = min(new_dict, key=len)
max_num = max (new_dict, key=len)
print(f"{new_dict} max element is '{max_num}', min element is '{min_num}'")