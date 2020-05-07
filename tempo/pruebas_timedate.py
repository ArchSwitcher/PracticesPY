import datetime

now = datetime.datetime.now()

now = now + datetime.timedelta(days=5)

now = now + datetime.timedelta(days=5,minutes=30,hours=4)

now = now - datetime.timedelta(days=15,minutes=30,hours=4)

#now.date()  #return only date whithout hours, minutes, seconds and microseconds

print(now)




