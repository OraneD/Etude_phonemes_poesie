#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:04:24 2023

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

def compte_repetition(fichier, phoneme, nb_vers) :
    compte_nb_rep_deux = 0
    compte_nb_rep_trois = 0
    compte_nb_rep_quatre = 0
    compte_nb_rep_cinq = 0
    compte_nb_rep_six = 0
    with open(fichier, "r") as filecsv:
        print(fichier)
        csvreader = csv.reader(filecsv)
        for row in csvreader :
            if row[2] == "12":
                if len(re.findall(phoneme, row[1])) == 2 :
                    compte_nb_rep_deux += 1
                elif len(re.findall(phoneme, row[1])) == 3 :
                    compte_nb_rep_trois += 1
                elif len(re.findall(phoneme, row[1])) == 4 :
                    compte_nb_rep_quatre
                elif len(re.findall(phoneme, row[1])) == 5 :
                    compte_nb_rep_cinq
                elif len(re.findall(phoneme, row[1])) == 6 :
                    compte_nb_rep_six
    lst_nb = []
    lst_nb.append(compte_nb_rep_deux)
    lst_nb.append(compte_nb_rep_trois)
    lst_nb.append(compte_nb_rep_quatre)
    lst_nb.append(compte_nb_rep_cinq)
    lst_nb.append(compte_nb_rep_six)
    lst_pourcentage = []
    for nb in lst_nb :
        lst_pourcentage.append(round((nb / nb_vers) * 100, 2))
    
    return phoneme, lst_pourcentage
    
                    

phoneme, nbHugo = compte_repetition("../../resultats/csv_transcriptions/corpus_corrige/hugo_corrig.csv", "e", 27693)
phoneme, nbBaudelaire = compte_repetition("../../resultats/csv_transcriptions/corpus_corrige/baudelaire_corrig.csv", "e", 2790)
phoneme, nbMusset = compte_repetition("../../resultats/csv_transcriptions/corpus_corrige/musset_corrig.csv", "e", 7231)
phoneme, nbLamartine = compte_repetition("../../resultats/csv_transcriptions/corpus_corrige/lamartine_corrig.csv", "e", 16018)

names = ["2", "3", "4", "5", "6"]

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


plt.ylabel("Pourcentage de vers")
plt.title("Pourcentages de vers avec x occurrences du phoneme " + phoneme)
plt.xlabel("Occurrences")

plt.xticks(ind+width, names)
plt.ylim(0,40)
plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
plt.show()