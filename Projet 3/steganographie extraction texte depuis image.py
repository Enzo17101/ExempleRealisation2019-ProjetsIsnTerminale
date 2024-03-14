#projet "Stéganographie" Février 2020

#auteurs (Terminale S. Sadi-Carnot Jean-Bertin): CAILLEAU ORLANN / CREUZET ENZO / LIGER QUENTIN

# Gestion des accents avec le logiciel Python
# -*- coding: utf-8 -*-

#Importation de la bibliothéque PIL d'accéder à des fonctions et procédure
# permettant de manipuler des images numériques
from PIL import Image

img = Image.open("D:/ISN/Projet 3/img.png")
cle = input("clé de cryptage")

#fonction permettant de créer un tableau de valeur contenant toutes les composantes RVB (Rouge Vert Bleu) de l'image
def recuperationimage(image) :
    table = []
    for y in range(image.height) :
        for x in range(image.width) :
            table.append(image.getpixel((x,y)))
    return table

def conversionbinaire(tab) :
    table = []
    for i in range(len(tab)) :
        table.append([])
        for j in range(len(tab[i])) :
            table[i].append(format(tab[i][j], "b"))
    return table

def binaireversASCII(tab, cle) :
    for i in range(len(tab)) :
        for j in range(len(tab[i])) :
            
    return texte



creation(conversiondecimale(conversionbinaire(recuperationimage(img))), img)