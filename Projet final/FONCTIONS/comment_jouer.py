import pygame 
pygame.init()
pygame.font.init()

def comment_jouer():
    Interface2 = pygame.display.set_caption("Commande")
    Interface2 = pygame.display.set_mode((1300,650))
    allumer2 = 1 
    police = pygame.font.Font("./POLICES/game_over.ttf",90)
    police2 = pygame.font.Font("./POLICES/game_over.ttf",130)

    while allumer2 == 1:
        for event in pygame.event.get():
            #Detecte une pression sur la touche "ECHAP"
            if (event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                allumer2 = 0
                #Si "ECHAP" est pressé on ferme la fenêtre
                pygame.quit()
            
        background = pygame.image.load("./IMAGES/background.png").convert_alpha()
        Interface2.blit(background, (0,0))

        Q = pygame.image.load("./IMAGES/touche/Touche_Q.png").convert_alpha()    
        Q = Interface2.blit(Q, (50,320))


        D = pygame.image.load("./IMAGES/touche/Touche_D.png").convert_alpha()
        D = Interface2.blit(D, (1000,320))

 
        Lfleche = pygame.image.load("./IMAGES/touche/fleche_gauche.png").convert_alpha()    
        Lfleche = Interface2.blit(Lfleche, (300,320))
        texte_gauche = police.render("Déplacement   vers la gauche",False, (0,0,0))
        Interface2.blit(texte_gauche, (60,470))

        Rfleche = pygame.image.load("./IMAGES/touche/fleche_droite.png").convert_alpha()    
        Rfleche = Interface2.blit(Rfleche, (750,320))
        texte_droite = police.render("Déplacement    vers la droite",False, (0,0,0))
        Interface2.blit(texte_droite, (760,470))
    
        espace = pygame.image.load("./IMAGES/touche/espace.png").convert_alpha()        
        espace = Interface2.blit(espace, (525,60))
        texte_tirer = police2.render("Tirer",False, (0,0,0))
        Interface2.blit(texte_tirer, (580,180))
    
        retour = pygame.image.load("./IMAGES/touche/retour.png").convert_alpha()
        retour = pygame.transform.scale(retour,(50,50))
        retour = Interface2.blit(retour, (0,600))

    
        if pygame.mouse.get_focused():

            x, y = pygame.mouse.get_pos() 

            collide = retour.collidepoint(x, y)
            if collide:
                pressed = pygame.mouse.get_pressed()
                if pressed[0]:
                    continue
                    
        pygame.display.flip()                        