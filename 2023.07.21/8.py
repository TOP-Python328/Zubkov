fib1 = 0
fib2 = 1
n = int(input())
row = []
 
for i in range(n):
    row.append(fib2)
    fib1, fib2 = fib2, fib1 + fib2
print(*row)    




# 1
# 1


# 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597