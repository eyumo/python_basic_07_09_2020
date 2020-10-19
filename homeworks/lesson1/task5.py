"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

proceeds_input = input("Введите значение выручки: ")
cost_input = input("Введите значение издержки: ")
if not proceeds_input.replace('.', '', 1).isdigit() or not cost_input.replace('.', '', 1).isdigit():
    print("Введенные значения не являются числами")
else:
    proceeds = float(proceeds_input)
    cost = float(cost_input)
    profit = proceeds - cost
    if profit > 0:
        print(f"Фирма отработала с выручкой {profit}")
        profitability = profit/proceeds*100
        print(f"Рентабельность выручки {profitability}%")
        staff_input = input("Введите штат сотрудников:")
        if not staff_input.isdigit():
            print(f"Некорректное значение штата сотрудников: {staff_input}")
        else:
            staff = int(staff_input)
            profit_per_staff = profit/staff
            print(f"Прибыль фирмы в расчете на одного сотрудника: {profit_per_staff}")
    else:
        print(f"Фирма отработала с убытком {profit * -1}")
