from datetime import datetime 
from datetime import date
from datetime import timedelta

import pytz

dtime = datetime(2023, 10, 30)

print(dtime)

now = datetime.now(pytz.timezone("Asia/kolkata"))
print(now)
print(now.isoformat())

#for timezone in pytz.all_timezones:
#    print(f"{timezone}: {datetime.now(pytz.timezone(timezone))}")

#for code, name in pytz.country_names.items():
#    print(code, ":", name)

dtTime = datetime(2023,10,30,9,00,00)
print(dtTime.year)
print(dtTime.month)
print(dtTime.day)
print(dtTime.hour)

strDate = dtTime.strftime("%Y-%m-%d %H %M:%S")
print(strDate)

today = datetime.now()

targetDate = today + timedelta(days=30)
print(today, targetDate)

dato_a = datetime(2016, 6, 21, 18, 30, 00)
dato_b = datetime(2021, 11, 2, 9, 44, 22)

dateDiff = dato_b - dato_a
print(dateDiff)

amountDays = dateDiff.days
print(amountDays)