#!/usr/bin/python3
# -*- coding: utf8 -*-

import donnees

def init_player():
    global dic_score
    print("Entre ton pseudo")
    new_player = True
    donnees.player = input()
    donnees.player = donnees.player.title()
    if not donnees.player.isalpha():
        print("Pseudo en alphanumérique")
        return init_player()
    for cle in donnees.dic_score.keys() :
        if cle == donnees.player:
            print("Rebonjour {}".format(donnees.player))
            print("Ton score est de {}".format(donnees.dic_score[donnees.player]))
            new_player = False
    if new_player :
        print("Bonjour {}".format(donnees.player))
        donnees.dic_score[donnees.player] = 0
        ecriture()

def lecture():
    import os
    if not os.path.exists("Score"):
        fichier = open("Score", "w")
        fichier.close()
    fichier = open("Score", "r")
    data = fichier.readlines()
    for a in data :
        ligne = a.split()
        donnees.dic_score[ligne[0]] = int(ligne[1])
    fichier.close()

def ecriture():
    fichier = open("Score", "w")
    for key in donnees.dic_score.keys():
        fichier.write(key + " " + str(donnees.dic_score[key]) + "\n")
    fichier.close()
    
def init_mots():
    import random
    global word, hidden_word
    word_str = random.choice(donnees.liste_mots)
    if len(donnees.liste_mots) == len(donnees.mots_precedent) :
        print("Remise à zero de la liste de mots")
        donnees.mots_precedent = []
    for i in donnees.mots_precedent:
        if i == word_str:
            return init_mots()
    donnees.mots_precedent.append(word_str)
    a = len(word_str)
    donnees.word = list(word_str)
    donnees.hidden_word = ["*"] * a
    donnees.hidden_word[0] = donnees.word[0]
    affichage_hidden()
    
def selec_lettre():
    global lettre
    print("A toi de jouer ! Choisis une lettre")
    if len(donnees.lettre_before) != 0:
        print("Tu as déjà entré les lettres : " + ",".join(donnees.lettre_before))
    donnees.lettre = input()
    donnees.lettre = donnees.lettre.lower()
    if not donnees.lettre.isalpha():
        print("Entre une lettre !")
        return selec_lettre()
    if len(donnees.lettre) != 1:
        print("Entre UNE lettre !")
        return selec_lettre()
    for a in donnees.lettre_before:
        if a == donnees.lettre:
            print("Tu as déjà entré la lettre '{}', tente autre chose !".format(donnees.lettre))
            return selec_lettre()
    donnees.lettre_before.append(donnees.lettre)

def recherche_mots():
    global test, hidden_word, essais
    cmpt = 0
    test = False
    for a in donnees.word:
        if a == donnees.lettre:
            test = True
            print("Bravo ! la lettre '{}' est dans le mots à trouver !".format (donnees.lettre))
            donnees.hidden_word[cmpt] = donnees.lettre
            affichage_hidden()
        cmpt += 1
            
    if not test :
        print ("Perdu ! la lettre '{}' n'est pas dans le mots à trouver !".format (donnees.lettre))     
        donnees.essais -= 1
        print("il reste {} essais avant de perdre".format(donnees.essais))
        affichage_hidden()

        
def affichage_hidden():
    print("".join(donnees.hidden_word))
    
def question():
    reponse = input("oui ou non ?")
    reponse = reponse.lower()
    if reponse == "oui" or reponse == "non":
        print("reponse valide")
        print(reponse)
        return reponse
    else :
        print("reponse non valide")
        return question()

        



                  

    

    