from Tic_Tac_Toe_Spiel import *
from Bauernschach_Spiel import *
def startgame(spiel):
    if spiel == "T":
        starttictactoe()
    if spiel == "S":
        startschach()


startgame("T")