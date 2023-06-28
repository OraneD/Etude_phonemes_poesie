import xml.etree.ElementTree as ET
import re
from pathlib import Path
from termcolor import colored
import pandas as pd 
from tabulate import tabulate
from ansi2html import Ansi2HTMLConverter
import csv
import time
import csv

start_time = time.time()
import os
print(os.getcwd())


def transcription(fichier, nom_sortie) : 
    diereses = pd.read_csv("diereses.txt")
    
    #Listes pour les règles 
    voyelles_sampa = ["i", "e", "E", "a", "A", "O", "o", "u", "y", "2", "9", "@", "e~", "a~", "o~", "9~", "C", "H", "j","w"]
    voyelles = ["a", "e", "i", "o", "u", "y", "é", "è","à", "â"]
    pattern = re.compile("^h[aeiouyéèà]{2}") #Tentative de règle pour les h aspirés, voir dans la boucle
    #######################################
    
    #Variables pour évaluer le script
    nb_vers = 0
    nb_vers_bon = 0
    liste_mots_inconnus = []
    evaluation_poemes = []
    ######################################
    with open(nom_sortie, "w") as correction :    
        with open(fichier, "r") as csvfile :
            lire = csv.reader(csvfile)
            for row in lire :
                    print(row)
                    vers_propre = row[0]
                    liste_mots_vers = vers_propre.split()
                    for mot in liste_mots_vers :
                        if "'" in mot :
                            sep = mot.split("'")
                            liste_mots_vers.insert(liste_mots_vers.index(mot), sep[0])
                            liste_mots_vers.insert(liste_mots_vers.index(mot), sep[1])
                            liste_mots_vers.remove(mot)
                        elif "-" in mot :
                            sep = mot.split("-")
                            liste_mots_vers.insert(liste_mots_vers.index(mot), sep[0])
                            liste_mots_vers.insert(liste_mots_vers.index(mot), sep[1])
                            liste_mots_vers.remove(mot)  
                    vers_phonetique_sanscouleur = ""
                    longueur_vers = len(liste_mots_vers)
                    nb_syllabes = 0
                    while longueur_vers > 0 :
                        mot = liste_mots_vers[0].strip()
                        liste_mots_vers = liste_mots_vers[1:]
                        longueur_vers = len(liste_mots_vers)
                        with open("dico1.txt", "r") as dico :
                            for line in dico.readlines():
                                if line[0] != "*":                    
                                    ortho = line.split()[0]
                                    phonetique = line.split()[1]
            
                                    if mot == ortho :
                                        if longueur_vers >= 1 :
                                            #Règles pour les "@" :
                                            if (len(mot) > 3 or mot == "une" or mot == "âme") and (mot[-1] == "e" or mot[-2:] == "es" or mot[-3:] == "ent") and (liste_mots_vers[0])[0] not in voyelles and liste_mots_vers[0][0] != "h" and phonetique[-1] != "@":
                               
                                                vers_phonetique_sanscouleur += phonetique + "@"
                                                for lettre in phonetique :
                                                    if lettre in voyelles_sampa :
                                                        nb_syllabes += 1
                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                nb_syllabes += 1
                                                if nb_syllabes == 6 :
            
                                                    vers_phonetique_sanscouleur += "|"
                                                break
                                            
                                            #Règles pour les "h" aspirés
                                            elif (len(mot) > 3 or mot == "une") and (mot[-1] == "e" or mot[-2:] == "es" or mot[-3:] == "ent") and liste_mots_vers[0][0] == "h" :
                                                if pattern.match(liste_mots_vers[0][0:3]) == None :
                
                                                    vers_phonetique_sanscouleur += phonetique
                                                    for lettre in phonetique :
                                                        if lettre in voyelles_sampa :
                                                            nb_syllabes += 1
                                                    if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                        nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                    break
                                                    if nb_syllabes == 6 :
            
                                                        vers_phonetique_sanscouleur += "|"
                                                else :
            
                                                    for lettre in phonetique :
                                                        if lettre in voyelles_sampa :
                                                            nb_syllabes += 1
                                                    if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                        nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                    nb_syllabes += 1
                                                    if nb_syllabes == 6 :
                                                        vers_phonetique_sanscouleur += "|"
                                                    break
                                                
                                            #Règles pour les liasions - "s"
                                            elif len(mot) > 3 and mot[-2:] == "es" and liste_mots_vers[0][0] in voyelles :
                                                vers_phonetique_sanscouleur += phonetique + "@" +"z"
                                                for lettre in phonetique :
                                                    if lettre in voyelles_sampa :
                                                        nb_syllabes += 1
                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                nb_syllabes += 1
                                                if nb_syllabes == 6 :
                                                    vers_phonetique_sanscouleur += "|"
                                                break
                                            elif (mot[-1] == "s" or mot[-1] == "x") and liste_mots_vers[0][0] in voyelles :
                                                vers_phonetique_sanscouleur += phonetique + "z"
                                                for lettre in phonetique :
                                                    if lettre in voyelles_sampa :
                                                        nb_syllabes += 1
                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                if nb_syllabes == 6 :
                                                    vers_phonetique_sanscouleur += "|"
                                                break
                                            
                                            #Règles pour les liasons "-t"
                                            elif (mot[-1] == "t" or mot[-1] == "d") and liste_mots_vers[0][0] in voyelles :
                                                vers_phonetique_sanscouleur += phonetique + "t"
                                                for lettre in phonetique :
                                                    if lettre in voyelles_sampa :
                                                        nb_syllabes += 1
                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                if nb_syllabes == 6 :
            
                                                    vers_phonetique_sanscouleur += "|"
                                                break
                                            
                                        #Transcription simple 
            
                                        vers_phonetique_sanscouleur += phonetique
                                        for lettre in phonetique :
                                            if lettre in voyelles_sampa :
                                                nb_syllabes += 1
                                        if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                            nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                        if nb_syllabes == 6 :
            
                                            vers_phonetique_sanscouleur += "|"
                                        break
    
                    print(vers_propre + "," + vers_phonetique_sanscouleur + "," + str(nb_syllabes) )
                            
                    correction.write(vers_propre + "," + vers_phonetique_sanscouleur + "," + str(nb_syllabes) + "\n")
                        

            



        


            
transcription("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_baudelaire.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_baudelaire.csv")
transcription("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_hugo.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_hugo.csv")
transcription("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_musset.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_musset.csv")
transcription("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_lamartine.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_lamartine.csv")