sales = float(input("Введите выручку"))
cost = float(input("Введите издержки"))

if sales > cost:
    print(f"Выручка фирмы больше издержек.Рентабельность выручки - {sales/cost}")
    stuff = int(input("Введите количество сотрудников"))
    print(f"Прибыль на сотрудника - {sales/stuff}")
elif sales == cost:
    print("нет выручки и убытков")
else: print(" издержки фирмы больше выручки")