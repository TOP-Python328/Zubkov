number = int(input())
num = int(number / 2 + 1)
total = [number]
for i in range(1, num):
    if number % i == 0:
        total.append(i)
print(sum(total))


# 50
# 93 