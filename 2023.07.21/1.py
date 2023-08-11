num = []
while True:
    numbers = int(input())
    if numbers % 7 == 0:
        num.append(numbers)
    else:
        break
num.reverse()
print (*num, sep = ' ')

# 7
# 7
# 14
# 21
# 13
# 21 14 7 7