def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Деление на ноль"
    except ValueError:
        return "Введите только номер"
print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))