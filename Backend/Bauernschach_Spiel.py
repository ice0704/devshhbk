import pygame, sys, uuid, pygame_gui

from math import inf
from anytree import Node, RenderTree
from classes.button import Button
from tkinter import messagebox
from queries.postFinishedGame import postFinishedChessQuery



pygame.init()

class Position:

    gameover = False

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def fillChildren(self):
        return
    def refreshChildren(self):
        return


class Pawn:

    currentTurn = "white"

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.has_moved = False  # Variable, welche angibt, ob der Bauer sich bewegt hat
        self.has_beaten = False  # Variable die angibt, ob geschlagen wurde

    def draw(self, surface, selected=False):
        radius = 30
        if self.color == "white":
            if selected:
                color = (0, 255, 0)  # green if selected
            else:
                color = (255, 255, 255)
        else:
            if selected:
                color = (0, 255, 0)  # green if selected
            else:
                color = (0, 0, 0)
        pygame.draw.circle(surface, color, (self.x * 80 + 40, self.y * 80 + 40), radius)

# render the board and pawns
def reRender(sizeX, sizeY, screen):
    board.fill((255, 206, 158))
    for x in range(0, 6, 2):
        for y in range(0, 6, 2):
            rect1 = pygame.draw.rect(board, (210, 180, 140), (x * 80, y * 80, 80, 80))
            rect2 = pygame.draw.rect(board, (210, 180, 140), ((x + 1) * 80, (y + 1) * 80, 80, 80))

    for pawn in pawns:
        pawn.draw(board, selected=(pawn == selected_pawn))

        # add the board to the screen
    screen.blit(board, ((sizeX/2)-(480/2), (sizeY/2)-(480/2)))
    pygame.display.flip()

#defining font size and get font element
def font(size): 
    return pygame.font.Font("resources/mainFont.ttf", size)

# set up the pawns
pawns = []
for i in range(6):
    pawns.append(Pawn("black", i, 0))
    pawns.append(Pawn("white", i, 5))
selected_pawn = None

# set up the board
squares = []
board = pygame.Surface((480, 480))
board.fill((255, 206, 158))
for x in range(0, 6, 2):
    for y in range(0, 6, 2):
        rect1 = pygame.draw.rect(board, (210, 180, 140), (x * 80, y * 80, 80, 80))
        rect2 = pygame.draw.rect(board, (210, 180, 140), ((x + 1) * 80, (y + 1) * 80, 80, 80))
        squares.append(rect1)
        squares.append(rect2)

print(squares)

for pawn in pawns:
    pawn.draw(board, selected=False)  # pass selected flag
    # add the board to the screen

#Minimax Algorithmus mit Alpha-Beta-Pruning
def minimax(position, depth, alpha, beta, maximizing_player):
    if depth == 0 or position.gameover:
        return position.evaluation

    if maximizing_player is True:
        max_eval = float(-inf)
        for child in position:
            eval = minimax(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float(inf)
        for child in position:
            eval = minimax(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def chessGame(sizeX,sizeY,screen, userName, difficulty):
    global selected_pawn, beaten_pawn, pawn_to_beat, last_pos
    current_turn = "white"
    run = True
    last_pos = None
    unique_ID = f"{uuid.uuid4()}"
    print(type(unique_ID))
  
    screen.fill("black")
    global selected_pawn
    screen.blit(board, ((sizeX/2)-(480/2), (sizeY/2)-(480/2)))
    

    backgroundIMG = pygame.image.load("resources/envi.jpg")
    background = pygame.transform.scale(backgroundIMG,(sizeX, sizeY))

    screen.blit(background, (0, 0))

    reRender(sizeX, sizeY, screen)

    # the game
    while run is True:
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        showHelp = Button(image=pygame.image.load("resources/test.png"), pos=(sizeX-100, sizeY-50), 
                            text_input="Regeln", font=font(30), base_color="#d7fcd4", hovering_color="Yellow")
        
        for button in [showHelp]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
            reRender(sizeX, sizeY, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if showHelp.checkForInput(MENU_MOUSE_POS):
                    
                    messagebox.showinfo("""
                    Es gibt zwei erlaubte Sorten von Zügen :
                    1)	Ziehen
                    kann ein Bauer, indem er ein Feld in Richtung der gegnerischen Grundlinie (das sind die Felder, auf denen anfangs die gegnerischen Bauern stehen) geht, aber nur sofern dieses Feld frei ist (also nicht von einem eigenen oder gegnerischen Bauern besetzt ist). 
                    2)	Schlagen
                    kann ein Bauer in Richtung der gegnerischen Grundlinie durch diagonales Ziehen in Richtung der gegnerischen Grundlinie, aber nur auf ein Feld, auf dem ein gegnerischer Bauer steht. 
                    """, """Bauernschach
                    ist eine simple Variante des Schachs, die nur mit Bauern gespielt wird. In der Ausgansstellung stehen dabei die weißen bzw. schwarzen Spielfiguren (Bauern) auf der jeweiligen Grundlinie. Die Spieler machen abwechselnd einen Zug, wobei Weiß beginnt. 

                    Für den Prototypen soll immer der menschliche Spieler beginnen und die KI entsprechend mit den schwarzen Spielfiguren ziehen. 

                    Es gibt zwei erlaubte Sorten von Zügen :
                    1)	Ziehen
                    kann ein Bauer, indem er ein Feld in Richtung der gegnerischen Grundlinie (das sind die Felder, auf denen anfangs die gegnerischen Bauern stehen) geht, aber nur sofern dieses Feld frei ist (also nicht von einem eigenen oder gegnerischen Bauern besetzt ist). 
                    2)	Schlagen
                    kann ein Bauer in Richtung der gegnerischen Grundlinie durch diagonales Ziehen in Richtung der gegnerischen Grundlinie, aber nur auf ein Feld, auf dem ein gegnerischer Bauer steht. 

                    Ziel des Spieles ist es, einen Bauern auf die generische Grundlinie zu platzieren; wenn das gelingt, ist das Spiel sofort zu Ende und die Farbe, die das erreicht hat, hat gewonnen. Wenn ein Spieler nicht mehr ziehen kann, oder überhaupt keine Figuren mehr hat, ist das Spiel für ihn als verloren zu werten. Ein unentschieden ist daher in dieser Variante nicht möglich.
                    """)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Speichert die Position des Mouseklicks in der Variable pos
                pos = pygame.mouse.get_pos()

                # Konvertiert die Positionen in Boardkoordinaten
                x = (pos[0] - (int)((sizeX/2)-(480/2))) // 80
                y = (pos[1] - (int)((sizeY/2)-(480/2))) // 80

                if selected_pawn is None or (selected_pawn is not None and selected_pawn.color is not current_turn):
                    # Prüft, ob ein Bauer angeklickt wurde
                    for pawn in pawns:
                        if pawn.x == x and pawn.y == y:
                            selected_pawn = pawn

                            print(pawn)
                            break


                    # Prüft, ob ein Bauer angeklickt wurde
                    for pawn in pawns:
                        if pawn.x == x and pawn.y == y:
                            selected_pawn = pawn

                            print(pawn)
                            break
                    last_pos = pos
            elif event.type == pygame.MOUSEBUTTONUP and selected_pawn is not None and selected_pawn.color is \
                    current_turn:
                # Speichert die Position des Mouseklicks
                pos = pygame.mouse.get_pos()

                # Konvertiert die Positionen in Boardkoordinaten
                x = (pos[0] - (int)((sizeX/2)-(480/2))) // 80
                y = (pos[1] - (int)((sizeY/2)-(480/2))) // 80

                for pawn in pawns:
                    beaten_pawn = False
                    if pawn.x == x and pawn.y == y and pawn.color is not selected_pawn.color:
                        pawn_to_beat = pawn
                        beaten_pawn = True
                        break

                # Spielfigur bewegen, wenn der Spielzug gültig ist
                if selected_pawn.color == "white" and selected_pawn.color == current_turn:
                    if selected_pawn.y == 5 and y == 3 and x == selected_pawn.x and beaten_pawn is False:
                        # Möglichkeit beim ersten Spielzug zwei Felder zu bewegen
                        selected_pawn.x = x
                        selected_pawn.y = y
                        current_turn = "black"
                    elif y == selected_pawn.y - 1 and x == selected_pawn.x and beaten_pawn is False:
                        # Ein Spielfeld nach vorne bewegen
                        selected_pawn.x = x
                        selected_pawn.y = y
                        current_turn = "black"
                    elif y == selected_pawn.y - 1 and x == selected_pawn.x - 1 and beaten_pawn is True:
                        selected_pawn.x = x
                        selected_pawn.y = y
                        current_turn = "black"
                        pawns.remove(pawn_to_beat)
                    elif y == selected_pawn.y - 1 and x == selected_pawn.x + 1 and beaten_pawn is True:
                        selected_pawn.x = x
                        selected_pawn.y = y
                        current_turn = "black"
                        pawns.remove(pawn_to_beat)
                elif selected_pawn.color == "black" and selected_pawn.color == current_turn:
                    if selected_pawn.y == 0 and y == 2 and x == selected_pawn.x and beaten_pawn is False:
                        # Möglichkeit beim ersten Spielzug zwei Felder zu bewegen
                        selected_pawn.x = x
                        selected_pawn.y = y
                        current_turn = "white"
                    elif y == selected_pawn.y + 1 and x == selected_pawn.x and beaten_pawn is False:
                        # Ein Spielfeld nach vorne bewegen
                        selected_pawn.x = x
                        selected_pawn.y = y
                        current_turn = "white"
                    elif y == selected_pawn.y + 1 and x == selected_pawn.x - 1 and beaten_pawn is True:
                        selected_pawn.x = x
                        selected_pawn.y = y
                        current_turn = "white"
                        pawns.remove(pawn_to_beat)
                    elif y == selected_pawn.y + 1 and x == selected_pawn.x + 1 and beaten_pawn is True:
                        selected_pawn.x = x
                        selected_pawn.y = y
                        current_turn = "white"
                        pawns.remove(pawn_to_beat)
                if selected_pawn.color == "white" and selected_pawn.y == 0:
                    run = False
                    print("Weiß hat gewonnen")
                    print(f"{unique_ID}, {userName}, turns, {difficulty}, {0}")
                    postFinishedChessQuery(unique_ID, userName, "turns?", 2, False)
                    

                elif selected_pawn.color == "black" and selected_pawn.y == 5:
                    run = False
                    print("Schwarz hat gewonnen")
                    print(f"{unique_ID}, {userName}, turns, {difficulty}, {1}")
                    postFinishedChessQuery(unique_ID, userName, "turns", 2, True)

                reRender(sizeX, sizeY, screen)

