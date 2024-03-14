#projet "Stéganographie" Février 2020

#auteurs (Terminale S. Sadi-Carnot Jean-Bertin): CAILLEAU ORLANN / CREUZET ENZO / LIGER QUENTIN

# Gestion des accents avec le logiciel Python
# -*- coding: utf-8 -*-

#Importation de la bibliothéque PIL d'accéder à des fonctions et procédure
#permettant de manipuler des images numériques
#et de Tkinter permettant d'afficher des fenêtres extérieure au terminal
#ici un exploreur de fichier

from PIL import Image as I

#texte = input("entrez le texte à crypter (400 caractères max")

img = I.open("D:/ISN/Projet 3/img.png")


#fonction permettant de créer un tableau de valeur contenant toutes les composantes RVB (Rouge Vert Bleu) de l'image
def recuperationimage(image) :
    table = []
    for y in range(image.height) :
        for x in range(image.width) :
            table.append(image.getpixel((x,y)))
    return table

#fonction permettant de convertir l'ensemble des valeurs décimales du tableau précédent en valeurs binaires 
def conversionbinaire(tab) :
    table = []
    for i in range(len(tab)) :
        table.append([])
        for j in range(len(tab[i])) :
            table[i].append(format(tab[i][j], "b"))
    print(table)
    return table

#fonction permettant de reconvertir l'ensemble des valeurs binaires du tableau précédent en valeurs décimales 
def conversiondecimale(tab):
    table = []
    for i in range(len(tab)) :
        table.append([])
        for j in range(len(tab[i])) :
            table[i].append(int(tab[i][j],2))
    for i in range(len(tab)) :
        table[i] = tuple(table[i])
    return table

#fonction permettant de reconstruire une image finale 
def creation(table, image):
    img_c = I.new("RGB", (image.width, image.height))
    for y in range(image.height) :
        for x in range(image.width) :
            img_c.putpixel((x,y), table[(y * image.width + x)])
    img_c.show()

#fonction permettant de 

creation(conversiondecimale(conversionbinaire(recuperationimage(img))), img)