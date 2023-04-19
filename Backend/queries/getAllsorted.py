import sqlite3

def getAllSortedByTurns():
    try:
        connection = sqlite3.connect("../DB/StrategiespieleDB.db")
        cursor = connection.cursor()

        selectALLSortedByTurnsQuery = "select * from Bauernschach ORDER BY turns ASC"

        cursor.execute(selectALLSortedByTurnsQuery)
        records = cursor.fetchall()
        return records

    except  sqlite3.Error as error:
        print("Error reading data", error)

    finally:
        if connection:
            connection.close()
            print("connection closed")
