#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:54:00 2023

@author: orane
"""

import re 


def transcription_prose(fichier, output):
    
    transcription_phonetique = ""
    mots_inconnus = []
    #Listes pour les règles 
    voyelles_sampa = ["i", "e", "E", "a", "A", "O", "o", "u", "y", "2", "9", "@", "e~", "a~", "o~", "9~", "C", "H", "j","w"]
    voyelles = ["a", "e", "i", "o", "u", "y", "é", "è","à"]
    
    
    with open(fichier, "r") as f :
        texte = f.read()
        texte_remplacement_apostrophe = texte.replace("’", "'")
        texte_propre = re.sub(r"[^\.\?\!\w\s\'’-]", "", texte_remplacement_apostrophe).lower().strip("-").strip("'")
        liste_mots = texte_propre.split()
        longueur_txt = len(liste_mots)
        while longueur_txt > 0 :
            mot = liste_mots[0].strip("\n").strip("\xa0").strip(".").strip("?").strip("!")
            liste_mots = liste_mots[1:]
            longueur_txt = len(liste_mots)
            if "'" in mot :
                for part in mot.split("'") :
                    mot = part
            elif "-" in mot :
                for part in mot.split("-") :
                    mot = part
                    
            with open("dico1.txt", "r") as dico :
                lignes = dico.readlines()
                for ligne in lignes :
                    entry = ligne.split("\t")[0]
                    phonetique = ligne.split("\t")[1].strip("\n")
                    
                    if mot == ("\n") or mot == "." or mot == "?" or mot == "!":
                        transcription_phonetique += mot
                        break
                        
                    if mot.strip() == entry :
                        print(mot, entry)
                        
                        #Règles pour les liasions - "s"
                        if len(liste_mots) > 1 and (mot[-1] == "s" or mot[-1] == "x") and liste_mots[0][0] in voyelles :
                            transcription_phonetique += phonetique + "z"
                            break
                        
                        #Règles pour les liasons "-t"
                        elif  len(liste_mots) > 1 and (mot[-1] == "t" or mot[-1] == "d") and liste_mots[0][0] in voyelles :
                            transcription_phonetique += phonetique + "t"
                            break
 
                        else :
                            transcription_phonetique += phonetique.strip("\n")
                            break
                        
                    elif entry == "***" : 
                        transcription_phonetique += "XXXX "
                        if mot not in mots_inconnus :
                            mots_inconnus.append(mot)
                        break
    with open("mot_inconnus.txt", "w") as mi :
        for mot in mots_inconnus :
            mi.write(mot + "\n")
    
    with open(output, "w") as f :
        f.write(transcription_phonetique)
        
    print(str(fichier) + " transcrit")
    
                
        
        

#transcription_prose("../../Corpus/Baudelaire/baudelaire_ecole_utf8.txt", 
                    #"../../resultats/transcriptions_prose/baudelaire_prose.txt")

#transcription_prose("../../Corpus/Hugo/hugo_quot_utf8.txt",
                   # "../../resultats/transcriptions_prose/hugo_prose.txt")

#transcription_prose("../../Corpus/Musset/musset_dupuis_utf8.txt", 
                    #"../../resultats/transcriptions_prose/musset_prose.txt")

transcription_prose("../../Corpus/LaMartine/lamartine_destinees_utf8.txt",
                    "../../resultats/transcriptions_prose/lamartine_prose.txt")