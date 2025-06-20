def change (list):
  if len(list) >= 2:
    list[0], list[-1] = list[-1], list[0]
  else:
    print('ошибка')
  return list
test_list = ['1','2','3',18]
print(change(test_list))
