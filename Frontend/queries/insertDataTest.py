import sqlite3


def insertChessGameIntoTable(gameId, userId, turns, level, won, lost):
    try:
        connection = sqlite3.connect("../DB/StrategiespieleDB.db") 
        cursor = connection.cursor()
        print("Succesfully Connected")

        insertPlayerQuery = """INSERT INTO Bauernschach
                            ("Spiele ID", "User ID", Züge, Schwierigkeitsgrad, Gewonnen, Verloren)
                            VALUES
                            (?, ?, ?, ?, ?, ?)
                            """
        
        data_tuple = (gameId, userId, turns, level, won, lost)
        cursor.execute(insertPlayerQuery, data_tuple)
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error occured while inserting data", error)

    finally:
        if connection:
            connection.close()
            print("connection closed")

def insertTttGameIntoTable(gameId, userId, turns, level, won, lost):
    try:
        connection = sqlite3.connect("../DB/StrategiespieleDB.db") 
        cursor = connection.cursor()
        print("Succesfully Connected")

        insertPlayerQuery = """INSERT INTO Bauernschach
                            ("Spiele ID", "User ID", Züge, Schwierigkeitsgrad, Gewonnen, Unentschieden, Verloren)
                            VALUES
                            (?, ?, ?, ?, ?, ?, ?)
                            """
        
        data_tuple = (gameId, userId, turns, level, won, lost)
        cursor.execute(insertPlayerQuery, data_tuple)
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error occured while inserting data", error)

    finally:
        if connection:
            connection.close()
            print("connection closed")

   
insertChessGameIntoTable(1 ,"nonPlayer", 20, 1,"JA", "NEIN")
insertChessGameIntoTable(2 ,"OliPlayer", 12, 1,"JA", "NEIN")
insertChessGameIntoTable(3 ,"sergiPlayer", 53, 1,"JA", "NEIN")

insertTttGameIntoTable(1 ,"nonPlayer", 20, 1,"JA","Nein", "NEIN")
insertTttGameIntoTable(1 ,"nonPlayer", 20, 1,"JA","Nein", "NEIN")
insertTttGameIntoTable(1 ,"nonPlayer", 20, 1,"JA","Nein", "NEIN")