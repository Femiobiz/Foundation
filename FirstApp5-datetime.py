import datetime as dt

today = dt.datetime.today()
r = dt.date.strftime(today, '%y')
print(r)