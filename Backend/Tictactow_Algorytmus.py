
def checkwinloosdraw(board):
    for i in range(6):
        for q in range(2):
            if board[i][0 + q] == board[i][1 + q] == board[i][2 + q] == board[i][3 + q] != " "
                return board[i][0 + q]

            if board[0 + q][i] == board[1 + q][i] == board[2 + q][i] == board[3 + q][i] != " ":
                return board[0 + q][i]

    oliure = (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)
    for pos in oliure:
        if board[pos[0]][pos[1]] == board[pos[0] + 1][pos[1] + 1] == board[pos[0] + 2][pos[1] + 2] == board[pos[0] + 3][pos[1] + 3] != " ":
            return board[pos[0]][pos[1]]

    oreuli = (0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5)
    for pos in oreuli:
        if board[pos[0]][pos[1]] == board[pos[0] + 1][pos[1] - 1] == board[pos[0] + 2][pos[1] - 2] == board[pos[0] + 3][pos[1] - 3] != " ":
            return board[pos[0]][pos[1]]



def Algorithmus(board):
    optimalesfeld = minimax(board,5)
    XXX = ((optimalesfeld[0] -1)*100)+50
    YYY = ((optimalesfeld[1] -1)*100)+50
    return [XXX,YYY]



def minimax(board,tiefe):

    wertung = [[" ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " "]]

    aktuelletiefe = 0
    for i in range(6):
        for u in range(6):
            boardcopy = board
            print(boardcopy)
            if boardcopy[i][u] == " ":

                boardcopy[i][u] = "O"

                #wenn die KI Gewinnt dann ist die wertung 1
                if checkwinloosdraw(boardcopy) == "O":
                    wertung[i][u] = 1
                #wenn die Spieler Gewinnt ist die Wertung -1
                if checkwinloosdraw(boardcopy) == "X":
                    wertung[i][u] = -1
                # wenn niemand gewonnen hat ist wird erneut der min max ausgeführt wenn die tiefe noch nicht erreicht ist
                if checkwinloosdraw(boardcopy) != "X" and checkwinloosdraw(boardcopy) != "O":
                    if tiefe != aktuelletiefe:
                        wertung[i][u] = minimax(boardcopy,tiefe)
                    aktuelletiefe = aktuelletiefe + 1

    return [0,0]

