def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Vidinskaya', name='Yana', year='2002', city='Minsk', email='example@mail.com',
              telephone='8-800-555-35-35'))