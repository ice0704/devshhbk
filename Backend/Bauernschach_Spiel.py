from math import inf
from anytree import Node, RenderTree

import pygame
import sys

import pygame_gui

pygame.init()

# Setzt die Spielfelder
boardArray = [["b", "b", "b", "b", "b", "b"],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         ["w", "w", "w", "w", "w", "w"]]

class Pawn:

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
def searchPawn(y, x):
    # Prüft, ob ein Bauer angeklickt wurde
    for pawn in pawns:
        if pawn.x == x and pawn.y == y:
            return pawn

def getBestMove(x, y, boardArray):
    if y == 4:
        if boardArray[y + 1][x] == " ":
            return[x, y, x, y + 1, 10]
        if x > 0 and boardArray[y + 1][x - 1] == "w":
            return [x, y, x - 1, y + 1, 10]
        if x < 5 and boardArray[y + 1][x - 1] == "w":
            return [x, y, x + 1, y + 1, 10]
    if y >= 2:
        if x < 2 or x > 3:
            if x > 0 and boardArray[y + 1][x - 1] == "w":
                return [x, y, x - 1, y + 1, 5]
            if x < 5 and boardArray[y + 1][x + 1] == "w":
                return [x, y, x + 1, y + 2, 5]
            if boardArray[y + 1][x] == " ":
                return [x, y, x, y + 1, 3]
        if x == 2 or x == 3:
            if boardArray[y + 1][x + 1] == "w":
                return [x, y, x + 1, y + 1, 6]
            if boardArray[y + 1][x - 1] == "w":
                return [x, y, x - 1, y + 1, 6]
            if boardArray[y + 1][x] == " ":
                return [x, y, x, y + 1, 4]
    if y == 0:
        if x < 2 or x > 3:
            if boardArray[y + 2][x] == " ":
                return [x, y, x, y + 2, 3]
            if boardArray[y + 1][x] == " ":
                return [x, y, x, y + 1, 1]
        if x == 2 or x == 3:
            if boardArray[y + 2][x] == " ":
                return [x, y, x, y + 2, 4]
            if boardArray[y + 1][x] == " ":
                return [x, y, x, y + 1, 2]
    if y < 2:
        if x < 2 or x > 3:
            if x > 0 and boardArray[y + 1][x - 1] == "w":
                return [x, y, x - 1, y + 1, 4]
            if x < 5 and boardArray[y + 1][x + 1] == "w":
                return [x, y, x + 1, y + 2, 4]
            if boardArray[y + 1][x] == " ":
                return [x, y, x, y + 1, 1]
        if x == 2 or x == 3:
            if boardArray[y + 1][x + 1] == "w":
                return [x, y, x + 1, y + 1, 5]
            if boardArray[y + 1][x - 1] == "w":
                return [x, y, x - 1, y + 1, 5]
            if boardArray[y + 1][x] == " ":
                return [x, y, x, y + 1, 2]
    return [0, 0, 0, 0, 0]




def chessGame(sizeX, sizeY, screen, userName, difficulty):

    global selected_pawn, beaten_pawn, pawn_to_beat

    clock = pygame.time.Clock()
    UI_REFRESH_RATE = clock.tick(60)/1000

    current_turn = "white"
    run = True
    last_pos = None
    zuege = 0
    gewonnen = False
    pawn_to_beat = None



    manager = pygame_gui.UIManager((sizeX, sizeY))

    screen.fill("black")
    screen.blit(board, ((sizeX/2)-(480/2), (sizeY/2)-(480/2)))
    pygame.display.flip()

    helpButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((sizeX/1.2)-20, sizeY/1.12), (sizeX/6, 50)), text = "BACK",  manager=manager,
                                            object_id='#helpButton')

    # the game
    while run is True:
        if gewonnen is False:
            if current_turn == "white":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if(event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#helpButton'):
                        print("hi")

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Speichert die Position des Mouseklicks in der Variable pos
                        pos = pygame.mouse.get_pos()

                        # Konvertiert die Positionen in Boardkoordinaten
                        x = (pos[0] - (int)((sizeX/2)-(480/2))) // 80
                        y = (pos[1] - (int)((sizeY/2)-(480/2))) // 80


                        # Prüft, ob ein Bauer angeklickt wurde
                        for pawn in pawns:
                            if pawn.x == x and pawn.y == y:
                                selected_pawn = pawn

                                print(pawn)
                                break

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
                                boardArray[selected_pawn.y][selected_pawn.x] = " "
                                boardArray[y][x] = "w"
                                selected_pawn.x = x
                                selected_pawn.y = y
                                current_turn = "black"
                                zuege += 1
                            elif y == selected_pawn.y - 1 and x == selected_pawn.x and beaten_pawn is False:
                                # Ein Spielfeld nach vorne bewegen
                                boardArray[selected_pawn.y][selected_pawn.x] = "w"
                                boardArray[y][x] = " "
                                selected_pawn.x = x
                                selected_pawn.y = y
                                current_turn = "black"
                                zuege += 1
                            elif y == selected_pawn.y - 1 and x == selected_pawn.x - 1 and beaten_pawn is True:
                                boardArray[selected_pawn.y][selected_pawn.x] = " "
                                boardArray[y][x] = "w"
                                selected_pawn.x = x
                                selected_pawn.y = y
                                current_turn = "black"
                                pawns.remove(pawn_to_beat)
                                zuege += 1
                            elif y == selected_pawn.y - 1 and x == selected_pawn.x + 1 and beaten_pawn is True:
                                boardArray[selected_pawn.y][selected_pawn.x] = " "
                                boardArray[y][x] = "w"
                                selected_pawn.x = x
                                selected_pawn.y = y
                                current_turn = "black"
                                pawns.remove(pawn_to_beat)
                                zuege += 1
                        if selected_pawn.color == "white" and selected_pawn.y == 0:
                            gewonnen = True
                            print("Weiß hat gewonnen")

                        reRender(sizeX, sizeY, screen)

                        manager.process_events(event)
                    manager.update(UI_REFRESH_RATE)
            elif current_turn == "black":
                board_copy = boardArray
                best_move = [0, 0, 0, 0, 0]

                x = 0

                while x < 6:
                    y = 0
                    while y < 6:
                        if board_copy[y][x] == "b":
                            current_move = getBestMove(x, y, board_copy)
                            if best_move[4] <= current_move[4]:
                                best_move = current_move
                        y += 1
                    x += 1

                x_move = best_move[0]
                y_move = best_move[1]

                x_destination = best_move[2]
                y_destination = best_move[3]

                print(f"Bester Zug: Von {x_move}, "
                      f"{y_move} nach {x_destination}, {y_destination} mit der Value {best_move[4]}")

                for pawn in pawns:
                    if pawn.x == x_move and pawn.y == y_move:
                        selected_pawn = pawn
                        break

                for pawn in pawns:
                    beaten_pawn = False
                    if pawn.x == x_destination and pawn.y == y_destination and pawn.color != selected_pawn.color:
                        pawn_to_beat = pawn
                        beaten_pawn = True
                        break

                if selected_pawn.color == "black" and selected_pawn.color == current_turn:
                    if y_move == 0 and y_destination == 2 and x_destination == x_move and \
                            beaten_pawn is False:
                        # Möglichkeit beim ersten Spielzug zwei Felder zu bewegen
                        boardArray[selected_pawn.y][selected_pawn.x] = " "
                        boardArray[y_destination][x_destination] = "b"
                        selected_pawn.x = x_destination
                        selected_pawn.y = y_destination
                    elif y_destination == y_move + 1 and x_destination == x_move and beaten_pawn is False:
                        # Ein Spielfeld nach vorne bewegen
                        boardArray[selected_pawn.y][selected_pawn.x] = " "
                        boardArray[y_destination][x_destination] = "b"
                        selected_pawn.x = x_destination
                        selected_pawn.y = y_destination
                    elif y_destination == y_move + 1 and x_destination == x_move - 1 and \
                            beaten_pawn is True:
                        boardArray[selected_pawn.y][selected_pawn.x] = " "
                        boardArray[y_destination][x_destination] = "b"
                        selected_pawn.x = x_destination
                        selected_pawn.y = y_destination
                        pawns.remove(pawn_to_beat)
                    elif y_destination == y_move + 1 and x_destination == x_move + 1 and \
                            beaten_pawn is True:
                        boardArray[selected_pawn.y][selected_pawn.x] = " "
                        boardArray[y_destination][x_destination] = "b"
                        selected_pawn.x = x_destination
                        selected_pawn.y = y_destination
                        pawns.remove(pawn_to_beat)
                if selected_pawn.color == "black" and selected_pawn.y == 5:
                    gewonnen = True
                    print("Schwarz hat gewonnen")

                current_turn = "white"
                print(boardArray)
                reRender(sizeX, sizeY, screen)
