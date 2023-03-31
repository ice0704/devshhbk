import pygame
from Tictactow_Algorytmus import Algorithmus
# Initialisiere Pygame
pygame.init()

# Display wird erstellt
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
# Initialisiert die Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setzt die Spielfelder
board = [[" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "]]


def draw_window():
    #Füllt den Bildschirm weiß aus
    screen.fill(WHITE)

    #Malt die Linien ins Spielfeld
    drawBoard()

    #Setzt Marker

    #Updated das Spielfeld
    pygame.display.update()

def drawBoard():
    for line in range(1, 6):
        # Vertikale Linien
        pygame.draw.line(screen, BLACK, (line * WIDTH / 6, 0), (line * WIDTH / 6, HEIGHT), 3)
        # Horizontale Linien
        pygame.draw.line(screen, BLACK, (0, line * HEIGHT / 6), (WIDTH, line * HEIGHT / 6), 3)

def drawcircle(circleX,circleY):
    pygame.draw.circle(screen, (0, 0, 0), (circleX, circleY), 20)
def drawx(xX1,xY1,xX2,xY2):
    pygame.draw.line(screen, (0, 0, 0), xX1, xY1, 10)
    pygame.draw.line(screen, (0, 0, 0), xX2, xY2, 10)

def checkwinloosdraw(board):
    for i in range(6):
        for y in range(3):
            if board[i][y]==board[i][y+1] ==board[i][y+2]==board[i][y+3] != " ":
                print(f"{board[i][2]} hat gewonnen")
                return board[i][2]

            if board[y][i]==board[y+1][i] ==board[y+2][i]==board[y+3][i] != " ":
                print(f"{board[2][i]} hat gewonnen")
                return board[2][i]

            if board[y][y] == board[y+1][y+1] == board[y+2][y+2] == board[y+3][y+3] != " ":
                print(f"{board[3][3]} hat gewonnen")
                return board[3][3]

        if board[y][y-5]==board[y+1][4-y] ==board[y+2][3-y]==board[y+3][2-y]  != " ":
            print(f"{board[0][5]} hat gewonnen")
            return board[0][5]

#boolean wer wer an der rheie ist true ist X und flase ist O
spieler = False
draw_window()
# Game loop
run = True
gamevorbei = False

while run:
    for event in pygame.event.get():
        #Event zum Schließen vom fenster
        if event.type == pygame.QUIT:
            run = False
        #if spieler == True:
        #    XYALGO = Algorithmus(board)
        #    print(XYALGO)
        #    drawcircle(XYALGO[0],XYALGO[1])
        #    spieler = False
        #    pygame.display.update()

        #if spieler == False:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #Prüfen ob der mouse klick sich im feld befindet und ob das board an der stelle noch leer ist dann den spieler rein zeichenen
            ## die horizontalen und vertikalen dinger sind die pixel welche mit den schleifen immer um 100 (einfeld) erhöht werden
            horizontalhunderter = 0
            horizontalfuenfundzwanziger = 25
            horizontalfuenfziger = 50
            horizontalfuenfundsiebziger = 75
            #schleife durch die horizontalen rheien
            for t in range(6):
                diagonalhunderter = 0
                diagonalfuenundzwanziger = 25
                diagonalfuenfziger = 50
                diagonalfuenfundsiebziger = 75
                #diese schleife geht die diagonalen rheien durch
                for i in range(6):
                    if pos[0] >= diagonalhunderter and pos[0] <= diagonalhunderter+100 and pos[1] >= horizontalhunderter and pos[1] <= horizontalhunderter+100 and board[t][i] == " " and gamevorbei == False:
                        if spieler == True:
                            drawcircle(diagonalfuenfziger, horizontalfuenfziger)
                            board[t][i] = "O"
                            spieler = False
                        elif spieler == False:
                            drawx((diagonalfuenundzwanziger, horizontalfuenfundzwanziger), (diagonalfuenfundsiebziger, horizontalfuenfundsiebziger), (diagonalfuenundzwanziger, horizontalfuenfundsiebziger), (diagonalfuenfundsiebziger, horizontalfuenfundzwanziger))
                            board[t][i] = "X"
                            spieler = True
                    diagonalhunderter = diagonalhunderter + 100
                    diagonalfuenfziger = diagonalfuenfziger + 100
                    diagonalfuenundzwanziger = diagonalfuenundzwanziger + 100
                    diagonalfuenfundsiebziger = diagonalfuenfundsiebziger + 100
                horizontalhunderter = horizontalhunderter +100
                horizontalfuenfundzwanziger = horizontalfuenfundzwanziger +100
                horizontalfuenfziger = horizontalfuenfziger +100
                horizontalfuenfundsiebziger = horizontalfuenfundsiebziger+100

                #checken ob jemand gewonnen hat und dann das spiel deaktivieren aber nicht schließen
                if gamevorbei == False:
                    if checkwinloosdraw(board) == "X" or checkwinloosdraw(board) == "O":
                        gamevorbei = True

                pygame.display.update()
# Quit Pygame
pygame.quit()