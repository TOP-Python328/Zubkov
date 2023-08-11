proposal = input()
text = proposal.replace(" ", "")
total = len(text)
sum_ = total * 30
rub = int(sum_ // 100)
kopecks = int(sum_ % 100)
print(f'{rub} руб. {kopecks} коп.')

# грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.