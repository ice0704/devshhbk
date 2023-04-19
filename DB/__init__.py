import sqlite3

connection = sqlite3.connect("StrategiespieleDB.db")

zeiger = connection.cursor()

def createDatabase():
    try:
        sqlAnweisungUserTabelle = """CREATE TABLE 'User' (
            'Username'  VARCHAR(30) NOT NULL UNIQUE,
            PRIMARY KEY('Username')
            );"""

        sqlAnweisungTicTacToeTabelle = """
            CREATE TABLE 'Tic Tac Toe' (
            'Spiele ID' INTEGER NOT NULL UNIQUE,
            'User ID' TEXT NO NULL UNIQUE,
            'Züge' INTEGER,
            'Schwierigkeitsgrad' INTEGER,
            'Gewonnen' TEXT,
            'Unentschieden' TEXT,
            'Verloren' TEXT,
            PRIMARY KEY('Spiele ID')
            );"""

        
        sqlAnweisungBauernschachTabelle = """
            CREATE TABLE 'Bauernschach' (
            'Spiele ID' INTEGER NOT NULL UNIQUE,
            'Username' VARCHAR(30),
            'Züge' INTEGER,
            'Schwierigkeitsgrad' INTEGER,
            'Ergebnis' BOOLEAN NOT NULL, 
            PRIMARY KEY('Spiele ID'),
            FOREIGN KEY(Username) REFERENCES User(Username)
            );"""
        zeiger.execute(sqlAnweisungUserTabelle)
        zeiger.execute(sqlAnweisungTicTacToeTabelle)
        zeiger.execute(sqlAnweisungBauernschachTabelle)

    except:
        print("Datenbanken sind bereits vorhanden")

createDatabase()