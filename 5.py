sales = float(input("Введите выручку"))
cost = float(input("Введите издержки"))
if sales > cost:
    print("выручка фирмы больше издержек")
elif sales == cost:
    print("нет выручки и убытков")
else: print(" издержки фирмы больше выручки")