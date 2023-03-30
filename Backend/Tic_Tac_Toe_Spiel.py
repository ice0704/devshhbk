import pygame

# Initialisiere Pygame
pygame.init()

# Display wird erstellt
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

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
    for i in range(1, 6):
        # Vertical lines
        pygame.draw.line(screen, BLACK, (i * WIDTH / 6, 0), (i * WIDTH / 6, HEIGHT), 3)
        # Horizontal lines
        pygame.draw.line(screen, BLACK, (0, i * HEIGHT / 6), (WIDTH, i * HEIGHT / 6), 3)



# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_window()

# Quit Pygame
pygame.quit()