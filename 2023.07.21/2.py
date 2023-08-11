number = int(input())
count = 0
total = []
while count < number:
    num = int(input())
    count+=1
    if num > 0:
        total.append(num)
    else:
        continue       
print(sum(total))
 





# 6
# 3
# -5
# 1
# 10
# -1
# 8
# 22