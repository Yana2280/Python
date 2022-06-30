while True:
    day = 1
    start_km = float(input("Начальный результат -"))
    finish_km = float(input("Конечный результат -"))

    while start_km<finish_km:
        start_km *= 1.1
        day += 1
    print(f"Спортсмен добьется результата за {day} дней")