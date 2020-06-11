#!/usr/bin/python3
# -*- coding: utf8 -*-

import donnees
from fonctions import *


lecture()
init_player()
init_mots()
run = True
while run :
    selec_lettre()
    recherche_mots()
    if donnees.essais == 0 :
        print("Tu as perdu ! /n Veux tu rejouer ?")
        reponse = question()
        donnees.lettre_before = []
        if reponse == "oui":
            donnees.essais = 8
            init_mots()
        if reponse == "non":
            run = False
            print("bye")
    if donnees.hidden_word.count("*") == 0:
        donnees.dic_score[donnees.player] += donnees.essais
        donnees.lettre_before = []
        print("Tu as trouvé '{}' !!".format("".join(donnees.hidden_word)))
        print("Tu as marqué {} points".format(donnees.essais))
        print("Veux tu rejouer ?")
        reponse = question()
        ecriture()
        if reponse == "oui":
            donnees.essais = 8
            init_mots()
        if reponse == "non":
            run = False
            print("A bientôt !")

            
    

        
            
        

