def season_events (number_of_months):
  if number_of_months < 1 or number_of_months > 12 or not
isinstance(number_of_months, int):
    print("Введите номер месяца от 1 до 12")
    return 'Ошибка'
  month ={
    1: "Январе",
    2: "Феврале",
    3: "Марте",
    4: "Апреле",
    5: "Мае",
    6: "Июне",
    7: "Июле",
    8: "Августе",
    9: "Сентябре",
    10: "Октябре",
    11: "Ноябре",
    12: "Декабре",
  }
  if number_of_months in [12, 1, 2]:
    res = 'За окном падал белый снег'
  elif number_of_months in [3, 4, 5]:
    res = 'Птицы пели прекрасные песни'
  elif number_of_months in [6, 7, 8]:
    res = 'Солнце светило ярче чем когда-либо'
  elif number_of_months in [9, 10, 11]:
    res = 'Урожай был невероятным'
  return f"Вы родились в {month[number_of_months]}. {res}"
print(season_events(int(input("Введите номер месяца от 1 до 12 "))))
