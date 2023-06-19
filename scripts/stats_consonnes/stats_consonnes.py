#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:39:46 2023

@author: orane
"""

import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np

liste_phonemes = ["a", "A", "b", "C", "k", "d", "e", "E", "f", "g", "H", "i", "j", "J", "t", "Z", "z", "e~", "w", "@", "s", "R", "2", "u", "y", "o", "O", "9", "v", "m", "n", "N", "S"]
liste_consonnes_sourdes = ["p", "t", "k", "f", "s" "S"]
liste_consonnes_sonores = ["b", "d", "g", "v", "z" "j", "l","R", "n" "N", "m"]
#Pourcentage par phonème
def stats_phonemes(fichier):

                dico_consonnes = {"sourdes" : 0, "sonores" : 0}
                nb_pho_total = 0
                nb_sourde = 0
                nb_sonore = 0
    
                with open(fichier, "r") as filecsv:
                    print(fichier)
                    csvreader = csv.reader(filecsv)
                    for row in csvreader :
                        if row[2] == "12":
                            for phoneme in liste_phonemes :
                                if phoneme in liste_consonnes_sourdes  and len(re.findall(phoneme, row[1])) != 0 :
                                    dico_consonnes["sourdes"] += len(re.findall(phoneme, row[1]))
                                    nb_pho_total += len(re.findall(phoneme, row[1]))
                                elif phoneme in liste_consonnes_sonores and len(re.findall(phoneme, row[1])) != 0 :
                                    dico_consonnes["sonores"] += len(re.findall(phoneme, row[1]))
                                    nb_pho_total += len(re.findall(phoneme, row[1]))
                                elif len(re.findall(phoneme, row[1])) != 0 :
                                    nb_pho_total += len(re.findall(phoneme, row[1]))
                                    
    
                names = list(dico_consonnes.keys())
                values = [round((v / nb_pho_total) * 100, 2) for v in dico_consonnes.values()]
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
plt.title("Pourcentage de chaque type de consonne (parmi tous les phonèmes)")

plt.xticks(ind+width, Nhugo)

plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
plt.show()