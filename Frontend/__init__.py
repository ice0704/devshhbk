import pygame, sys
from classes.button import Button


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

#defining font size and get font element
def font(size): 
    return pygame.font.Font("resources/mainFont.ttf", size)
    
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
    screen.blit(board, ((sizeX/2)-(480/2), (sizeY/2)-(480/2)))
    pygame.display.flip()

# set up the window
sizeX = 520*1.7
sizeY = 520*1.3

size = (sizeX, sizeY)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess Game")
backgroundIMG = pygame.image.load("resources/hideinpain.png")
background = pygame.transform.scale(backgroundIMG,(sizeX, sizeY))


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



def mainMenu():
    pygame.display.set_caption("Menü")
    while True:
        screen.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font(100).render("MAIN MENU", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(sizeX/2, 60))

        playChessButton = Button(image=pygame.image.load("resources/test.png"), pos=(sizeX/4, 250), 
                            text_input="SCHACH", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")
        playToeButton = Button(image=pygame.image.load("resources/test.png"), pos=((sizeX/4)*3, 250), 
                            text_input="TICTACTOE", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")
        showRanking = Button(image=pygame.image.load("resources/test.png"), pos=(sizeX/2, 400), 
                            text_input="RANKING", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")
        quitButton = Button(image=pygame.image.load("resources/test.png"), pos=(sizeX/2, 550), 
                            text_input="VERLASSEN", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [playChessButton, playToeButton, showRanking, quitButton]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playChessButton.checkForInput(MENU_MOUSE_POS):
                    chessGame()
                if playToeButton.checkForInput(MENU_MOUSE_POS):
                    chessGame()
                if showRanking.checkForInput(MENU_MOUSE_POS):
                    showRanking()
                if quitButton.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# ' geholene Datananzeigen'
# def showRanking():
#     pygame.display.set_caption("Ranking")
#     while True:
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

#         screen.fill("white")

#         OPTIONS_TEXT = font(45).render("This is the OPTIONS screen.", True, "Black")
#         OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
#         screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

#         OPTIONS_BACK = Button(image=None, pos=(640, 460), 
#                             text_input="BACK", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")

#         OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
#         OPTIONS_BACK.update(screen)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
#                     mainMenu()

#         pygame.display.update()


    
def chessGame():
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
                
                reRender()


mainMenu()