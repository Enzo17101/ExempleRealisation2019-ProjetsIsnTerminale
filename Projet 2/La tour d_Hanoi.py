
#définition des variables

#une liste de trois entités (trois tours) qui sont trois listes de quatres entités (quatres disques)
hanoi = [[1,2,3,4],[],[]]
final = [[],[],[1,2,3,4]]
deplacements = 0 #compteur de déplacements
liste = [1,2,3]

#methode = int(input("choisissez une méthode de déplacement (0 = logique, 1 = IA)"))



#IA
if hanoi[0][0] % 2 == 0 :
    hanoi[2].insert(0,hanoi[0][0])
else :
    hanoi[1].insert(0,hanoi[0][0])


while final != hanoi :
    #teste si la case 2 est libre, si oui il y place la plus grande des plaque au début de la case 1 ou 3
    if hanoi[1] == [] and hanoi[0][0] > hanoi[2][0] :
        hanoi[1].insert(0,hanoi[0][0])
        hanoi[1].remove
    elif hanoi[1] == [] :
        hanoi[1].insert(0,hanoi[2][0])
    if hanoi[2] == [] and hanoi[0][0] > hanoi[1][0] :
        hanoi[2].insert(0,hanoi[0][0])
    elif hanoi[2] == [] :
        hanoi[2].insert(0,hanoi[1][0])
    break


print(hanoi)







#methode logique (fuck car trop long)