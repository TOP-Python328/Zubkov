proposal = input()
text = proposal.replace(" ", "")
# УДАЛИТЬ: эта переменная используется только единожды — в её создании нет необходимости
total = len(text)
sum_ = total * 30
# УДАЛИТЬ: эти переменные используются только единожды — в их создании нет необходимости
# ИСПРАВИТЬ: операторы // и % возвращают int объекты при условии, что оба операнда являются int объектами — явный вызов функций int() избыточен
rub = int(sum_ // 100)
kopecks = int(sum_ % 100)
print(f'{rub} руб. {kopecks} коп.')


# грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.

# ДОБАВИТЬ: тесты с другими входными данными


# ИТОГ: хорошо, но можно лучше — 2/3
