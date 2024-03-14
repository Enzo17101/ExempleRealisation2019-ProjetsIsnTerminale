#projet "Stéganographie" Février 2020

#auteurs (Terminale S. Sadi-Carnot Jean-Bertin): CAILLEAU ORLANN / CREUZET ENZO / LIGER QUENTIN

# Gestion des accents avec le logiciel Python
# -*- coding: utf-8 -*-

#Importation de la bibliothéque PIL d'accéder à des fonctions et procédure
# permettant de manipuler des images numériques
from PIL import Image
import binascii

img = Image.open("D:/ISN/Projet 3/mario.png")

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
        for j in range(len(tab[i])) :
            #format(x, "b") permet de renvoyer la valeur binaire 
            #on convertit en string pour ensuite pouvoir manipuler la valeur plus facilement
            table.append(str(format(tab[i][j], "b"))) 
    for i in range(len(table)) :
        #
        while len(table[i]) < 3 :
            table[i] = "0" + table[i]

    return table

def recuperationtroisdernierscaractere(tab) :
    table = []
    for i in range(len(tab)) :
        table.append(tab[i][-3] + tab[i][-2] + tab[i][-1])
    return table

def reorganisationtableau(tab) :
    table = []
    for i in range(0, len(tab), 3) :
        table.append(tab[i + 2])
        table.append(tab[i + 1])
        table.append(tab[i])
    return table

def recuperationlettres(tab) :
    table = []
    for i in range(0, len(tab), 3) :
        table.append(tab[i][1] + tab[i][2] + tab[i+1][0] +tab[i+1][1] +tab[i+1][2] +tab[i+2][0] + tab[i+2][1] + tab[i+2][2])
    print(table)
    return(table)



def reconstructiontexte(tab) :
    texte = ""
    texte2 = ""
    for i in range(len(tab)) :
        texte = texte + tab[i]
    texte2= binascii.unhexlify('%x' % int(texte , 2))
    print(texte2)
    print(texte)
    return texte2

reconstructiontexte(recuperationlettres(reorganisationtableau(recuperationtroisdernierscaractere(conversionbinaire(recuperationimage(img))))))