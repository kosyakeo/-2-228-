import locale
import datetime

try:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
except locale.Error:
    print("Не удалось установить русскую локаль. Результаты могут отображаться не корректно.")

try:
    input_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
except Exception as e:
    print(f"Ошибка ввода: {e}")
else:
    try:
        date_object = datetime.datetime.strptime(input_date, '%d.%m.%Y')
    except ValueError:
        print("Неверный формат даты")
    else:
        try:
            output_date = date_object.strftime('%A, %-d %B, %Y год')
        except ValueError:
            output_date = date_object.strftime('%A, %#d %B, %Y год')
        except Exception as e:
            print(f"Ошибка форматирования даты: {e}")
        else:
            print("Результат: ", output_date.capitalize())
