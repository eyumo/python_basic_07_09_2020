"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

total_seconds_input = input("Введите количество секунд: ")
user_input_counter = 1
user_input_attempts = 3
while user_input_attempts > user_input_counter:
    if not total_seconds_input.isdigit():
        print("Введено не целое число. Повторите ввод")
        total_seconds_input = input("Введите целое число: ")
        user_input_counter += 1
    else:
        print(f"Вы ввели число {total_seconds_input}")
        break
if not total_seconds_input.isdigit():
    print(f"Вы ввели не целое число. Превышено допустимое количество попыток {user_input_attempts}")
else:
    total_seconds = int(total_seconds_input)
    hours = total_seconds // 3600
    hours_str = str(hours) if hours >= 10 else "0" + str(hours)
    hours_modulo = total_seconds % 3600
    minutes = hours_modulo // 60
    minutes_str = str(minutes) if minutes >= 10 else "0" + str(minutes)
    seconds = hours_modulo % 60
    seconds_str = str(seconds) if seconds >= 10 else "0" + str(seconds)
    print(f"Количество часов, минут и секунд в формате hh:mm:ss {hours_str}:{minutes_str}:{seconds_str}")
