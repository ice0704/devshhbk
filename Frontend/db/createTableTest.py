import sqlite3

try:
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    print("Succesfully Connected")

    createPlayerQuery = '''CREATE TABLE player(
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL UNIQUE,
                        game TEXT,
                        turns INTEGER,
                        BOTLEVEL INTEGER
                        );'''
    
    cursor.execute(createPlayerQuery)
    connection.commit()
    print("table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error occured while creating database", error)

finally:
    if connection:
        connection.close()
        print("connection closed")

   
