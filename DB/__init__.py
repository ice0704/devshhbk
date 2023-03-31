import sqlite3

connection = sqlite3.connect("StrategiespieleDB.db")

zeiger = connection.cursor()

def createDatabase():
    try:
        sqlAnweisungUserTabelle = """CREATE TABLE 'User' (
            'User-ID' TEXT NOT NULL UNIQUE,
            'Name' TEXT UNIQUE,
            'Spiele TicTacToe' INTEGER,
            'Gewonnen TicTacToe' INTEGER,
            'Unentschieden TicTacToe' INTEGER,
            'Verloren TicTacToe' INTEGER,
            'Spiele Bauernschach' INTEGER,
            'Gewonnen Bauernschach' INTEGER,
            'Unentschieden Bauernschach' INTEGER,
            'Verloren Bauernschach' INTEGER,
            PRIMARY KEY('User-ID')
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
            'User ID' TEXT NOT NULL UNIQUE,
            'Züge' INTEGER,
            'Schwierigkeitsgrad' INTEGER,
            'Gewonnen' TEXT,
            'Verloren' TEXT,
            PRIMARY KEY('Spiele ID')
            );"""

        zeiger.execute(sqlAnweisungUserTabelle)
        zeiger.execute(sqlAnweisungTicTacToeTabelle)
        zeiger.execute(sqlAnweisungBauernschachTabelle)

    except:
        print("Datenbanken sind bereits vorhanden")

createDatabase()