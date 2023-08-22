number = int(input())
total = []
# ИСПРАВИТЬ: когда количество итераций заранее известно, то обычно уместнее использовать цикл for
count = 0
while count < number:
    num = int(input())
    # ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы вокруг бинарных операторов
    count += 1
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

# ДОБАВИТЬ: тесты с другими входными данными


# ИТОГ: хорошо — 2/3
