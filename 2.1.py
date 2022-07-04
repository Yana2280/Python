my_list = [34, 3.4, False, None,(2,3)]
for i, item in enumerate(my_list, 1):
    print(f'{i}. {item} - {type(item)}')