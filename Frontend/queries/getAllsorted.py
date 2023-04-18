import sqlite3

def getAllSortedByTurns():
    try:
        connection = sqlite3.connect("test.db")
        cursor = connection.cursor()

        selectALLSortedByTurnsQuery = "select * from player ORDER BY turns ASC"

        cursor.execute(selectALLSortedByTurnsQuery)
        records = cursor.fetchall()
        print(records)

    except  sqlite3.Error as error:
        print("Error reading data", error)

    finally:
        if connection:
            connection.close()
            print("connection closed")