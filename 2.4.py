string = input("Введите набор слов через пробел")
word = []
num = 1
for el in range(string.count(' ') + 1):
    word = string.split()
    if len(str(word)) <= 10:
        print(f" {num} {word [el]}")
        num += 1
    else:
        print(f" {num} {word [el] [0:10]}")
        num += 1