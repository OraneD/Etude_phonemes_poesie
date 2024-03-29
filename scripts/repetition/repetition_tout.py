#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:12:24 2023

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
couple_k_g = ["k" , "g"]
couple_f_v = ["f", "v"]
couple_p_b_m = ["p", "b", "m"]
couple_s_z = ["s", "z"]
couple_S_Z = ["S", "Z"]
couple_t_d = ["t", "d"]
liste_consonnes =  ["p", "t", "k", "f", "s", "S","b", "d", "g", "v", "z", "j", "l","R", "n", "N", "m", "w", "H"]
liste_voyelles = ["a", "@", "2", "9", "o", "O", "e", "E", "u", "y", "i", "e~", "A", "C"]

def compte_repetition(fichier, nb_vers, liste_pho) :

    dico_nb_rep = {2:0, 3:0, 4:0}
    with open(fichier, "r") as filecsv:
        print(fichier)
        csvreader = csv.reader(filecsv)
        for consonne in liste_pho :
            for row in csvreader :
                if row[2] == "12":
                    if len(re.findall(consonne, row[1])) == 2 :
                        dico_nb_rep[2] += 1
                    elif len(re.findall(consonne, row[1])) == 3 :
                        dico_nb_rep[3] += 1
                    elif len(re.findall(consonne, row[1])) == 4 :
                        dico_nb_rep[4] += 1


    
    #return [round((x/nb_vers) * 100, 2) for x in dico_nb_rep.values()] #return pourcentage
    return [v for v in dico_nb_rep.values()]
    
                    

nbHugo = compte_repetition("../../resultats/csv_transcriptions/corpus_corrige/hugo_corrig.csv", 27693, liste_voyelles)
nbBaudelaire = compte_repetition("../../resultats/csv_transcriptions/corpus_corrige/baudelaire_corrig.csv", 2790, liste_voyelles)
nbMusset = compte_repetition("../../resultats/csv_transcriptions/corpus_corrige/musset_corrig.csv", 7231, liste_voyelles)
nbLamartine = compte_repetition("../../resultats/csv_transcriptions/corpus_corrige/lamartine_corrig.csv", 16018, liste_voyelles)

names = [2, 3, 4]

N = 4
ind = np.arange(len(nbHugo))
width = 0.20

xvals = nbHugo
bar1= plt.bar(ind, xvals, width, color = "tab:blue")

yvals = nbBaudelaire
bar2 = plt.bar(ind + width, yvals, width, color = "tab:orange")

zvals = nbMusset
bar3 = plt.bar(ind+width*2, zvals, width, color = "tab:green")

uvals = nbLamartine
bar4 = plt.bar(ind+width*3, uvals, width, color = "tab:red")


plt.ylabel("occurrences")
plt.title("Répétitions voyelles par vers")
plt.xlabel("Répétitions")

plt.xticks(ind+width, names)
#plt.ylim(0,40)
plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
plt.show()

