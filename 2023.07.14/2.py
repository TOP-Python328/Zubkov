number_1 = int (input())
number_2 = int (input())
number_3 = number_1 % number_2
if  (number_3 != 0):
    print (f'{number_1} не делиться на {number_2} нацело', f'неполное  частное: {number_1 // number_2}', f'остаток: {number_3}', sep = '\n' )
elif (number_3 == 0):
    print(f'{number_1} делиться на {number_2} нацело', f'частное: {number_1 / number_2:.0f}', sep = '\n')  





# 8 делиться на 2 нацело
# частное: 4



# 11 не делиться на 5 нацело
# неполное  частное: 2
# остаток: 1
