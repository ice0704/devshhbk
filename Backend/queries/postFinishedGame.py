import sqlite3

def postFinishedGameQuery(gameId, userName, turns, difficulty, result):
    try:    
        connection = sqlite3.connect("../DB/StrategiespieleDB.db") 
        cursor = connection.cursor()
        print("Succesfully Connected")

        insertFinischedGame = """INSERT INTO Bauernschach
                            ("Spiele ID", "Username", Züge, Schwierigkeitsgrad, Ergebnis)
                            VALUES
                            (?, ?, ?, ?, ?)
                            """
        
        data_tuple = (gameId, userName, turns, difficulty, result)
        cursor.execute(insertFinischedGame, data_tuple)
        connection.commit()
        cursor.close()
    
    except sqlite3.Error as error:
        print("Error occured while inserting data", error)

    finally:
        if connection:
            connection.close()
            print("connection closed")