#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 23:04:37 2023

@author: orane
"""
import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np

liste_phonemes = ["a", "A", "b", "C", "k", "d", "e", "E", "f", "g", "H", "i", "j", "J", "t", "Z", "z", "e~", "w", "@", "s", "R", "2", "u", "y", "o", "O", "9", "v", "m", "n", "N", "S", "p"]

#Pourcentage par phonème
def stats_phonemes(fichier):

                dico_stats = {}
                nb_pho_total = 0
                for phoneme in liste_phonemes :
                    dico_stats[phoneme] = 0
    
                with open(fichier, "r") as filecsv:
                    print(fichier)
                    csvreader = csv.reader(filecsv)
                    for row in csvreader :
                        if row[2] == "12":
                            for phoneme in liste_phonemes :
                                if len(re.findall(phoneme, row[1])) != 0 :
                                    dico_stats[phoneme] += len(re.findall(phoneme, row[1]))
                                    nb_pho_total += len(re.findall(phoneme, row[1]))
    

                names = list(dico_stats.keys())
                values = [round((v / nb_pho_total) * 100, 2) for v in dico_stats.values()]
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
plt.title("Pourcentage de chaque phonème")

plt.xticks(ind+width, Nhugo)

plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
plt.show()


