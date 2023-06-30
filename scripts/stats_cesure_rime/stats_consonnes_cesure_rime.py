#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 04:06:14 2023

@author: orane
"""

import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np
import os
print(os.getcwd())
liste_phonemes = ["a", "A", "b", "C", "k", "d", "e", "E", "f", "g", "H", "i", "j", "J", "t", "Z", "z", "e~", "w", "@", "s", "R", "2", "u", "y", "o", "O", "9", "v", "m", "n", "N", "S"]
liste_consonnes_sourdes = ["p", "t", "k", "f", "s" "S"]
liste_consonnes_sonores = ["b", "d", "g", "v", "z" "j", "l","R", "n" "N", "m"]
couple_k_g = ["k", "g"]
couple_f_v = ["f", "v"]
couple_p_b_m = ["p", "b", "m"]
couple_s_z = ["s", "z"]
couple_S_Z = ["S", "Z"]
couple_t_d = ["t", "d"]
liste_consonnes =  ["p", "t", "k", "f", "s", "S","b", "d", "g", "v", "z", "j", "l","R", "n", "N", "m", "w", "H"]


def stats_consonnes_six_douze(fichier):

                dico_consonnes = {"k, g" : 0, "f, v" : 0, "H" : 0, "s, z" : 0, "S, Z" : 0, "R" : 0, "l" : 0, "j" : 0,"p, b, m" : 0, "w" : 0, "t, d" : 0, "n" : 0}

                with open(fichier, "r") as filecsv:
                    print(fichier)
                    csvreader = csv.reader(filecsv)
                    for row in csvreader :
                        if row[0] == "Syllabe" :
                            continue
                        for phoneme in liste_consonnes :
                            if phoneme in couple_k_g  and len(re.findall(phoneme, row[0])) != 0 :
                                dico_consonnes["k, g"] += int(row[1])
                                
                            elif phoneme in couple_f_v and len(re.findall(phoneme, row[0])) != 0 :
                                dico_consonnes["f, v"] += int(row[1])
                                
                            elif phoneme in couple_p_b_m and len(re.findall(phoneme, row[0])) != 0 :
                                dico_consonnes["p, b, m"] += int(row[1])
                                
                            elif phoneme in couple_s_z and len(re.findall(phoneme, row[0])) != 0 :
                                dico_consonnes["s, z"] += int(row[1])
                                
                            elif phoneme in couple_S_Z and len(re.findall(phoneme, row[0])) != 0 :
                                dico_consonnes["S, Z"] += int(row[1])
                            
                            elif phoneme in couple_t_d and len(re.findall(phoneme, row[0])) != 0 :
                                dico_consonnes["t, d"] += int(row[1])
                                 
                            elif len(re.findall(phoneme, row[0])) != 0 :
                                dico_consonnes[phoneme] += int(row[1])
                                    
    
                names = list(dico_consonnes.keys())
                values = [round((v / sum(dico_consonnes.values())) * 100, 2) for v in dico_consonnes.values()]
                return names, values

    
                
Nhugo, Vhugo = stats_consonnes_six_douze("../../resultats/statistique/rime_cesure/csv/hugo_syllabe_cesure_rime.csv")
Nbaudelaire, Vbaudelaire = stats_consonnes_six_douze("../../resultats/statistique/rime_cesure/csv/baudelaire_syllabe_cesure_rime.csv")
Nmusset, Vmusset = stats_consonnes_six_douze("../../resultats/statistique/rime_cesure/csv/musset_syllabe_cesure_rime.csv")
Nlamartine, Vlamartine = stats_consonnes_six_douze("../../resultats/statistique/rime_cesure/csv/lamartine_syllabe_cesure_rime.csv")

def histogramme(x, y, z, u) :
    N = 4
    ind = np.arange(len(Nhugo))
    width = 0.20
    
    xvals = x
    bar1= plt.bar(ind, xvals, width, color = "tab:blue")
    
    yvals = y
    bar2 = plt.bar(ind + width, yvals, width, color = "tab:orange")
    
    zvals = z
    bar3 = plt.bar(ind+width*2, zvals, width, color = "tab:green")
    
    uvals = u
    bar4 = plt.bar(ind+width*3, uvals, width, color = "tab:red")
    
    
    plt.ylabel("%")
    plt.title("Pourcentage consonnes positions 6 et 12 (parmi toutes les consonnes)")
    
    plt.xticks(ind+width, Nhugo)
    
    plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
    plt.show()

histogramme(Vhugo, Vbaudelaire, Vmusset, Vlamartine)

def camembert(labels, valeurs, titre) :
    plt.figure(figsize = (8,8))
    plt.pie(valeurs, 
            labels = labels, 
            normalize = True, 
            autopct = '%1.1f%%',
            #pctdistance = 0.7, labeldistance = 1.4,
            shadow = True)
    plt.title(titre, fontsize=14)
    plt.show()

camembert(Nhugo, Vhugo, "Répartition consonnes positions 6 et 12 pour Hugo")
camembert(Nbaudelaire, Vbaudelaire, "Répartition consonnes positions 6 et 12 pour Baudelaire")
camembert(Nmusset, Vmusset, "Répartition consonnes positions 6 et 12 pour Musset")
camembert(Nlamartine, Vlamartine, "Répartition consonnes positions 6 et 12 pour Lamartine")

def histogramme_sup(x1, x2, x3, x4) :
    
    valeurs_tous = []
    
    for i in range(len(x1)) :
        j = 0
        j += round((x1[i] + x2[i] + x3[i] + x4[i])/4, 2)
        valeurs_tous.append(j)
    print(sum(valeurs_tous))
      
    plt.ylabel("%")
    width = 0.05
    ind = np.arange(len(Nhugo))
    plt.ylim(0,20)
    bar1= plt.bar(ind, valeurs_tous, color = "tab:blue")
    plt.xticks(ind+width, Nhugo)
    plt.title("Pourcentage consonnes positions 6 et 12 sur l'ensemble du corpus")
    plt.show()
    
    plt.figure(figsize = (8,8))
    plt.pie(valeurs_tous, 
            labels = Nhugo, 
            normalize = True, 
            autopct = '%1.1f%%',
            #pctdistance = 0.7, labeldistance = 1.4,
            shadow = True)
    plt.title("Pourcentage consonnes positions 6 et 12 sur l'ensemble du corpus")

    plt.show()
    
    

    
histogramme_sup(Vhugo, Vbaudelaire, Vmusset, Vlamartine)