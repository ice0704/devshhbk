import sqlite3


def insertPlayerIntoTable(id, name, game, turns, botlevel):
    try:
        connection = sqlite3.connect("test.db") 
        cursor = connection.cursor()
        print("Succesfully Connected")

        insertPlayerQuery = """INSERT INTO player
                            (id, name, game, turns, botlevel)
                            VALUES
                            (?, ?, ?, ?, ?)
                            """
        
        data_tuple = (id, name, game, turns, botlevel)
        cursor.execute(insertPlayerQuery, data_tuple)
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error occured while inserting data", error)

    finally:
        if connection:
            connection.close()
            print("connection closed")

   
insertPlayerIntoTable(1, "non", "chess", 20, 2)
insertPlayerIntoTable(2, "kat", "tic", 10, 1)
insertPlayerIntoTable(3, "gut", "chess", 24, 3)