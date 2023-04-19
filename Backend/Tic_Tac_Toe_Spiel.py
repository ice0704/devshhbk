import uuid
import pygame
from Tictactow_Algorytmus import Algorithmus
from queries.postFinishedGame import postFinishedTttQuery
# Initialisiere Pygame
pygame.init()


def ttt(userName, difficulty):
    print(userName)
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
            for q in range(2):
                if board[i][0+q] == board[i][1+q] == board[i][2+q] == board [i][3+q] != " ":
                    print (f" {board[i][0+q]} hat gewonnen")
                    return board[i][0+q]

                if board[0+q][i] == board[1+q][i] == board[2+q][i] == board[3+q][i] != " ":
                    print (f" {board [0+q] [i]} hat gewonnen")
                    return board [0+q] [i]
        oliure = (0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)
        for pos in oliure:
            if board[pos[0]][pos[1]] == board [pos[0]+1] [pos [1]+1] == board [pos[0]+2] [pos[1]+2] == board [pos[0]+3] [pos[1]+3] != " ":
                print(f" {board [pos[0]] [pos [1]]} hat gewonnen")
                return board [pos[0]] [pos [1]]
        oreuli = (0,3),(1,3),(2,3),(0,4),(1,4),(2,4),(0,5),(1,5),(2,5)
        for pos in oreuli:
            if board [pos[0]][pos[1]] == board [pos[0]+1] [pos[1]-1] == board [pos[0]+2] [pos[1]-2] == board [pos[0]+3] [pos [1]-3] != " ":
                print (f" {board [pos[0]] [pos[1]]} hat gewonnen")
                return board [pos[0]] [pos[1]]




    #boolean wer wer an der rheie ist true ist X und flase ist O
    spieler = False
    draw_window()
    # Game loop
    run = True
    gamevorbei = False

    unique_ID = f"{uuid.uuid4()}"

    while run:
        for event in pygame.event.get():
            #Event zum Schließen vom fenster
            if event.type == pygame.QUIT:
                run = False
            if spieler == True:
                XYALGO = Algorithmus(board)


                if board[XYALGO[2][1]][XYALGO[2][0]] == " ":
                    board[XYALGO[2][1]][XYALGO[2][0]] = "O"
                    drawcircle(XYALGO[0],XYALGO[1])
                else:
                    print("----------------")
                    print("FEHLER")
                    print(XYALGO)
                    print("----------------")

                pygame.display.update()
                spieler = False

            if spieler == False:
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
                            if checkwinloosdraw() == "X":
                                gamevorbei == True
                                postFinishedTttQuery(unique_ID, userName, 12, difficulty, 1)
                                run == False
                            elif checkwinloosdraw() == "O":
                                gamevorbei == True
                                postFinishedTttQuery(unique_ID, userName, 11, difficulty, 0)
                                run == False
                            else:
                                gamevorbei == True
                                postFinishedTttQuery(unique_ID, userName, 11, difficulty, 0)
                                run == False
                                    
                        pygame.display.update()
    # Quit Pygame
    pygame.quit()
