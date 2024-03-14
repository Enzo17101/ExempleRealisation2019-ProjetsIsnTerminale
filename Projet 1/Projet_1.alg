<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER Quantité[1]" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2defaut="" F2etat="inactif" F2para="" F2lignes=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param arrondiAuto="vrai" totalBoucles="5000000" totalAffichages="1000" maxBoucle="500000" epaisseurPoint="2" nbDecimales="8" epaisseurLigne="2"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#Position" algoitem="Position EST_DU_TYPE NOMBRE"/>
        <item code="1#LISTE#Quantité" algoitem="Quantité EST_DU_TYPE LISTE"/>
        <item code="1#LISTE#Billets" algoitem="Billets EST_DU_TYPE LISTE"/>
        <item code="1#NOMBRE#Montant_à_retirer" algoitem="Montant_à_retirer EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#Reste" algoitem="Reste EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#Méthode" algoitem="Méthode EST_DU_TYPE NOMBRE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="2#Montant_à_retirer#pasliste" algoitem="LIRE Montant_à_retirer"/>
        <item code="5#Position#4#pasliste" algoitem="Position PREND_LA_VALEUR 4"/>
        <item code="5#Billets#5:10:20:50#1" algoitem="Billets[1] PREND_LA_VALEUR 5:10:20:50"/>
        <item code="5#Quantité#0:0:0:0#1" algoitem="Quantité[1] PREND_LA_VALEUR 0:0:0:0"/>
        <item code="5#Reste#Montant_à_retirer#pasliste" algoitem="Reste PREND_LA_VALEUR Montant_à_retirer"/>
        <item code="2#Méthode#pasliste" algoitem="LIRE Méthode"/>
        <item code="6#Méthode&lt;=0" algoitem="SI (Méthode&lt;=0) ALORS">
            <item code="7#debutsi" algoitem="DEBUT_SI"/>
            <item code="4#Méthode 1#1" algoitem="AFFICHER &quot;Méthode 1&quot;"/>
            <item code="15#Reste>=Billets[1]" algoitem="TANT_QUE (Reste>=Billets[1]) FAIRE">
                <item code="16#debuttantque" algoitem="DEBUT_TANT_QUE"/>
                <item code="6#Reste>=Billets[Position]" algoitem="SI (Reste>=Billets[Position]) ALORS">
                    <item code="7#debutsi" algoitem="DEBUT_SI"/>
                    <item code="5#Reste#Reste-Billets[Position]#pasliste" algoitem="Reste PREND_LA_VALEUR Reste-Billets[Position]"/>
                    <item code="5#Quantité#Quantité[Position]+1#Position" algoitem="Quantité[Position] PREND_LA_VALEUR Quantité[Position]+1"/>
                    <item code="8#finsi" algoitem="FIN_SI"/>
                </item>
                <item code="6#Reste&lt;Billets[Position]" algoitem="SI (Reste&lt;Billets[Position]) ALORS">
                    <item code="7#debutsi" algoitem="DEBUT_SI"/>
                    <item code="5#Position#Position-1#pasliste" algoitem="Position PREND_LA_VALEUR Position-1"/>
                    <item code="8#finsi" algoitem="FIN_SI"/>
                </item>
                <item code="17#fintantque" algoitem="FIN_TANT_QUE"/>
            </item>
            <item code="8#finsi" algoitem="FIN_SI"/>
            <item code="9#sinon" algoitem="SINON">
                <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                <item code="4#Méthode 2#1" algoitem="AFFICHER &quot;Méthode 2&quot;"/>
                <item code="15#Reste>=Billets[1]" algoitem="TANT_QUE (Reste>=Billets[1]) FAIRE">
                    <item code="16#debuttantque" algoitem="DEBUT_TANT_QUE"/>
                    <item code="12#Position#0#4" algoitem="POUR Position ALLANT_DE 0 A 4">
                        <item code="13#debutpour" algoitem="DEBUT_POUR"/>
                        <item code="6#Reste-Billets[Position]>=0" algoitem="SI (Reste-Billets[Position]>=0) ALORS">
                            <item code="7#debutsi" algoitem="DEBUT_SI"/>
                            <item code="5#Reste#Reste -= Billets[Position]#pasliste" algoitem="Reste PREND_LA_VALEUR Reste -= Billets[Position]"/>
                            <item code="5#Quantité#Quantité[Position] += 1#Position" algoitem="Quantité[Position] PREND_LA_VALEUR Quantité[Position] += 1"/>
                            <item code="8#finsi" algoitem="FIN_SI"/>
                        </item>
                        <item code="14#finpour" algoitem="FIN_POUR"/>
                    </item>
                    <item code="17#fintantque" algoitem="FIN_TANT_QUE"/>
                </item>
                <item code="11#finsinon" algoitem="FIN_SINON"/>
            </item>
        </item>
        <item code="4#nombre à retirer : #0" algoitem="AFFICHER &quot;nombre à retirer : &quot;"/>
        <item code="3#Montant_à_retirer#1#pasliste" algoitem="AFFICHER Montant_à_retirer"/>
        <item code="4#Nombre de billets de 50€ = #0" algoitem="AFFICHER &quot;Nombre de billets de 50€ = &quot;"/>
        <item code="3#Quantité#1#4" algoitem="AFFICHER Quantité[4]"/>
        <item code="4#Nombre de billets de 20€ = #0" algoitem="AFFICHER &quot;Nombre de billets de 20€ = &quot;"/>
        <item code="3#Quantité#1#3" algoitem="AFFICHER Quantité[3]"/>
        <item code="4#Nombre de billets de 10€ = #0" algoitem="AFFICHER &quot;Nombre de billets de 10€ = &quot;"/>
        <item code="3#Quantité#1#2" algoitem="AFFICHER Quantité[2]"/>
        <item code="4#Nombre de billets de 5€ = #0" algoitem="AFFICHER &quot;Nombre de billets de 5€ = &quot;"/>
        <item code="3#Quantité#1#1" algoitem="AFFICHER Quantité[1]"/>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
