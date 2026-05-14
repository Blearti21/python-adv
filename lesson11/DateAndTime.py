import datetime
from email.utils import formatdate

currentDate = datetime.datetime.now()

print("year",currentDate.year)
print("month",currentDate.month)
print("day",currentDate.day)
print("minute",currentDate.minute)
print("second",currentDate.second)

print("----------------------")


currentDate2 = datetime.datetime.now(). date()

print("year:",currentDate2.year)
print("month:",currentDate2.month)
print("day:",currentDate2.day)


timeObject = datetime.time(12,30,45,)

print("ora:", timeObject.hour)
print("minute:", timeObject.minute)
print("second:", timeObject.second)


specific_datetime = datetime.datetime(2024,1,1,25)

formatdate= specific_datetime.strftime('%d-%m-%Y')

print(formatdate)

utc_time = datetime.datetime.now(datetime.timezone.utc)

print("curreent time:", utc_time)

custom = datetime.timedelta(hours=3)


