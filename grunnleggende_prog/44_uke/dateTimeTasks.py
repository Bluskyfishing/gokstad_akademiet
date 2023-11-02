from datetime import datetime 
from datetime import timedelta
from pytz import timezone
import pytz

global nowDate
nowDate = datetime.today()

#1
def todayDate(): 
    print("Date now:",nowDate.strftime("%x"))

def timeDate():
    nowTimeDate = nowDate.strftime("%Y-%m-%d %M:%S")
    print("Date and Time now:", nowTimeDate)

def yesterday():
    yesterdayDate = nowDate - timedelta(days = 1)
    yesterdayDateFormated = yesterdayDate.strftime("%Y-%m-%d %M:%S")
    print("Yesterdays date:", yesterdayDateFormated)


#2
def add5Days():
    addDays = nowDate + timedelta(days = 5)
    addDaysFormated = addDays.strftime("%x")
    nowDateFormated = nowDate.strftime("%x")
    print(nowDateFormated, "+5 days=", addDaysFormated)
    
def subtract10days():
    subtractdays = nowDate - timedelta(days = 10)
    addDaysFormated = subtractdays.strftime("%x")
    nowDateFormated = nowDate.strftime("%x")
    print(nowDateFormated,"-10 days=", addDaysFormated)

def add2Weeks():
    addWeeks = nowDate + timedelta(weeks = 2)
    addWeeksFormated = addWeeks.strftime("%x")
    nowDateFormated = nowDate.strftime("%x")
    print(nowDateFormated,"+2 weeks=", addWeeksFormated)


#3
def add30Min():
    addMinute = nowDate + timedelta(minutes = 30)
    addMinuteFormated = addMinute.strftime("%H:%M")
    nowDateFormated = nowDate.strftime("%H:%M")
    print(nowDateFormated,"+30 min =",addMinuteFormated)

def subtract15Min():
    subtractMinute = nowDate - timedelta(minutes = 15)
    subtractMinuteFormated = subtractMinute.strftime("%H:%M")
    nowDateFormated = nowDate.strftime("%H:%M")
    print(nowDateFormated,"-15 min =",subtractMinuteFormated)


#4
def convertStringToDate():
    mystring = "2023-10-05"
    dateFormat = "%Y-%m-%d"
    dataObject = datetime.strptime(mystring, dateFormat)
    dateOnly = dataObject.date()
    print(dateOnly)

def convertDateToString():
    dateObject = nowDate.date()
    myString = dateObject.strftime("%d-%m-%Y")
    print(myString)


#5
def differenceInDays():
    dateA = nowDate
    dateB = datetime(2023, 10, 1)
    difference = dateA - dateB
    result = difference.days
    print("The difference is:",result,"Days")

def midnightDifference():
    midnight = datetime(nowDate.year, nowDate.month, nowDate.day)
    timeDifference = nowDate - midnight
    seconds = timeDifference.total_seconds()
    print("Amount of seconds till midnight:", seconds)


#6
def findNameOfDay():
    nameOfDay = nowDate.strftime("%A")
    print(f"Today is {nameOfDay}!")

def findIfWeekend():
    date = datetime(2023, 10, 1)
    if date.strftime("%A") == "Saturday" or date.strftime("%A") == "Sunday":
        print("It's the weekend!", date.strftime("%A"))
    else:
        print("It's no the weekend :(", date.strftime("%A"))


#7
def nextNewYearsEve():
    newYearsEve = datetime(nowDate.year + 1, 1, 1)
    difference = newYearsEve - nowDate
    daysLeft = difference.days
    print(daysLeft, "Days left till New Years!")

def importantDays():
    dateA = datetime(2023, 12, 24)
    if dateA.strftime("%m-%d") == "12-24":
        print("Its Christmas!")
    else:
        print("Nothing important today!")

#8
def timeZoneConversion():
   utcNow = datetime.utcnow()
   japanTime = utcNow.astimezone(pytz.timezone("Japan"))
   print(f"Local time: {utcNow}\nTime in Japan: {japanTime}")


def timeConversion():
    utcNow = datetime.utcnow()
    japanTime = utcNow.astimezone(pytz.timezone("Japan"))
    jpOffset = japanTime.utcoffset()
    difference = utcNow + jpOffset

    print("Japan Offset:", jpOffset)
    print("UTC Now:", utcNow,"\nUTC Now with Japan Offset:", difference)


#9
def birthdayAge():
    birthday = str(input("Birthday(dd-mm-yyyy): "))
    dateFormat = "%d-%m-%Y"
    dateObject = datetime.strptime(birthday, dateFormat)

    difference = nowDate - dateObject
    age = difference.days / 360
    return age

def findAge():
    if birthdayAge() >= 18:
        print("You're old enough to drive!")
    else:
        print("You're not old enough to drive :(")

#10
def countdownDate():
    targetDate = str(input("Date(dd-mm-yyyy): "))
    dateFormat = "%d-%m-%Y"
    dateObject = datetime.strptime(targetDate, dateFormat)

    difference = dateObject - nowDate 
    differenceInSeconds = difference.total_seconds()
    print(f"{differenceInSeconds} seconds till {targetDate}")

def earliestDate():
    dateA = str(input("Date(dd-mm-yyyy): "))
    dateB = str(input("Date(dd-mm-yyyy): "))
    dateFormat = "%d-%m-%Y"
    dateObjectA = datetime.strptime(dateA, dateFormat)
    dateObjectB = datetime.strptime(dateB, dateFormat)

    difference = dateObjectA - dateObjectB
    if difference.days < 0:
        print(f"{dateA} is before {dateB}.")
    if difference.days > 0:
        print(f"{dateB} is before {dateA}.")