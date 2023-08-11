number = input()
total1 = 0
total2 = 0
for i in range (3):
    total1 += int(number[i])
for i in range (3, (len(number))):
    total2 += int(number[i])
if total1 == total2:
    print('да')
else:
    print('нет')
    
# 183534
# да
# 401367
# нет