number = int (input ())
# ПЕРЕИМЕНОВАТЬ: цифра числа — digit
figure_1 = number//100
figure_2 = number%100//10
figure_3 = number%10
# ИСПРАВИТЬ: нужно справиться за один вызов print()
print(f'Cумма цифр = {figure_1 + figure_2 + figure_3}')
print (f'Произведение цифр = { figure_1 * figure_2 * figure_3}')


# 333
# Cумма цифр = 9
# Произведение цифр = 27


# ИТОГ: хорошо, но можно лучше — 3/5