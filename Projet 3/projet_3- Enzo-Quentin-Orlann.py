projet "Stéganographie" Février 2020

#auteurs (Terminale S. Sadi-Carnot Jean-Bertin): CAILLEAU ORLANN / CREUZET ENZO / LIGER QUENTIN

# Gestion des accents avec le logiciel Python
# -*- coding: utf-8 -*-

#Importation de la bibliothéque PIL d'accéder à des fonctions et procédure
# permettant de manipuler des images numériques
from PIL import Image
import binascii

import binascii
from PIL import Image

def recuperation(image):  #mettre toutes les composantes dans un tableau
    Table=[]
    for y in range(image.height):
        for x in range(image.width):
            #la fonction getpixel permet de récupérer les valeur allant de 0 à 255 correspondant à l'intensité
            #de chacune des composantes Rouge, Vert, Bleu d'un pixel
            Table.append(image.getpixel((x,y)))
    return Table

def conversionbinaire(tab) :
    table = []
    for i in range(len(tab)) :
        for j in range(len(tab[i])) :
            table.append(str(format(tab[i][j], "b"))) 
            #format(x, "b") permet de renvoyer la valeur binaire 
            #on convertit en string pour ensuite pouvoir manipuler la valeur plus facilement
    for i in range(len(table)) :
        while len(table[i]) < 3 : #boucle pour verifier le nombre de caractère dans un valeur de la table
            table[i] = "0" + table[i] #ajoute un 0 a la place du premier caractère pour diminuer le nombre de caractère
    return table

def recuperationtroisdernierscaractere(tab) :
    table = []
    for i in range(len(tab)) :
        table.append(tab[i][-3] + tab[i][-2] + tab[i][-1]) #permet de recuperer seulement les 3 dernier caractère
    return table


# crée des erreurs
#def reorganisationtableau(tab) :
#    table = []
#    for i in range(0, len(tab), 3) :  #permet de deplacer l'ordre rvb en bvr 
#        table.append(tab[i + 2])
#        table.append(tab[i + 1])
#        table.append(tab[i])
#    return table

def recuperationlettres(tab) :   #permet d'addition les 3 composant bvr pour avoir un nombre binaire
    table = []
    for i in range(0, len(tab), 3) :
        table.append(tab[i][0] + tab[i][1] + tab[i][2] +tab[i+1][0] +tab[i+1][1] +tab[i+1][2] + tab[i+2][1] + tab[i+2][2])
        #il n'y a pas de tab[i][0] car on ne veux que 8 bit donc le premier du bleu n'est pas utilisé
    print(table)
    return(table)

def bintoASCIIandCESAR(table, cle) :
    texte_ASCII = ""
    for i in range(len(table)) :
        #décodage de CESAR par décalage des caractères dans la table ASCII (modulo 128)
        #on stocke temporairement la valeur binaire correspondant à chacune des lettres pour la decrypter
        tampon = (int(table[i], 2) + cle) % 128
        #source du code suivant permettant de convertir la suite de "0" ou "1" stockée dans un chaine de caractère en ASCII
        #https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
        texte_ASCII = texte_ASCII + (tampon.to_bytes((tampon.bit_length() + 7) // 8, 'big').decode("utf-8"))
    print(texte_ASCII)
    print(f"la clé est {cle}\n")
    correct = input("""\nappuyez sur entrée si le texte correspondant n'est pas correct, sinon écrivez "CORRECT" avant de continuer""")
    return (texte_ASCII, correct)



img = Image.open(r"D:\ISN\Projet 3\mario.png")

table_1 = recuperation(img)
binaire = conversionbinaire(table_1)
trois = recuperationtroisdernierscaractere(binaire)
#reorganisation = reorganisationtableau(trois)
fusion = recuperationlettres(trois)
#décodage de CESAR par décalage des caractères dans la table ASCII (modulo 128)
for cle in range(128) :
    sortie = bintoASCIIandCESAR(fusion, cle)
    if sortie[1] == "CORRECT" :
        #si l'utilisateur indique que le texte qu'il lit est correct. L'instruction "break" permet de sortir de la boucle for
        break
    else:
        #l'instrucion pass permet d'éviter les erreurs car on a pas le droit de ne rien écrire derrière "else:" elle n'a aucun effet sur le programme
        pass


print(f"le texte caché dans l'image était : {sortie[0]}")