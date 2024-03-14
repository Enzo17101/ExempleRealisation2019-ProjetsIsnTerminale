#Définition des variables de base
valeur_des_billets = [5, 10, 20, 50]
nombre_de_billets = [0, 0, 0, 0]
position = 3

#Entrée par l'utilisateur
montant_retire = input("Montant retiré (entrer un multiple de 5)")
methode = input("Choisissez une méthode de répartition des billets (0 = Nombre minimum de billets / 1 = Au moins un billet de chaque sorte)")

#Vérification de la validité des entrées
while int(montant_retire) % 5 != 0 or not montant_retire.isdigit:
    print("Le montant entré n'est pas un multiple de 5 ou contient des caractères invalides")
    montant_retire = input("Montant retiré (entrer un multiple de 5)")
montant_retire = reste = int(montant_retire)
while int(methode) != 0 and int(methode) != 1 :
    print("La valeur entrée pour la méthode est invalide")
    methode = input("Choisissez une méthode de répartition des billets (0 = Nombre minimum de billets / 1 = Au moins un billet de chaque sorte)")
methode = int(methode)

#Méthode 1
if methode == 0 :
    while reste >= valeur_des_billets[0] :
        if reste >= valeur_des_billets[position] :
            reste -= valeur_des_billets[position]
            nombre_de_billets[position] += 1
        if reste < valeur_des_billets[position] :
            position -= 1

#Méthode 2
if methode == 1 :
    while reste >=valeur_des_billets[0] :
        for position in range(4) :
            if reste - valeur_des_billets[position] >= 0 :
                reste -= valeur_des_billets[position]
                nombre_de_billets[position] += 1


#Affichage
print(f"Montant retiré = {montant_retire}")
print(f"Nombre de billets de 50€ = {nombre_de_billets[3]}")
print(f"Nombre de billets de 20€ = {nombre_de_billets[2]}")
print(f"Nombre de billets de 10€ = {nombre_de_billets[1]}")
print(f"Nombre de billets de 5€ = {nombre_de_billets[0]}")

end = input("Appuyez sur entrée pour quitter")