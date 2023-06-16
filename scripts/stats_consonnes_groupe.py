#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:57:06 2023

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
def stats_consonnes(fichier, consonnes):
    
                dico_consonne = {}
                for consonne in consonnes :
                    dico_consonne[consonne] = 0

    
                with open(fichier, "r") as filecsv:
                    print(fichier)
                    csvreader = csv.reader(filecsv)
                    for row in csvreader :
                        if row[2] == "12":
                            for consonne in consonnes :
                                if  len(re.findall(consonne, row[1])) != 0 :
                                    dico_consonne[consonne] += len(re.findall(consonne, row[1]))

                                    
    
                names = list(dico_consonne.keys())
                values = [round((v / sum(dico_consonne.values())) * 100, 2) for v in dico_consonne.values()]
                return names, values


                
Nhugo, Vhugo = stats_consonnes("../resultats/csv_transcriptions/hugo.csv", ["p", "b", "m"])
Nbaudelaire, Vbaudelaire = stats_consonnes("../resultats/csv_transcriptions/baudelaire.csv", ["p", "b", "m"])
Nmusset, Vmusset = stats_consonnes("../resultats/csv_transcriptions/musset.csv", ["p", "b", "m"])
Nlamartine, Vlamartine = stats_consonnes("../resultats/csv_transcriptions/lamartine.csv", ["p", "b", "m"])


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
plt.title("Pourcentage groupe de consonnes")

plt.xticks(ind+width, Nhugo)

plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
plt.show()