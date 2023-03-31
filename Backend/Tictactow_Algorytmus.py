
def checkwinloosdraw(board):
    for i in range(6):
        if board[i][0]==board[i][1] ==board[i][2]==board[i][3]==board[i][4]==board[i][5] != " ":

            return board[i][0]
        if board[0][i]==board[1][i] ==board[2][i]==board[3][i]==board[4][i]==board[5][i] != " ":

            return board[0][i]
        if board[0][0]==board[1][1] ==board[2][2]==board[3][3]==board[4][4]==board[5][5] != " ":

            return board[0][0]
        if board[0][5]==board[1][4] ==board[2][3]==board[3][2]==board[4][1]==board[5][0] != " ":

            return board[0][5]


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

