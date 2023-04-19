import pygame, sys, pygame_gui
from classes.button import Button
from Bauernschach_Spiel import *
from difficulty import *
from queries.getAllsorted import getAllSortedByTurns
from queries.createUser import *



pygame.init()

#defining font size and get font element
def font(size): 
    return pygame.font.Font("resources/mainFont.ttf", size)
    
# set up the window
sizeX = 520*1.7
sizeY = 520*1.3

size = (sizeX, sizeY)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess Game")
backgroundIMG = pygame.image.load("resources/hideinpain.png")
background = pygame.transform.scale(backgroundIMG,(sizeX, sizeY))

backgroundIMGTwo = pygame.image.load("resources/wojak.jpg")
backgroundTwo = pygame.transform.scale(backgroundIMGTwo,(sizeX, sizeY))

manager = pygame_gui.UIManager((sizeX, sizeY))



def mainMenu(sizeX,sizeY, screen, userName):
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
                    difficulty(sizeX, sizeY, screen, userName, "chess")
                if playToeButton.checkForInput(MENU_MOUSE_POS):
                    difficulty(sizeX, sizeY, screen, userName, "ttt")
                if showRanking.checkForInput(MENU_MOUSE_POS):
                    showRankingF()
                if quitButton.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def showRankingF():
    pygame.display.set_caption("Ranking")
    testest = getAllSortedByTurns()
    for row in testest:
        print("name", row[1], row[3])

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    mainMenu()

        pygame.display.update()

def startPage(sizeX, sizeY, screen):
    pygame.display.set_caption("Welcome")
    clock = pygame.time.Clock()
    while True:
        screen.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font(100).render("Welcome", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(sizeX/2, 60))

        registerButton = Button(image=pygame.image.load("resources/test.png"), pos=(sizeX/4, sizeY/2), 
                            text_input="Registieren", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")
        loginButton = Button(image=pygame.image.load("resources/test.png"), pos=((sizeX/4)*3, sizeY/2), 
                            text_input="Login", font=font(40), base_color="#d7fcd4", hovering_color="Yellow")
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [registerButton, loginButton]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if registerButton.checkForInput(MENU_MOUSE_POS):
                    register(sizeX, sizeY, screen)
                if loginButton.checkForInput(MENU_MOUSE_POS):
                    login(sizeX, sizeY, screen)
        pygame.display.update()

def register(sizeX, sizeY, screen):
    pygame.display.set_caption("REGISTIEREN")
    clock = pygame.time.Clock()

    #u wanna know then go read the doc https://pygame-gui.readthedocs.io/en/latest/pygame_gui.elements.html?highlight=pygame_gui.elements.UIButton#pygame_gui.elements.UIButton
    text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((sizeX/4, sizeY/3), (sizeX/2, 50)), manager=manager,
                                                object_id='#main_text_entry')
    submitButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((sizeX/4, sizeY/2), (sizeX/2, 100)), text = "SUBMIT",  manager=manager,
                                                object_id='#main_button_entry')
    backButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((sizeX/1.2)-20, sizeY/1.12), (sizeX/6, 50)), text = "BACK",  manager=manager,
                                                object_id='#backButton')
    error_msg = None # initialize error message to None

    while True:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        UI_REFRESH_RATE = clock.tick(60)/1000

        MENU_TEXT = font(100).render("REGISTIEREN", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(sizeX/2, 60))

        USERNAME_TEXT = font(30).render("USERNAME:", True, "#355E3B")
        USERNAME_RECT = MENU_TEXT.get_rect(center=(sizeX/1.5, (sizeY/3)+20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if (event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and
                event.ui_object_id == '#main_text_entry'):
                 userName = event.text

            if(event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#main_button_entry'):
                try:
                    createUserQuery(userName)
                    text_input.kill()
                    startPage(sizeX, sizeY, screen)
                except Exception as e:
                    error_msg = str(e) # set error message to the exception string
                    print(error_msg) # print error message to console
            
            if(event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#backButton'):
                    text_input.kill()
                    startPage(sizeX, sizeY, screen)
  
                
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        screen.blit(backgroundTwo, (0, 0))
        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(USERNAME_TEXT, USERNAME_RECT)

        if error_msg: # if error message exists, display it on the screen
            ERROR_TEXT = font(20).render(error_msg, True, "#FF0000")
            ERROR_RECT = ERROR_TEXT.get_rect(center=(sizeX/2.8, (sizeY/3)+70))
            screen.blit(ERROR_TEXT, ERROR_RECT)
        

        manager.draw_ui(screen)

        pygame.display.update()


def login(sizeX, sizeY, screen):
    pygame.display.set_caption("LOGIN")
    clock = pygame.time.Clock()

    #u wanna know then go read the doc https://pygame-gui.readthedocs.io/en/latest/pygame_gui.elements.html?highlight=pygame_gui.elements.UIButton#pygame_gui.elements.UIButton
    text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((sizeX/4, sizeY/3), (sizeX/2, 50)), manager=manager,
                                                object_id='#main_text_entry')
    submitButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((sizeX/4, sizeY/2), (sizeX/2, 100)), text = "LOGIN",  manager=manager,
                                                object_id='#main_button_entry')
    backButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((sizeX/1.2)-20, sizeY/1.12), (sizeX/6, 50)), text = "BACK",  manager=manager,
                                                object_id='#backButton')
    error_msg = None # initialize error message to None

    while True:
        screen.blit(background, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        UI_REFRESH_RATE = clock.tick(60)/1000

        MENU_TEXT = font(100).render("LOGIN", True, "#000000")
        MENU_RECT = MENU_TEXT.get_rect(center=(sizeX/2, 60))

        USERNAME_TEXT = font(30).render("USERNAME:", True, "#355E3B")
        USERNAME_RECT = MENU_TEXT.get_rect(center=(sizeX/2.25, (sizeY/3)+20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if (event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and
                event.ui_object_id == '#main_text_entry'):
                 userName = event.text

            if(event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#main_button_entry'):
                try:
                    checkingExistingUser(userName)
                    mainMenu(sizeX, sizeY, screen, userName)
                except Exception as e:
                    error_msg = str(e) # set error message to the exception string
                    print(error_msg) # print error message to console
            
            if(event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == '#backButton'):
                    text_input.kill()
                    startPage(sizeX, sizeY, screen)
  
                
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        screen.blit(backgroundTwo, (0, 0))
        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(USERNAME_TEXT, USERNAME_RECT)

        if error_msg: # if error message exists, display it on the screen
            ERROR_TEXT = font(20).render(error_msg, True, "#FF0000")
            ERROR_RECT = ERROR_TEXT.get_rect(center=(sizeX/2.8, (sizeY/3)+70))
            screen.blit(ERROR_TEXT, ERROR_RECT)
        

        manager.draw_ui(screen)

        pygame.display.update()



startPage(sizeX, sizeY, screen)