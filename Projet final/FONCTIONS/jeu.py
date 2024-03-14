import pygame 
pygame.init()

def jeu() :
    class Jeu: #permet de appeler les autres classes
        
       def __init__(self):
            self.joueur = Joueur() #appele la classe joueur
            self.ennemi_1 = Ennemi_1()
            self.appuyer = {}

    class Joueur(pygame.sprite.Sprite):
        
        def __init__(self):
            super().__init__() 
            self.vie = 3 #determine la vie du joueur
            self.vie_max = 3 #vie maximum du joueur
            self.attaque = 1 #degat sur les ennemies
            self.vitesse = 12 #vitesse de deplacement en nombre de pixel
            self.listes_missiles = pygame.sprite.Group() #permet de regrouper les missiles en dans avoir plusieur en meme temps
            self.image = pygame.image.load("./IMAGES/vaisseau.png").convert_alpha() 
            self.image = pygame.transform.scale(self.image,(100,100))
            self.rect = self.image.get_rect() #determine la position de l'objet
            self.rect.x = 600 #deplace l'image en x
            self.rect.y = 550 #deplace l'image en y
        
    
        def droite(self): #permet d'aller vers la droite
            self.rect.x += self.vitesse #ajoute la vitesse de deplacement donc deplacement en x ici de 15 pixels

        def gauche(self): #permet d'aller vers la gauche
            self.rect.x -= self.vitesse #ajoute la vitesse de deplacement donc deplacement en x ici de -15 pixels
    
        def missiles(self): #permet de tirer
            self.listes_missiles.add(Missile(self)) #tire les missiles a gauches
            self.listes_missiles.add(Missile2(self)) #tire les missiles a droites


    class Missile(pygame.sprite.Sprite): #missiles gauche
        
        def __init__(self, joueur): 
            super().__init__() 
            self.vitesse = 15 #vitesse de deplacement en nombre de pixel
            self.joueur = Joueur() #permet de faire apparaitre le missiles directement sur le joueur
            self.image = pygame.image.load("./IMAGES/missile/missile_vaisseau.png").convert_alpha() 
            self.image = pygame.transform.scale(self.image,(15,15))
            self.rect = self.image.get_rect() #determine la position de l'objet
            self.rect.x = joueur.rect.x + 10 #deplace l'image en x d'apres l'image du joueur
            self.rect.y = joueur.rect.y + 35 #deplace l'image en y d'apres l'image du joueur
    
        def mouvement(self): #le missiles se deplace
            self.rect.y -= self.vitesse #pour monter il doit aller dans les -y 
            if self.rect.y > 0: #permet de supprimer l'image apres etre sortie de la fenêtre
                self.joueur.listes_missiles.remove(self)
            

    class Missile2(pygame.sprite.Sprite): #idem que missiles 1 sauf la position d'apres l'image du joueur
        
        def __init__(self, joueur):
            super().__init__()
            self.vitesse = 15
            self.joueur = Joueur()
            self.image = pygame.image.load("./IMAGES/missile/missile_vaisseau.png").convert_alpha() 
            self.image = pygame.transform.scale(self.image,(15,15))
            self.rect = self.image.get_rect()
            self.rect.x = joueur.rect.x + 75
            self.rect.y = joueur.rect.y + 35
    
        def mouvement(self):
            self.rect.y -= self.vitesse
            if self.rect.y < 0:
                self.joueur.listes_missiles.remove(self)

#crée la classe ennemi_1 (sur la même base que la classe Joueur)
    class Ennemi_1(pygame.sprite.Sprite) :

        def __init__(self):
            super().__init__()
            self.vie = 1
            self.vie_max = 1
            self.attaque = 1
            self.vitesse = 2
            self.image = pygame.image.load("./IMAGES/ennemi_simple.png")
            self.image = pygame.transform.scale(self.image,(50,50))
            self.rect = self.image.get_rect() #determine la position de l'objet
            self.rect.x = 625 #deplace l'image en x
            self.rect.y = 150 #deplace l'image en y

        def gauche(self):
            self.rect.x -= self.vitesse

        def droite(self) :
            self.rect.x += self.vitesse


    Interface3 = pygame.display.set_caption("Commande")
    Interface3 = pygame.display.set_mode((1305,650))

    jeu = Jeu() #appele la classe jeu qui donne acces a toute les sous classes

    allumer3 = 1 
    direction_ennemis = 1 #initialise la direction du groupe d'ennemis (1 pour droite et 0 pour gauche)
    while allumer3 == 1:
    
        background = pygame.image.load("./IMAGES/background.png").convert_alpha()
        Interface3.blit(background, (0,0))
    
        Interface3.blit(jeu.joueur.image, jeu.joueur.rect) #fait apparaitre l'image du joueur avec sa position
        Interface3.blit(jeu.ennemi_1.image, jeu.ennemi_1.rect) #fait apparaitre l'image du joueur avec sa position


        for missile in jeu.joueur.listes_missiles:#permet d'afficher l'image d'un missiles 
            missile.mouvement()
        jeu.joueur.listes_missiles.draw(Interface3)
    
        pygame.display.flip() 
    
        for event in pygame.event.get():
            if (event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                allumer3 = 0
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                jeu.appuyer[event.key] = True #determine si une touche est pressé 
                if event.key==pygame.K_SPACE:
                    jeu.joueur.missiles()
            elif event.type == pygame.KEYUP: 
                jeu.appuyer[event.key] = False #determine si une touche est relaché
    
        if jeu.appuyer.get(pygame.K_RIGHT) and jeu.joueur.rect.x < 1200: #permet de savoir si la flèche droite et appuyer et si le joueur peut aller vers la droite sans sortir de l'interface
            jeu.joueur.droite()
        elif jeu.appuyer.get(pygame.K_LEFT) and jeu.joueur.rect.x > 0: #permet de savoir si la flèche gauche et appuyer et si le joueur peut aller vers la gauche sans sortir de l'interface
            jeu.joueur.gauche()
        elif jeu.appuyer.get(pygame.K_d) and jeu.joueur.rect.x < 1200: #permet de savoir si la touche d et appuyer et si le joueur peut aller vers la droite sans sortir de l'interface
            jeu.joueur.droite()
        elif jeu.appuyer.get(pygame.K_a) and jeu.joueur.rect.x > 0: #permet de savoir si la touche q et appuyer et si le joueur peut aller vers la droite sans sortir de l'interface
            jeu.joueur.gauche()
        
        if jeu.ennemi_1.rect.x < 500 :
            direction_ennemis = 1
        if jeu.ennemi_1.rect.x > 750 :
            direction_ennemis = 0

        if direction_ennemis == 1 :
            jeu.ennemi_1.droite()
        if direction_ennemis == 0 :
            jeu.ennemi_1.gauche()

jeu()