#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:43:04 2023

@author: orane
"""

import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np

liste_phonemes = ["a", "A", "b", "C", "k", "d", "e", "E", "f", "g", "H", "i", "j", "J", "t", "Z", "z", "e~", "w", "@", "s", "R", "2", "u", "y", "o", "O", "9", "v", "m", "n", "N", "S"]
liste_e = ["@", "2", "9"]
liste_o = ["o", "O"]
liste_voyelles = ["a", "@", "2", "9", "o", "O", "e", "E", "u", "y", "i", "e~", "A", "C"]
liste_voyelles_dico = ["a", "@", "o", "e", "E", "u", "y", "i", "e~", "A", "C"]
liste_consonnes = ["p", "t", "k", "f", "s" "S", "b", "d", "g", "v", "z" "j", "l","R", "n" "N", "m"]
#Pourcentage par phonème
def stats_phonemes(fichier):
                dico_voyelles = {"voyelles" : 0, "consonnes" : 0}

    
                with open(fichier, "r") as filecsv:
                    print(fichier)
                    csvreader = csv.reader(filecsv)
                    for row in csvreader :
                        if row[2] == "12":
                            for phoneme in liste_phonemes :
                                if  phoneme in liste_voyelles and len(re.findall(phoneme, row[1])) != 0 :
                                    dico_voyelles["voyelles"] += len(re.findall(phoneme, row[1]))

                                elif  phoneme in liste_consonnes and len(re.findall(phoneme, row[1])) != 0 :
                                    dico_voyelles["consonnes"] += len(re.findall(phoneme, row[1]))



                                    
    
                names = list(dico_voyelles.keys())
                values = [round((v / sum(dico_voyelles.values())) * 100, 2) for v in dico_voyelles.values()]
                return names, values


                
Nhugo, Vhugo = stats_phonemes("../resultats/csv_transcriptions/hugo.csv")
Nbaudelaire, Vbaudelaire = stats_phonemes("../resultats/csv_transcriptions/baudelaire.csv")
Nmusset, Vmusset = stats_phonemes("../resultats/csv_transcriptions/musset.csv")
Nlamartine, Vlamartine = stats_phonemes("../resultats/csv_transcriptions/lamartine.csv")


N = 4
ind = np.arange(len(Nhugo))
width = 0.20

xvals = Vhugo
bar1= plt.bar(ind, xvals, width, color = "tab:blue")

yvals = Vbaudelaire
bar2 = plt.bar(ind + width, yvals, width, color = "tab:orange")

zvals = Vmusset
bar3 = plt.bar(ind+width*2, zvals, width, color = "tab:green")

uvals = Vlamartine
bar4 = plt.bar(ind+width*3, uvals, width, color = "tab:red")


plt.ylabel("%")
plt.title("Pourcentage voyelles et consonnes")

plt.xticks(ind+width, Nhugo)

plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
plt.show()