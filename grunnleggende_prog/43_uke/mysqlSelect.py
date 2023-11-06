import mysql.connector
try:
    query = ""
    with mysql.connector.connect(host="127.0.0.1",
                                 port="3306",
                                 user="root",
                                 password="gokstad",
                                 database="world") as conn:

        with conn.cursor() as db_cursor:
            db_cursor.execute(query)

            results = db_cursor()

            for result in results:
                print(results)
except mysql.connector.DatabaseError as dbErr:
    print(f"Database error: {dbErr}")