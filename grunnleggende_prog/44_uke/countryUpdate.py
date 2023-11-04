import mysql.connector
import csv
from deep_translator import GoogleTranslator

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

sqlFormulaUpdate = "UPDATE ncountry SET Population = %s WHERE Name = %s"
csvFilePath = 'countries.csv'

with open(csvFilePath, newline='', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:

        intCheck = ''.join([i for i in row[0] if not i.isdigit()])
        translated = GoogleTranslator(source="no", target="en").translate(intCheck)
        row[0] = translated
        row[1] = row[1].strip()

        countryName = row[0]
        counrtyPopulation = row[1]

        try: 
            data = (counrtyPopulation, countryName)
            myCursor.execute(sqlFormulaUpdate, data)
        except mysql.connector.errors.InternalError as sqlerr:
            print(f"Didnt work:{sqlerr}")
        except mysql.connector.errors.IntegrityError as integerityErr:
            print(f"Didnt work:{integerityErr}")

myDB.commit()