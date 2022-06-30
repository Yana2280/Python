num = int(input("Введите целое положительное число"))
max_num = num % 10

while num>0:
    numeral = num % 10
    if numeral > max_num:
        max_num=numeral


    if numeral == 9:
        break
    num//=10
    print(num)

print(max_num)