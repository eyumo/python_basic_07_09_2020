int_var = 3
float_var = 3.1

string_var = "Hello world!"

print(f"integer variable: {int_var}, float variable: {float_var}, string variable: {string_var}")

user_int_var = input("Введите целое число: ")
user_int_var_counter = 1
user_int_var_max_attempts = 3
while user_int_var_max_attempts > user_int_var_counter:
    if not user_int_var.isdigit():
        print("Введено не целое число. Повторите ввод")
        user_int_var = input("Введите целое число: ")
        user_int_var_counter += 1
    else:
        print(f"Вы ввели число {user_int_var}")
        break
if not user_int_var.isdigit():
    print(f"Вы ввели не целое число. Превышено допустимое количество попыток {user_int_var_max_attempts}")
else:
    print(f"Ваше число, умноженное на 5, равно {int(user_int_var) * 5}")
