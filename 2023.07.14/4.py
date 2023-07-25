cell_1 = input()
cell_2 = input()
cell_3 = cell_1[0]
cell_4 = cell_2[0]
number_1 = cell_1[1]
number_2 = cell_2[1]
if (cell_3 == 'a' or cell_3 == 'c' or cell_3 == 'e' or cell_3 == 'g' ):
    figure = 1
if (cell_3 == 'b' or cell_3 == 'd' or cell_3 == 'f' or cell_3 == 'h'):
    figure = 2
if (cell_4 == 'b' or cell_4 == 'd' or  cell_4 == 'f' or cell_4 =='h'  ):
    figure_1 = 2
if (cell_4 == 'a' or cell_4 == 'c' or  cell_4 == 'e' or cell_4 =='g'):
    figure_1 = 1
if ((figure + int(number_1) ) % 2 == (figure_1 + int(number_2)) % 2):
    print('да')
if ((figure + int(number_1) ) % 2 != (figure_1 + int(number_2)) % 2):
    print ('нет')

# a1
# b2
# да


# b1
# g3
# нет