#PROJET FINAL d'ISN
#Auteurs : Creuzet Enzo, Caillau Orlann, Liger Quentin

#basé sur le code de "nolimitech" 
#https://openclassrooms.com/forum/sujet/pygame-faire-un-bouton


import pygame 
from FONCTIONS.jeu import jeu
from FONCTIONS.comment_jouer import comment_jouer

#initialisation du module pygame, et des polices
pygame.init()
pygame.font.init()

#Initalisation de l'interface
Interface = pygame.display.set_caption("Space Invader")
Interface = pygame.display.set_mode((1300,650))
allumer = 1 
police = pygame.font.Font("./POLICES/game_over.ttf",130)


#Boucle de l'interface
while allumer == 1:
    for event in pygame.event.get():
        #Detecte une pression sur la touche "ECHAP"
        if (event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            allumer = 0
            #Si "ECHAP" est pressé on ferme la fenêtre
            pygame.quit()
    
    #chargement de l'arrière plan
    background = pygame.image.load("./IMAGES/background.png").convert_alpha()
    Interface.blit(background, (0,0))

    #création des boutons
    FOND_BOUTON_JOUER = pygame.draw.rect(Interface,(0,0,0), (390,110,520,120))
    BOUTON_JOUER = pygame.draw.rect(Interface,(150,150,150), (400,120,500,100))
    FOND_BOUTON_COMMENT_JOUER = pygame.draw.rect(Interface,(0,0,0), (390,260,520,120))
    BOUTON_COMMENT_JOUER = pygame.draw.rect(Interface,(150,150,150), (400,270,500,100))
    FOND_BOUTON_QUITTER = pygame.draw.rect(Interface,(0,0,0), (390,410,520,120))
    BOUTON_QUITTER = pygame.draw.rect(Interface,(150,150,150), (400,420,500,100))

    #création du texte jouer
    texte_JOUER = police.render("JOUER",False, (0,0,150))
    Interface.blit(texte_JOUER, (570,130))

    #création du texte comment jouer
    texte_COMMENT_JOUER= police.render("COMMENT JOUER",False, (0,0,150))
    Interface.blit(texte_COMMENT_JOUER, (440,280))

    #création du texte quitter
    texte_QUITTER = police.render("QUITTER ",False, (0,0,150))
    Interface.blit(texte_QUITTER, (550,430))


    if pygame.mouse.get_focused():
        ## Trouve position de la souris
        x, y = pygame.mouse.get_pos() 
        ## S'il y a collision:
        collide = BOUTON_QUITTER.collidepoint(x, y)
        if collide:
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:      
                allumer = 0
                pygame.quit()
                break
            
    if pygame.mouse.get_focused():
        ## Trouve position de la souris
        x, y = pygame.mouse.get_pos() 
        ## S'il y a collision:
        collide = BOUTON_COMMENT_JOUER.collidepoint(x, y)
        if collide:
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:      
                comment_jouer()
                allumer = 0
                
                
            
    if pygame.mouse.get_focused():
            ## Trouve position de la souris
        x, y = pygame.mouse.get_pos() 
        ## S'il y a collision:
        collide = BOUTON_JOUER.collidepoint(x, y)
        if collide:
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:      
                jeu()
                allumer = 0
                pygame.quit()
                break
    pygame.display.flip()                    
