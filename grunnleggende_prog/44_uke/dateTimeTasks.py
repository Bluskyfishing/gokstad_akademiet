from datetime import datetime 
from datetime import date
from datetime import timedelta

#1

nowDate = datetime.now()
print("Date now:",nowDate.strftime("%x"))


nowTimeDate = nowDate.strftime("%Y-%m-%d %M:%S")
print(nowTimeDate)

yesterdayDate = nowDate.year, nowDate.month, nowDate.day -1, nowDate.hour
print(yesterdayDate)