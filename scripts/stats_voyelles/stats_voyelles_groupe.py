#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 13:47:47 2023

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
def stats_consonnes(fichier, voyelles):
    
                dico_voyelle = {}
                for voyelle in voyelles :
                    dico_voyelle[voyelle] = 0

    
                with open(fichier, "r") as filecsv:
                    print(fichier)
                    csvreader = csv.reader(filecsv)
                    for row in csvreader :
                        if row[2] == "12":
                            for voyelle in voyelles :
                                if  len(re.findall(voyelle, row[1])) != 0 :
                                    dico_voyelle[voyelle] += len(re.findall(voyelle, row[1]))

                                    
    
                names = list(dico_voyelle.keys())
                values = [round((v / sum(dico_voyelle.values())) * 100, 2) for v in dico_voyelle.values()]
                return names, values


                
Nhugo, Vhugo = stats_consonnes("../resultats/csv_transcriptions/hugo.csv", ["A", "C"])
Nbaudelaire, Vbaudelaire = stats_consonnes("../resultats/csv_transcriptions/baudelaire.csv", ["A", "C"])
Nmusset, Vmusset = stats_consonnes("../resultats/csv_transcriptions/musset.csv", ["A", "C"])
Nlamartine, Vlamartine = stats_consonnes("../resultats/csv_transcriptions/lamartine.csv", ["A", "C"])


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
plt.title("Pourcentage groupe de voyelles")

plt.xticks(ind+width, Nhugo)

plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
plt.show()