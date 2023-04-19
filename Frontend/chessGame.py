import pygame, sys

pygame.init()

class Pawn:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.has_moved = False  # added variable to track if pawn has moved

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

    def move(self, x, y, selected=False):
        # move the piece if the destination is valid
        if self.color == "white" and y == self.y - 1:
            self.x = x
            self.y = y
            self.has_moved = True  # update has_moved after move
        elif self.color == "black" and y == self.y + 1:
            self.x = x
            self.y = y
            self.has_moved = True  # update has_moved after move
        self.draw(board, selected=selected)  # draw the pawn with the selected flag


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

for pawn in pawns:
    pawn.draw(board, selected=False)  
    # add the board to the screen

def chessGame(sizeX,sizeY,screen):
    screen.fill("black")
    global selected_pawn
    screen.blit(board, ((sizeX/2)-(480/2), (sizeY/2)-(480/2)))
    pygame.display.flip()

    # the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # get the position of the click
                pos = pygame.mouse.get_pos()
                print(pos)
                # convert the position to board coordinates
                x = (pos[0] - (int)((sizeX/2)-(480/2))) // 80
                y = (pos[1] - (int)((sizeY/2)-(480/2))) // 80
                print(x,y)
                # check if a piece has been clicked
                for pawn in pawns:
                    if pawn.x == x and pawn.y == y:
                        selected_pawn = pawn

                        print(pawn)
                        break

            elif event.type == pygame.MOUSEBUTTONUP and selected_pawn is not None:
                # get the position of the click
                pos = pygame.mouse.get_pos()

                # convert the position to board coordinates
                x = (pos[0] - (int)((sizeX/2)-(480/2))) // 80
                y = (pos[1] - (int)((sizeY/2)-(480/2))) // 80

                # move the piece if the destination is valid
                if selected_pawn.color == "white":
                    if selected_pawn.y == 5 and y == 3 and x == selected_pawn.x:
                        # move 2 squares if pawn has never moved before
                        selected_pawn.x = x
                        selected_pawn.y = y
                    elif y == selected_pawn.y - 1 and x == selected_pawn.x:
                        # move 1 square
                        selected_pawn.x = x
                        selected_pawn.y = y

                elif selected_pawn.color == "black":
                    if selected_pawn.y == 0 and y == 2 and x == selected_pawn.x:
                        # move 2 squares if pawn has never moved before
                        selected_pawn.x = x
                        selected_pawn.y = y
                    elif y == selected_pawn.y + 1 and x == selected_pawn.x:
                        # move 1 square
                        selected_pawn.x = x
                        selected_pawn.y = y
                
                reRender(sizeX, sizeY, screen)