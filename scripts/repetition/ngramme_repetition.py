#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:10:26 2023

@author: orane
"""

import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np
import os

#print(os.getcwd())
#os.chdir("Etude_phonemes_poesie/scripts/stats_rime/")
#print(os.getcwd())

liste_phonemes = ["a", "A", "b", "C", "k", "d", "e", "E", "f", "g", "H", "i", "j", "J", "t", "Z", "z", "e~", "w", "@", "s", "R", "2", "u", "y", "o", "O", "9", "v", "m", "n", "N", "S"]
liste_e = ["@", "2", "9"]
liste_o = ["o", "O"]
liste_voyelles = ["a", "@", "2", "9", "o", "O", "e", "E", "u", "y", "i", "e~", "A", "C", "H", "j"]
liste_voyelles_dico = ["a", "@", "o", "e", "E", "u", "y", "i", "e~", "A", "C"]

liste_consonnes = ["p", "t", "k", "f", "s" ,"S","b", "d", "g", "v", "z" "j", "l","R", "n" "N", "m"]

regex_consonnes = "(p|t|k|f|s|S|b|d|g|v|z|j|l|R|n|N|m|Z|w|H)"
regex_voyelles = "(a|@|2|9|o|O|e|E|u|y|i|e~|A|C|H|j)"

regex = ( "(" + regex_consonnes + "?" + regex_voyelles + regex_consonnes + "?" + ")" )

def ngramme(string, n) :
        new_s = string.replace("|", "").replace("e~", "1")
        lst_ngramme = []
        for i in range(len(new_s)-n+1):
            ngramm = ""
            for j in range(n):
                ngramm += new_s[i + j]
            lst_ngramme.append(ngramm)
        return(lst_ngramme)


def stats_repetition(fichier):
                dico_cesure = {}
                nb_row = 0
    
                with open(fichier, "r") as filecsv:
                    print(fichier)
                    csvreader = csv.reader(filecsv)
                    for row in csvreader :
                        if row[2] == "12":
                            nb_row += 1
                            
                            ngramme_syllabe = (ngramme(row[1], 3))
                            lst_row = []
                            for syl in ngramme_syllabe :

                                if ngramme_syllabe.count(syl) > 2 and syl not in lst_row :
                                    print(row)
                                    print(syl, ngramme_syllabe.count(syl))
                                    lst_row.append(syl)
                            
                            
        



                
#Nhugo, Vhugo = stats_rime("../../resultats/csv_transcriptions/hugo.csv")
#Nbaudelaire, Vbaudelaire = stats_rime("../../resultats/csv_transcriptions/baudelaire.csv")
#Nmusset, Vmusset = stats_rime("../../resultats/csv_transcriptions/musset.csv")
stats_repetition("../../resultats/csv_transcriptions/lamartine.csv")


