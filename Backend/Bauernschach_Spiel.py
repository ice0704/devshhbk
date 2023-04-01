import pygame
import sys

pygame.init()

# Setzt die Spielfelder mit Startpositionen
board = [["b", "b", "b", "b", "b", "b"],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         ["w", "w", "w", "w", "w", "w"]]

class Pawn:
    currentTurn = "white"
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.has_moved = False  # added variable to track if pawn has moved
        self.has_beaten = False # Variable die angibt ob geschlagen wurde


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

#    def move(self, x, y, selected=False, currentTurn = currentTurn):
#        # move the piece if the destination is valid
#        if currentTurn == "white":
#            if self.color == "white" and y == self.y - 1:
#                self.x = x
#                self.y = y
#                self.has_moved = True  # update has_moved after move
#                self.has_beaten = False
#                currentTurn = "black"
#            elif self.color == "white" and y == self.y - 1 and (
#                    x == self.x + 1 or x == self.x - 1) and pawn.color == "black":
#                self.x = x
#                self.y = y
#                self.has_moved = True
#                self.has_beaten = True
#                currentTurn = "black"
#        if currentTurn == "black":
#            if self.color == "black" and y == self.y + 1:
#                self.x = x
#                self.y = y
#                self.has_moved = True  # update has_moved after move
#                self.has_beaten = False
#                currentTurn = "white"
#            elif self.color == "black" and y == self.y - 1 and (
#                    x == self.x + 1 or x == self.x - 1) and pawn.color == "white":
#                self.x = x
#                self.y = y
#               self.has_moved = True
#               self.has_beaten = True
#                currentTurn = "black"
#        self.draw(board, selected=selected)  # draw the pawn with the selected flag


# render the board and pawns
def reRender():
    board.fill((255, 206, 158))
    for x in range(0, 6, 2):
        for y in range(0, 6, 2):
            rect1 = pygame.draw.rect(board, (210, 180, 140), (x * 80, y * 80, 80, 80))
            rect2 = pygame.draw.rect(board, (210, 180, 140), ((x + 1) * 80, (y + 1) * 80, 80, 80))

    for pawn in pawns:
        pawn.draw(board, selected=(pawn == selected_pawn))

        # add the board to the screen
    screen.blit(board, (20, 20))
    pygame.display.flip()


# set up the window
size = (520, 520)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess Game")

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
screen.blit(board, (20, 20))
pygame.display.flip()
print(squares)


def chessGame():
    global selected_pawn, beaten_pawn, pawn_to_beat

    current_turn = "white"

    # the game
    while True:
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

                # Prüft, ob ein Bauer angeklickt wurde
                for pawn in pawns:
                    if pawn.x == x and pawn.y == y:
                        selected_pawn = pawn

                        print(pawn)
                        break
            elif event.type == pygame.MOUSEBUTTONUP and selected_pawn is not None and selected_pawn.color is current_turn:
                # Speichert die Position des Mouseklicks
                pos = pygame.mouse.get_pos()

                # Konvertiert die Positionen in Boardkoordinaten
                x = (pos[0] - 20) // 80
                y = (pos[1] - 20) // 80

                for pawn in pawns:
                    if pawn.x == x and pawn.y == y and pawn.color is not selected_pawn.color:
                        pawn_to_beat = pawn
                        beaten_pawn = True
                        break

                # Spielfigur bewegen, wenn der Spielzug gültig ist
                if selected_pawn.color == "white" and selected_pawn.color == current_turn:
                    if selected_pawn.y == 5 and y == 3 and x == selected_pawn.x:
                        # Möglichkeit beim ersten Spielzug zwei Felder zu bewegen
                        selected_pawn.x = x
                        selected_pawn.y = y
                        current_turn = "black"
                    elif y == selected_pawn.y - 1 and x == selected_pawn.x:
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
                    if selected_pawn.y == 0 and y == 2 and x == selected_pawn.x:
                        # Möglichkeit beim ersten Spielzug zwei Felder zu bewegen
                        selected_pawn.x = x
                        selected_pawn.y = y
                        current_turn = "white"
                    elif y == selected_pawn.y + 1 and x == selected_pawn.x:
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
                reRender()


chessGame()