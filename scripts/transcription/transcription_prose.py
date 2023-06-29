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
        texte_propre = vers_propre = re.sub(r"[^\w\s\'’-]", "", texte).lower().strip("-").strip("'")
        for mot in texte_propre.split(" ") :
            with open("dico1.txt", "r") as dico :
                lignes = dico.readlines()
                for ligne in lignes :
                    entry = ligne.split("\t")[0]
                    phonetique = ligne.split("\t")[1]
                    
                    if mot == ("\n") :
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
