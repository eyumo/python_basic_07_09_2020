"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

user_input = input("Введите целое число: ")
user_input_counter = 1
user_input_attempts = 3
while user_input_attempts > user_input_counter:
    if not user_input.isdigit():
        print("Введено не целое число. Повторите ввод")
        user_input = input("Введите целое число: ")
        user_input_counter += 1
    else:
        print(f"Вы ввели число {user_input}")
        break
if not user_input.isdigit():
    print(f"Вы ввели не целое число. Превышено допустимое количество попыток {user_input_attempts}")
else:
    user_number = int(user_input)
    max_number = 0
    while user_number:
        last_digit_in_number = user_number % 10
        if last_digit_in_number > max_number:
            max_number = last_digit_in_number
        user_number = user_number // 10
    else:
        print(f"Максимальная цифра в числе {max_number}")
