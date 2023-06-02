#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:23:21 2023

@author: orane
"""

import xml.etree.ElementTree as ET
import re
from pathlib import Path
from termcolor import colored
import pandas as pd 
from tabulate import tabulate
from ansi2html import Ansi2HTMLConverter
import csv
import time

start_time = time.time()

def transcription(corpusPath, stats_auteur) : 
    diereses = pd.read_csv("diereses.txt")
    
    #Listes pour le dataframe en sortie
    syllabes = []
    liste_vers = []
    liste_vers_phonetique = []
    liste_vers_phonetique_sanscouleur = []
    ######################################
    
    #Listes pour les règles 
    voyelles_sampa = ["i", "e", "E", "a", "A", "O", "o", "u", "y", "2", "9", "@", "e~", "a~", "o~", "9~", "C", "H", "j","w"]
    voyelles = ["a", "e", "i", "o", "u", "y", "é", "è","à"]
    pattern = re.compile("^h[aeiouyéèà]{2}") #Tentative de règle pour les h aspirés, voir dans la boucle
    #######################################
    
    #Variables pour évaluer le script
    nb_vers = 0
    nb_vers_bon = 0
    liste_mots_inconnus = []
    evaluation_poemes = []
    ######################################

        
    
    corpus_dir = corpusPath
    
    for fichier in corpus_dir.iterdir():
        if fichier.name.endswith(".xml") :
            tree = ET.parse(fichier)
            root = tree.getroot()
            for div in root.findall('.//{http://www.tei-c.org/ns/1.0}div') :
                if div.get("type") == "poem" :
                    with open(stats_auteur, "r") as csvfile :
                        obj = csv.DictReader(csvfile, delimiter="\t")
                        for dico in obj :
                            if div.get("key") == dico["ID_POEME"] and dico["LM"] == "12" :
                                print()
                                print("#################################")
                                print()
                                id_poem = div.get("key")
                                for vers in div.findall('.//{http://www.tei-c.org/ns/1.0}l') :
                                    if vers.text == None :
                                        continue
                                    remplacement_apo = re.sub(r"’", "'", vers.text)
                                    vers_propre = re.sub(r"[^\w\s\'’-]", "", remplacement_apo).lower()
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
                                    vers_phonetique = ""
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
                                                            if (len(mot) > 3 or mot == "une") and (mot[-1] == "e" or mot[-2:] == "es") and (liste_mots_vers[0])[0] not in voyelles and liste_mots_vers[0][0] != "h" and phonetique[-1] != "@":
                                                                vers_phonetique += phonetique + colored("@","green") + " "
                                                                vers_phonetique_sanscouleur += phonetique + "@"
                                                                for lettre in phonetique :
                                                                    if lettre in voyelles_sampa :
                                                                        nb_syllabes += 1
                                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                                nb_syllabes += 1
                                                                if nb_syllabes == 6 :
                                                                    vers_phonetique += " | " 
                                                                    vers_phonetique_sanscouleur += "|"
                                                                break
                                                            
                                                            #Règles pour les "h" aspirés
                                                            elif (len(mot) > 3 or mot == "une") and (mot[-1] == "e" or mot[-2:] == "es") and liste_mots_vers[0][0] == "h" :
                                                                if pattern.match(liste_mots_vers[0][0:3]) == None :
                                                                    vers_phonetique += phonetique +  " "
                                                                    vers_phonetique_sanscouleur += phonetique
                                                                    for lettre in phonetique :
                                                                        if lettre in voyelles_sampa :
                                                                            nb_syllabes += 1
                                                                    if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                                        nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                                    break
                                                                    if nb_syllabes == 6 :
                                                                        vers_phonetique += " | "
                                                                        vers_phonetique_sanscouleur += "|"
                                                                else :
                                                                    vers_phonetique += phonetique + colored("@","green") + " "
                                                                    vers_phonetique += phonetique + "@"
                                                                    for lettre in phonetique :
                                                                        if lettre in voyelles_sampa :
                                                                            nb_syllabes += 1
                                                                    if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                                        nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                                    nb_syllabes += 1
                                                                    if nb_syllabes == 6 :
                                                                        vers_phonetique += " | "
                                                                    break
                                                                
                                                            #Règles pour les liasions - "s"
                                                            elif len(mot) > 3 and mot[-2:] == "es" and liste_mots_vers[0][0] in voyelles :
                                                                vers_phonetique += phonetique + colored("@","green") + colored("z", "red") + " "
                                                                vers_phonetique_sanscouleur += phonetique + "@" +"z"
                                                                for lettre in phonetique :
                                                                    if lettre in voyelles_sampa :
                                                                        nb_syllabes += 1
                                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                                nb_syllabes += 1
                                                                if nb_syllabes == 6 :
                                                                    vers_phonetique += " | "
                                                                    vers_phonetique_sanscouleur += "|"
                                                                break
                                                            elif (mot[-1] == "s" or mot[-1] == "x") and liste_mots_vers[0][0] in voyelles :
                                                                vers_phonetique += phonetique + colored("z", "red") + " "
                                                                vers_phonetique_sanscouleur += phonetique + "z"
                                                                for lettre in phonetique :
                                                                    if lettre in voyelles_sampa :
                                                                        nb_syllabes += 1
                                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                                if nb_syllabes == 6 :
                                                                    vers_phonetique += " | "
                                                                    vers_phonetique_sanscouleur += "|"
                                                                break
                                                            
                                                            #Règles pour les liasons "-t"
                                                            elif (mot[-1] == "t" or mot[-1] == "d") and liste_mots_vers[0][0] in voyelles :
                                                                vers_phonetique += phonetique + colored("t", "blue") + " "
                                                                vers_phonetique_sanscouleur += phonetique + "t"
                                                                for lettre in phonetique :
                                                                    if lettre in voyelles_sampa :
                                                                        nb_syllabes += 1
                                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                                if nb_syllabes == 6 :
                                                                    vers_phonetique += " | "
                                                                    vers_phonetique_sanscouleur += "|"
                                                                break
                                                            
                                                        #Transcription simple 
                                                        vers_phonetique += phonetique + " "
                                                        vers_phonetique_sanscouleur += phonetique
                                                        for lettre in phonetique :
                                                            if lettre in voyelles_sampa :
                                                                nb_syllabes += 1
                                                        if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                            nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                        if nb_syllabes == 6 :
                                                            vers_phonetique += " | "
                                                            vers_phonetique_sanscouleur += "|"
                                                        break
                                                    
                                                #Si on trouve pas le mot dans le dictionnaire :
                                                elif line[0] == "*" : 
                                                    vers_phonetique += "XXXX "
                                                    if mot not in liste_mots_inconnus :
                                                        liste_mots_inconnus.append(mot)
                                                    break
                
                                    if nb_syllabes == 12 :
                                        nb_vers_bon += 1
                                    nb_vers += 1
                                    
                                    liste_vers.append(vers_propre.strip("\n"))
                                    liste_vers_phonetique.append(vers_phonetique)
                                    liste_vers_phonetique_sanscouleur.append(vers_phonetique_sanscouleur)
                                    syllabes.append(nb_syllabes)
                                    print(vers_propre, vers_phonetique, nb_syllabes)
                                    print()
                                        
            print("----MOTS INCONNUS------")    
            print(len((liste_mots_inconnus)))
            print(liste_mots_inconnus)
            with open("mots_inconnus_transcriptions.txt", "w") as file :
                for mot in liste_mots_inconnus :
                    file.write(mot + "\n")

            print("----EVALUATION----")
            print("Pourcentage pars vers :")
            print((nb_vers_bon / nb_vers)* 100)

            return liste_vers, liste_vers_phonetique, syllabes, liste_vers_phonetique_sanscouleur
    
               
liste_vers, liste_vers_phonetique, syllabes, liste_vers_phonetique_sans_couleur = transcription(Path("../Corpus/LaMartine"),Path("../Corpus/LaMartine/analyse_CM_profils_Lamartine.csv")   )     

end_time = time.time()
print(end_time - start_time)

def resultats_html(vers, vers_phonetique, syllabes, nomfichier) :          
    df_poeme = pd.DataFrame()
    df_poeme["vers"] = vers
    df_poeme["vers_phonetique"] = vers_phonetique
    df_poeme["syllabes"] = syllabes
    print(tabulate(df_poeme, headers='keys', tablefmt='psql'))
    #CONVERSION AU FORMAT HTML
    #html = df_poeme.to_html()
   #conv = Ansi2HTMLConverter()
    #html_conv = html = conv.convert(html)
    #text_file = open(nomfichier, "w")
    #text_file.write(html_conv)
    #text_file.close()
    
resultats_html(liste_vers, liste_vers_phonetique, syllabes, "lamartine.html")

def resultats_csv(vers, vers_phonetique_sanscouleur, syllabes, nomfichier) :
    with open(nomfichier, "w") as csvfile :
        colonnes = ["Vers", "Phonétique", "Syllabes"]
        objet = csv.writer(csvfile)
        objet.writerow(colonnes)
        c = zip(vers, vers_phonetique_sanscouleur, syllabes)
        objet.writerows(c)

    
resultats_csv(liste_vers, liste_vers_phonetique_sans_couleur, syllabes, Path("../resultats/csv_transcriptions/lamartine.csv"))







