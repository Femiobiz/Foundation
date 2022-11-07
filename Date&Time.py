# import datetime as dt
# from datetime import date
# from datetime import time

# present = dt.datetime.today()
# present = dt.date.today()
# print(present)

####### for date##########
# import datetime as dt

# today = dt.date.today()
# result = dt.date.strftime(today, '%d %b %Y ')
# print(result)

## or

# day = dt.date.strftime(today, '%d')
# month = dt.date.strftime(today, '%b')
# year = dt.date.strftime(today, '%Y')
# fulldate = (f'{day} /{month}/{year}')
# print(fulldate)

########## for time #############
import datetime as dt

today = dt.datetime.now()
result = dt.date.strftime(today, '%H-%M-%S %p')
print(result)