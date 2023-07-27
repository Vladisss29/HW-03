amount = 0
tickets = int(input("Введите количество билетов:"))
for age in range(tickets):
    age = int(input("Введите Ваш возраст:"))
    if age <= 18:
        amount += 0
    elif age >= 18 and age <= 25:
        amount += 990
    elif age > 25:
        amount += 1390
if amount == 0:
    print("Вход бесплатный")
else:
    print("Количество ваших билетов:", tickets, "шт.")
if tickets > 3:
    discount = amount / 100 * 10
    print("Ваша скидка составляет:", "%.2f" % discount, "руб.")
    print("К оплате со скидкой:", "%.2f" % (amount-discount), "руб.")
if tickets < 4:
    Nodiscount = amount
    print("Скидка составляет:", "%.2f" % Nodiscount, "руб.")
    print("К оплате:", "%.2f" % Nodiscount, "руб.")