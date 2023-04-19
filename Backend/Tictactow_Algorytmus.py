import random

def checkwinloosdraw(boardcopy):
    for i in range(6):
        for q in range(2):
            if boardcopy[i][0+q] == boardcopy[i][1+q] == boardcopy[i][2+q] == boardcopy [i][3+q] != " ":
                print(boardcopy[i][0 + q])
                return boardcopy[i][0 + q]

            if boardcopy[0+q][i] == boardcopy[1+q][i] == boardcopy[2+q][i] == boardcopy[3+q][i] != " ":
                print(boardcopy[0 + q][i])
                return boardcopy[0 + q][i]

    oliure = (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)
    for pos in oliure:
        if boardcopy[pos[0]][pos[1]] == boardcopy [pos[0]+1] [pos [1]+1] == boardcopy [pos[0]+2] [pos[1]+2] == boardcopy [pos[0]+3] [pos[1]+3] != " ":
            print(boardcopy[pos[0]][pos[1]])
            return boardcopy[pos[0]][pos[1]]

    oreuli = (0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5)
    for pos in oreuli:
        if boardcopy [pos[0]][pos[1]] == boardcopy [pos[0]+1] [pos[1]-1] == boardcopy [pos[0]+2] [pos[1]-2] == boardcopy [pos[0]+3] [pos [1]-3] != " ":
            print(boardcopy[pos[0]][pos[1]])
            return boardcopy[pos[0]][pos[1]]



def Algorithmus(board):
    optimalesfeld = minimax(board,2)
    print(optimalesfeld)
    if optimalesfeld[0] != 0:
        XXX = ((optimalesfeld[0])*100)+50
    else:
        XXX = 50
    if optimalesfeld[1] != 0:
        YYY = ((optimalesfeld[1])*100)+50
    else:
        YYY = 50
    return [XXX,YYY,optimalesfeld]


def minimax(board,tiefe):

    wertung = [[" ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " "]]

    aktuelletiefe = 0
    boardcopy = board
    for i in range(6):
        for u in range(6):
            if boardcopy[i][u] == " ":

                boardcopy[i][u] = "O"

                if  checkwinloosdraw(boardcopy) != None:
                    print(checkwinloosdraw(boardcopy))
                print(boardcopy)
                print(checkwinloosdraw(boardcopy))
                #wenn die KI Gewinnt dann ist die wertung 1
                if checkwinloosdraw(boardcopy) == "O":
                    wertung[i][u] = 1
                #wenn die Spieler Gewinnt ist die Wertung -1
                if checkwinloosdraw(boardcopy) == "X":
                    wertung[i][u] = -1
                # wenn niemand gewonnen hat ist wird erneut der min max ausgeführt wenn die tiefe noch nicht erreicht ist
                if checkwinloosdraw(boardcopy) != "X" and checkwinloosdraw(boardcopy) != "O":
                    if tiefe != aktuelletiefe:

                        wertung[i][u] = 0
                        #wertung[i][u] = minimax(boardcopy,tiefe)
                    #aktuelletiefe = aktuelletiefe + 1

                boardcopy[i][u] = " "
    print(wertung)
    naechsterzug = " "
    for y in range(6):
        for p in range(6):
            if wertung[y][p] == 1:
                naechsterzug=[y,p]

            if naechsterzug == " ":
                naechsterzug = [random.randint(0,5),random.randint(0,5)]

            while board[naechsterzug[0]][naechsterzug[1]] != " ":
                naechsterzug = [random.randint(0, 5), random.randint(0, 5)]



    return naechsterzug

