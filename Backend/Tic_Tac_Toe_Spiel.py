import pygame

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

def checkwinloosdraw():
    for i in range(6):
        if board[i][0]==board[i][1] ==board[i][2]==board[i][3]==board[i][4]==board[i][5] != " ":
            print(f"{board[i][0]} hat gewonnen")
            return True
        if board[0][i]==board[1][i] ==board[2][i]==board[3][i]==board[4][i]==board[5][i] != " ":
            print(f"{board[0][i]} hat gewonnen")
            return True
        if board[0][0]==board[1][1] ==board[2][2]==board[3][3]==board[4][4]==board[5][5] != " ":
            print(f"{board[0][0]} hat gewonnen")
            return True
        if board[0][5]==board[1][4] ==board[2][3]==board[3][2]==board[4][1]==board[5][0] != " ":
            print(f"{board[0][5]} hat gewonnen")
            return True

#boolean wer wer an der rheie ist true ist X und flase ist O
spieler = False
draw_window()
# Game loop
run = True

while run:
    for event in pygame.event.get():
        #Event zum Schließen vom fenster
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #Prüfen ob der mouse klick sich im feld befindet und ob das board an der stelle noch leer ist dann den spieler rein zeichenen
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
                    if pos[0] >= diagonalhunderter and pos[0] <= diagonalhunderter+100 and pos[1] >= horizontalhunderter and pos[1] <= horizontalhunderter+100 and board[t][i] == " ":
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
            if checkwinloosdraw() == True:
                run = False
            pygame.display.update()
# Quit Pygame
pygame.quit()