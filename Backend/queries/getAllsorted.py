import sqlite3

def getAllSortedByTurns():
    try:
        connection = sqlite3.connect("StrategiespieleDB.db")
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

def getAllSortedByTurns():
    try:
        connection = sqlite3.connect("StrategiespieleDB.db")
        cursor = connection.cursor()

        selectALLSortedByTurnsQuery = "select TOP 5 from Bauernschach ORDER BY turns ASC"

        cursor.execute(selectALLSortedByTurnsQuery)
        records = cursor.fetchall()
        return records

    except sqlite3.Error as error:
        print("Error occured while inserting data", error)

    finally:
        if sqlite3.Connection:
            connection.close()
            print("connection closed")
