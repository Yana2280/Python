sec =int(input("Введите время в секундах"))
hour = sec// 3600
min = (sec - hour*3600)//60
seconds = (sec-(hour*3600+min*60))
print(f"{hour:02} : {min:02} : {seconds:02}")