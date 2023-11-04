import mysql.connector
import csv

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="test",
    database="world"
)

myCursor = myDB.cursor()

myCursor.execute("SHOW TABLES")

tables = myCursor.fetchall() #same as ; its just to run another query 
for db in myCursor:
    print(db)

sqlFormula = "INSERT INTO ncity (ID, Name, CountryCode, Population) VALUES (%s,%s,'NOR',%s);"
csvFilePath = 'cities.csv'

with open(csvFilePath, newline='', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    cityID = 3320
    for row in csv_reader:
        try: 
            data = (cityID, row[0], row[1])
            myCursor.execute(sqlFormula, data)
            cityID += 1
        except mysql.connector.errors.InternalError as sqlerr:
            print(f"Didnt work:{sqlerr}")
        except mysql.connector.errors.IntegrityError as integerityErr:
            print(f"Didnt work:{integerityErr}")

myDB.commit()