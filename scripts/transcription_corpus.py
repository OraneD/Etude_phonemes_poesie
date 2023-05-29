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
diereses = pd.read_csv("diereses.txt")

#Listes pour le dataframe en sortie
syllabes = []
liste_vers = []
liste_vers_phonetique = []

voyelles_sampa = ["i", "e", "E", "a", "A", "O", "o", "u", "y", "2", "9", "@", "e~", "a~", "o~", "9~", "C", "H", "j","w"]
voyelles = ["a", "e", "i", "o", "u", "y", "é", "è","à"]
pattern = re.compile("^h[aeiouyéèà]{2}")

nb_vers = 0
nb_vers_bon = 0
liste_mots_inconnus = []


corpus_dir = Path("../Corpus/Baudelaire")

for fichier in corpus_dir.iterdir():
    if fichier.name.endswith(".xml") :
        tree = ET.parse(fichier)
        root = tree.getroot()
        for div in root.findall('.//{http://www.tei-c.org/ns/1.0}div') :
            if div.get("type") == "poem" :
                print()
                print("#################################")
                print()
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
                    longueur_vers = len(liste_mots_vers)
                    nb_syllabes = 0
                    while longueur_vers > 0 :
                        mot = liste_mots_vers[0]
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
                                                for lettre in phonetique :
                                                    if lettre in voyelles_sampa :
                                                        nb_syllabes += 1
                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                nb_syllabes += 1
                                                if nb_syllabes == 6 :
                                                    vers_phonetique += " | "
                                                    
                                                break
                                            elif (len(mot) > 3 or mot == "une") and (mot[-1] == "e" or mot[-2:] == "es") and liste_mots_vers[0][0] == "h" :
                                                if pattern.match(liste_mots_vers[0][0:3]) == None :
                                                    vers_phonetique += phonetique +  " "
                                                    for lettre in phonetique :
                                                        if lettre in voyelles_sampa :
                                                            nb_syllabes += 1
                                                    if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                        nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                    break
                                                    if nb_syllabes == 6 :
                                                        vers_phonetique += " | "
                                                else :
                                                    vers_phonetique += phonetique + colored("@","green") + " "
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
                                                for lettre in phonetique :
                                                    if lettre in voyelles_sampa :
                                                        nb_syllabes += 1
                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                nb_syllabes += 1
                                                if nb_syllabes == 6 :
                                                    vers_phonetique += " | "
                                                break
                                            elif (mot[-1] == "s" or mot[-1] == "x") and liste_mots_vers[0][0] in voyelles :
                                                vers_phonetique += phonetique + colored("z", "red") + " "
                                                for lettre in phonetique :
                                                    if lettre in voyelles_sampa :
                                                        nb_syllabes += 1
                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                if nb_syllabes == 6 :
                                                    vers_phonetique += " | "
                                                break
                                            #Règles poyr les liasons "-t"
                                            elif (mot[-1] == "t" or mot[-1] == "d") and liste_mots_vers[0][0] in voyelles :
                                                vers_phonetique += phonetique + colored("t", "blue") + " "
                                                for lettre in phonetique :
                                                    if lettre in voyelles_sampa :
                                                        nb_syllabes += 1
                                                if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                                    nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                                if nb_syllabes == 6 :
                                                    vers_phonetique += " | "
                                                break

                                            
                                                
                                                        
                                        vers_phonetique += phonetique + " "
                                        for lettre in phonetique :
                                            if lettre in voyelles_sampa :
                                                nb_syllabes += 1
                                        if len(re.findall("[Hjw]", phonetique)) > 0 and mot not in list(diereses["forme"])  :
                                            nb_syllabes -= len(re.findall("[Hjw]", phonetique))
                                        if nb_syllabes == 6 :
                                            vers_phonetique += " | "
                                            
                                        break
                                elif line[0] == "*" : 
                                    vers_phonetique += "XXXX " #Si le mot ne figure pas dans le dictionnaire, on le signale
                                    if mot not in liste_mots_inconnus :
                                        liste_mots_inconnus.append(mot)
                                    break

                    if nb_syllabes == 12 :
                        nb_vers_bon += 1
                    nb_vers += 1
                    liste_vers.append(vers_propre.strip("\n"))
                    liste_vers_phonetique.append(vers_phonetique)
                    syllabes.append(nb_syllabes)
                    print(vers_propre, vers_phonetique, nb_syllabes)
                    print()
    
print((liste_mots_inconnus))
with open("mots_inconnus_transcriptions.txt", "w") as file :
    for mot in liste_mots_inconnus :
        file.write(mot + "\n")
    
            
                    
            #df_poeme = pd.DataFrame()
            #df_poeme["vers"] = liste_vers
            #df_poeme["vers_phonetique"] = liste_vers_phonetique
            #df_poeme["syllabes"] = syllabes
            #print(tabulate(df_poeme, headers='keys', tablefmt='psql'))
            #print("----------ÉVALUATION-----------")
            #print(nb_vers_bon / nb_vers * 100)
        
