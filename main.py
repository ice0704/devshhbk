import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_SIZE = (400, 300)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the window
pygame.display.set_caption("Login Page")

# Define the font to use
font = pygame.font.SysFont('Arial', 24)

# Set the position and size of the username and password fields
username_rect = pygame.Rect(100, 100, 200, 30)
password_rect = pygame.Rect(100, 150, 200, 30)

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click was in the username or password field
            if username_rect.collidepoint(event.pos):
                print("Clicked username field")
            elif password_rect.collidepoint(event.pos):
                print("Clicked password field")

    # Clear the screen
    screen.fill(WHITE)

    # Draw the login form
    pygame.draw.rect(screen, GRAY, username_rect, 2)
    pygame.draw.rect(screen, GRAY, password_rect, 2)

    # Draw the text labels for the username and password fields
    username_label = font.render("Username:", True, BLACK)
    password_label = font.render("Password:", True, BLACK)
    screen.blit(username_label, (username_rect.x - 80, username_rect.y))
    screen.blit(password_label, (password_rect.x - 80, password_rect.y))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()

