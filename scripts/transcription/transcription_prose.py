#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:54:00 2023

@author: orane
"""

import re 

def transcription_prose(fichier):
    
    transcription_phonetique = ""
    mots_inconnus = []
    
    
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
                    phonetique = ligne.split("\t")[1]
                    
                    if mot == ("\n") or mot == "." or mot == "?" or mot == "!":
                        transcription_phonetique += mot
                        break
                        
                    if mot.strip() == entry :
                        
                        print(mot, entry)
                        transcription_phonetique += phonetique.strip("\n")
                        break
                        
                    elif entry == "***" : 
                        transcription_phonetique += "XXXX "
                        if mot not in mots_inconnus :
                            mots_inconnus.append(mot)
                        break
    
    print(mots_inconnus)
    print(transcription_phonetique)
                
        
        
        

transcription_prose("../../Corpus/Baudelaire/baudelaire_ecole_utf8.txt")
