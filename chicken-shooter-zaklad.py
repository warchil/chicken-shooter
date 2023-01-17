import pygame

# Pripraveni pygame (inicializace)
pygame.init()

# Vytvoreni herniho okna o dane sirce a vysce (nasobek velikosti dlazice)
herniOkno = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

# Pojmenovani herniho okna
pygame.display.set_caption("Ostrostřelec")

# Skarede cernobile kurzory umi pygame jednoduse :)
# pygame.mouse.set_cursor(pygame.cursors.broken_x)

# Jakykoliv obrazkovy kurzor
# obrazekZamerovace = pygame.image.load('crosshair.png')
# obrazekZamerovace = pygame.transform.scale(obrazekZamerovace, (64, 64))
# pygame.mouse.set_visible(False)
# obrazekZamerovace_rect = obrazekZamerovace.get_rect()

# Promenna "hraBezi" je nastavena na True (Pravda), pokud hra bezi. Jakmile hrac klikne na krizek,
# tak se promenna nastavi na False (Nepravda), hlavni herni cyklus se ukonci a hra konci.
hraBezi = True

#### Hlavni herni cyklus
while hraBezi:

    # Cyklus, ktery zjistuje, jake nastaly udalosti.
    for event in pygame.event.get():
        # Pokud hrac kliknul na krizek, tak se nastavi promenna "hraBezi" na False (Nepravda)
        if event.type == pygame.QUIT:
            hraBezi = False

    # herniOkno.fill(pygame.Color('black'))

    # obrazekZamerovace_rect.center = pygame.mouse.get_pos()  # Nastaveni pozice kurzoru
    # herniOkno.blit(obrazekZamerovace, obrazekZamerovace_rect)  # Vykresleni kurozru

    # Zavolame funkci "update", ktera vykresli vsechny zmeny na obrazovku
    pygame.display.update()

# Ukonceni pygame
pygame.quit()