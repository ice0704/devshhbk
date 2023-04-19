from math import inf
from anytree import Node, RenderTree

import pygame
import sys

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

    screen.fill("black")
    global selected_pawn
    screen.blit(board, ((sizeX/2)-(480/2), (sizeY/2)-(480/2)))
    pygame.display.flip()

    # the game
    while run is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Speichert die Position des Mouseklicks in der Variable pos
                pos = pygame.mouse.get_pos()

                # Konvertiert die Positionen in Boardkoordinaten
                x = (pos[0] - 20) // 80
                y = (pos[1] - 20) // 80

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
                x = (pos[0] - 20) // 80
                y = (pos[1] - 20) // 80

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
                elif selected_pawn.color == "black" and selected_pawn.y == 5:
                    run = False
                    print("Schwarz hat gewonnen")
                reRender(sizeX, sizeY, screen)
