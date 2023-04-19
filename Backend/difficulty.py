import pygame, sys, pygame_gui
from classes.button import Button
from Bauernschach_Spiel import *

#defining font size and get font element
def font(size): 
    return pygame.font.Font("resources/mainFont.ttf", size)


def difficulty(sizeX,sizeY, screen, userName, gameType):
    pygame.display.set_caption("difficulty")
    backgroundIMG = pygame.image.load("resources/hideinpain.png")
    background = pygame.transform.scale(backgroundIMG,(sizeX, sizeY))
    while True:
        screen.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font(100).render("DIFFICULTY", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(sizeX/2, 60))


        easyButton = Button(image=pygame.image.load("resources/test.png"), pos=(sizeX/2, sizeY/3), 
                            text_input="easy", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")
        mediumButton = Button(image=pygame.image.load("resources/test.png"), pos=(sizeX/2, (sizeY/3)+150), 
                            text_input="medium", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")
        hardButton = Button(image=pygame.image.load("resources/test.png"), pos=(sizeX/2, (sizeY/3) +300), 
                            text_input="hard", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")
        
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [easyButton, mediumButton, hardButton]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if gameType == "chess":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easyButton.checkForInput(MENU_MOUSE_POS):
                        print("chesas")
                        chessGame(sizeX, sizeY, screen, userName, 1)
                    if mediumButton.checkForInput(MENU_MOUSE_POS):
                        chessGame(sizeX, sizeY, screen, userName, 2)
                    if hardButton.checkForInput(MENU_MOUSE_POS):
                        chessGame(sizeX, sizeY, screen, userName,3)
            if gameType == "ttt":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if easyButton.checkForInput(MENU_MOUSE_POS):
                            print("ttt")
                            chessGame(sizeX, sizeY, screen, userName, 1)
                        if mediumButton.checkForInput(MENU_MOUSE_POS):
                            chessGame(sizeX, sizeY, screen, userName, 2)
                        if hardButton.checkForInput(MENU_MOUSE_POS):
                            chessGame(sizeX, sizeY, screen, userName,3)
  

        pygame.display.update()