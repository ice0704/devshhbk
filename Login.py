import pygame

# Pygame initialisieren
pygame.init()

# Fenstergröße festlegen
size = (900, 600)
screen = pygame.display.set_mode(size)

# Schriftarten definieren
font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 24)

# Benutzerliste definieren
users = ["Mirko", "Oli", "Sergio", "Non", "Laurenz"]

# Dropdown-Menü definieren
dropdown_rect = pygame.Rect(50, 100, 350, 40)
dropdown_items = list(users)
selected_item = None
dropdown_active = False

# Login-Button definieren
login_button_rect = pygame.Rect(500, 100, 300, 40)
login_button_text = font.render("Login", True, pygame.Color("white"))

# Haupt-Loop
done = False
while not done:

    # Ereignisschleife durchlaufen
    for event in pygame.event.get():
        # Beim Schließen-Button auf das X-Symbol klicken
        if event.type == pygame.QUIT:
            done = True
        # Wenn auf die Maustaste gedrückt wird
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Wenn auf das Dropdown-Menü geklickt wird, öffne oder schließe es
            if dropdown_rect.collidepoint(event.pos):
                dropdown_active = not dropdown_active
            # Wenn das Dropdown-Menü geöffnet ist, prüfe, ob ein Eintrag ausgewählt wurde
            elif dropdown_active:
                for i, item in enumerate(dropdown_items):
                    item_rect = pygame.Rect(dropdown_rect.x, dropdown_rect.y + (i + 1) * dropdown_rect.height, dropdown_rect.width, dropdown_rect.height)
                    if item_rect.collidepoint(event.pos):
                        selected_item = item
                        dropdown_active = False
                        break
            # Wenn auf den Login-Button geklickt wird, prüfe, ob ein Benutzer ausgewählt wurde
            elif login_button_rect.collidepoint(event.pos):
                if selected_item is not None:
                    # Führe Aktionen aus, z.B. Anmelden oder Programm beenden
                    print(f"Logged in as {selected_item}")
                    # Hier könnten Sie weitere Aktionen ausführen, z.B. eine neue Seite öffnen oder das Programm beenden.

    # Benutzeroberfläche zeichnen

    # Hintergrund schwarz füllen
    screen.fill(pygame.Color("black"))

    # Dropdown-Menü als weißes Rechteck zeichnen
    pygame.draw.rect(screen, pygame.Color("white"), dropdown_rect, 2)

    # Text für den ausgewählten Benutzernamen rendern und auf das Dropdown-Menü zeichnen
    dropdown_text = font.render(selected_item if selected_item is not None else "Benutzernamen auswählen...", True, pygame.Color("white"))
    screen.blit(dropdown_text, (dropdown_rect.x + 5, dropdown_rect.y + 5))

    # Wenn das Dropdown-Menü aktiv ist, alle Elemente in der Dropdown-Liste als Rechtecke zeichnen und ihre Texte rendern
    if dropdown_active:
        for i, item in enumerate(dropdown_items):
            item_rect = pygame.Rect(dropdown_rect.x, dropdown_rect.y + (i + 1) * dropdown_rect.height, dropdown_rect.width, dropdown_rect.height)
            pygame.draw.rect(screen, pygame.Color("white"), item_rect, 2)
            item_text = small_font.render(item, True, pygame.Color("white"))
            screen.blit(item_text, (item_rect.x + 5, item_rect.y + 5))

    # Login-Button als weißes Rechteck zeichnen und Text rendern
    pygame.draw.rect(screen, pygame.Color("white"), login_button_rect, 2)
    screen.blit(login_button_text, (login_button_rect.x + 5, login_button_rect.y + 5))

    # Pygame-Fenster aktualisieren
    pygame.display.flip()

# Pygame beenden
pygame.quit()
