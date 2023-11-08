import mysql.connector

def selectEverything():
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="test",
        database="world"
    )

    cursor = myDB.cursor()

    countries = []

    cursor.execute("SELECT * FROM ncountry")

    attributeNames = [i[0] for i in cursor.description]
    countries.append(tuple(attributeNames))

    columns = cursor.fetchall()

    cursor.execute("SELECT * FROM ncountry")
    for x in cursor:
        countries.append(x)
    return countries