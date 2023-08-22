num = []
while True:
    numbers = int(input())
    if numbers % 7 == 0:
        num.append(numbers)
    else:
        break
num.reverse()
# ИСПОЛЬЗОВАТЬ везде: PEP 8 не рекомендует добавлять пробелы вокруг = при передаче аргументов по ключу
print(*num, sep=' ')


# 7
# 7
# 14
# 21
# 13
# 21 14 7 7

# ДОБАВИТЬ: тесты с другими входными данными


# ИТОГ: отлично — 3/3
