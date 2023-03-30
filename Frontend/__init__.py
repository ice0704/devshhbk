import pygame

# initialize Pygame
pygame.init()

# set the window size
defineWidth = 800
defineHeight = 800
WINDOW_SIZE = (defineWidth, defineHeight)
squares=[]
SQUARE_SIZE = defineWidth/6

class Pawn:
    def __init__(self, color):
        self.color = color
        self.radius = int(SQUARE_SIZE/3)
        if self.color == "white":
            self.color_code = (255, 255, 255)
        else:
            self.color_code = (0, 0, 0)
        self.position = None

    def draw(self, screen, position):
        self.position = pygame.Rect(position[0], position[1], SQUARE_SIZE, SQUARE_SIZE)
        x, y = position
        pygame.draw.circle(screen, self.color_code, (x + int(SQUARE_SIZE/2), y + int(SQUARE_SIZE/2)), int(self.radius))

def chessGame(window_size):
    screen = pygame.display.set_mode(window_size)
    # set the title of the window
    pygame.display.set_caption("Chess Board")

    # set the colors of the board
    BLACK = (165, 42,42)
    WHITE = (181, 101, 29)


    # draw the board 
    for row in range(6, 0, -1):
        for col in range(6):
            # calculate the position of the square
            x = col * SQUARE_SIZE
            y = (6 - row) * SQUARE_SIZE
            # set the color of the square
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            # draw the square
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            # store the square's position 
            square = {"rect": pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)}
            squares.append(square)

    # create the pawns
    white_pawns = [Pawn("white") for i in range(6)]
    black_pawns = [Pawn("black") for i in range(6)]

    # draw the pawns on the board
    for i in range(6):
        white_pawns[i].draw(screen, (i*SQUARE_SIZE, 0))
        black_pawns[i].draw(screen, (i*SQUARE_SIZE, 5*SQUARE_SIZE))

    # update the Pygame window
    pygame.display.update()

    # wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for pawn in black_pawns:
                    if pawn.position.collidepoint(mouse_pos):
                        # change the color of the clicked pawn to green
                        pawn.color = "green"
                        pawn.color_code = (0, 255, 0)
                        pawn.draw(screen, pawn.position.topleft)
                # update the Pygame window
                pygame.display.update()
            

chessGame(WINDOW_SIZE)





