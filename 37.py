import datetime

money = 0
count = 0
for month in range(1, 13):
    for year in range(1, 4001):
        count += 1
        intDay = datetime.date(year=year, month=month, day=1).weekday() + 1
        money += intDay


print((money / count) * 1000000)

# ANSWER IS 4001666
