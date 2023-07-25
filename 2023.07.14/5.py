cell_1 = input()
cell_2 = input()
cell_3 = ord(cell_1[0])
cell_4 = ord (cell_2[0])
number = int (cell_1[1]) + 96
number_1 = int (cell_2[1])+96
if (cell_3 > 104 or cell_4 > 104 or number > 104 or number_1 > 104): 
    print ('не корректно')
elif (abs(cell_3 - cell_4) >= 1 and abs(number - number_1) >=1):
    print ('нет')
else:
    print('да')


# d4
# e4
# да

# a2
# c4
# нет