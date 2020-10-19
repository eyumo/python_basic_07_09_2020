"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
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
    n = int(user_input)
    nn = int(user_input + user_input)
    nnn = int(user_input + user_input + user_input)
    result = n + nn + nnn
    print(f"{n} + {nn} + {nnn} = {result}")