money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
life = (money_capital) + (salary) - (spend)
while  True:
    spend = (spend) * (1 + increase)
    life = (life) + (salary) - (spend)
    if life > 0:
        month += 1
    else:
        break

month = month + 1 #тк прожили месяц, до того месяц, в котором нам не хватит денег

# TODO Оформить решение

print(month)
