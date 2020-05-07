import datetime

central_time = datetime.timezone(datetime.timedelta(hours =- 6))
print(central_time)

pasific_time = datetime.timezone(datetime.timedelta(hours =- 8))
print(pasific_time)

ester_time = datetime.timezone(datetime.timedelta(hours =- 5))
print(ester_time)


now = datetime.datetime.now(central_time)
print(now)

now = now.astimezone(pasific_time)
print(now)
