def my_sum ():
    sum= 0
    leave = False
    while leave == False:
        number = input('Введите числа или Q для выхода: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                leave = True
                break
            else:
                res = res + int(number[el])
        sum = sum + res
        print(f'Текущая сумма: {sum}')
    print(f'Конечная сумма: {sum}')


my_sum()