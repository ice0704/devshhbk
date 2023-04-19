import sqlite3

def createUserQuery(userName):
    try:
        connection = sqlite3.connect("StrategiespieleDB.db") 
        cursor = connection.cursor()

        print("Succesfully Connected")

        cursor.execute('SELECT Username FROM User WHERE Username = ?', (userName,))

        result = cursor.fetchone()

        if result is None:

            cursor.execute("INSERT INTO User VALUES(?)", (userName,))
            connection.commit()
        else:
            raise ValueError("User already exists")
    except sqlite3.Error as error:
        print("Error occured while inserting data", error)

    finally:
        if connection:
            connection.close()
            print("connection closed")

def checkingExistingUser(userName):
    try:
        connection = sqlite3.connect("StrategiespieleDB.db") 
        cursor = connection.cursor()

        print("Succesfully Connected")

        cursor.execute('SELECT Username FROM User WHERE Username = ?', (userName,))

        result = cursor.fetchone()

        if result:
            print("login succesfully")
        else:
            raise ValueError("User dont exists")
    except sqlite3.Error as error:
        print("Error occured while inserting data", error)

    finally:
        if connection:
            connection.close()
            print("connection closed")