def my_func(first, second, third):
    if first >= third and second >= third:
        return first + second
    elif first > second and first < third:
        return first + third
    else:
        return second + third

print(f'Result - {my_func(int(input("enter first argument: ")), int(input("enter second argument: ")), int(input("enter third argument: ")))}')