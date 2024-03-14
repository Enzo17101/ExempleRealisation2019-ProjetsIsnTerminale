#auteurs (Terminale S. Sadi-Carnot Jean-Bertin): CAILLEAU Orlann / CREUZET Enzo / LIGER Quentin 
import binascii
from PIL import Image

def recuperation(image):  #mettre toutes les composantes dans un tableau
    Table=[]
    for y in range(image.height):
        for x in range(image.width):
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

def reorganisationtableau(tab) :
    table = []
    for i in range(0, len(tab), 3) :  #permet de deplacer l'ordre rvb en bvr 
        table.append(tab[i + 2])
        table.append(tab[i + 1])
        table.append(tab[i])
    return table

def recuperationlettres(tab) :   #permet d'addition les 3 composant bvr pour avoir un nombre binaire
    table = []
    for i in range(0, len(tab), 3) :
        table.append(tab[i][1] + tab[i][2] + tab[i+1][0] +tab[i+1][1] +tab[i+1][2] +tab[i+2][0] + tab[i+2][1] + tab[i+2][2])
                        #il n'y a pas de tab[i][0] car on ne veux que 8 bit donc le premier du bleu n'est pas utilisé
    return(table)

def reconstructiontexte(tab) :
    texte = ""
    texte2 = ""
    for i in range(len(tab)) :
        texte = texte + tab[i]
    texte2= binascii.unhexlify('%x' % int(texte , 2))
    return texte2

img = Image.open("C:/Users/canai/Desktop/Traitement Image/Mario_cryptee.png")

table_1 = recuperation(img)
binaire = conversionbinaire(table_1)
trois = recuperationtroisdernierscaractere(binaire)
reorganisation = reorganisationtableau(trois)
fusion = recuperationlettres(reorganisation)
texte = reconstructiontexte(fusion)


print(texte)
a = b'\xe9\x80\x80'.decode('utf-8')
u'\u9000'
print(a)
