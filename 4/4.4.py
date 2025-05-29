import locale
import datetime

try:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
except locale.Error:
    pass

input_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")

try:
    date_object = datetime.datetime.strptime(input_date, '%d.%m.%Y')
    output_date = date_object.strftime('%A, %-d %B, %Y год')
    print("Результат: ", output_date.capitalize())
except ValueError:
    print("Неверный формат даты")
