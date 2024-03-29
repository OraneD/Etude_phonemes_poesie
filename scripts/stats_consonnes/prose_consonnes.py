#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 22:28:17 2023

@author: orane
"""

import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate 

liste_phonemes = ["a", "A", "b", "C", "k", "d", "e", "E", "f", "g", "H", "i", "j", "J", "t", "Z", "z", "e~", "w", "@", "s", "R", "2", "u", "y", "o", "O", "9", "v", "m", "n", "N", "S"]
liste_consonnes_sourdes = ["p", "t", "k", "f", "s" "S"]
liste_consonnes_sonores = ["b", "d", "g", "v", "z" "j", "l","R", "n" "N", "m"]
couple_k_g = ["k" , "g"]
couple_f_v = ["f", "v"]
couple_p_b_m = ["p", "b"]
couple_s_z = ["s", "z"]
couple_S_Z = ["S", "Z"]
couple_t_d = ["t", "d"]
liste_consonnes =  ["p", "t", "k", "f", "s", "S","b", "d", "g", "v", "z", "j", "l","R", "n", "N", "m", "w", "H"]
#Pourcentage par phonème
def stats_phonemes(fichier):

                dico_consonnes = {"k, g" : 0, "f, v" : 0, "H" : 0, "s, z" : 0, "S, Z" : 0, "R" : 0, "l" : 0, "j" : 0,"p, b" : 0, "w" : 0, "t, d" : 0, "n" : 0, "m" : 0}

                with open(fichier, "r") as file:
                    reader = file.read()
                    for phoneme in liste_consonnes :
                        if phoneme in couple_k_g  and len(re.findall(phoneme, reader)) != 0 :
                            dico_consonnes["k, g"] += len(re.findall(phoneme, reader))
                            
                        elif phoneme in couple_f_v and len(re.findall(phoneme, reader)) != 0 :
                            dico_consonnes["f, v"] += len(re.findall(phoneme, reader))
                            
                        elif phoneme in couple_p_b_m and len(re.findall(phoneme, reader)) != 0 :
                            dico_consonnes["p, b"] += len(re.findall(phoneme, reader))
                            
                        elif phoneme in couple_s_z and len(re.findall(phoneme, reader)) != 0 :
                            dico_consonnes["s, z"] += len(re.findall(phoneme, reader))
                            
                        elif phoneme in couple_S_Z and len(re.findall(phoneme, reader)) != 0 :
                            dico_consonnes["S, Z"] += len(re.findall(phoneme, reader))
                        
                        elif phoneme in couple_t_d and len(re.findall(phoneme, reader)) != 0:
                            dico_consonnes["t, d"] += len(re.findall(phoneme, reader))
                             
                        elif len(re.findall(phoneme, reader)) != 0 :
                            dico_consonnes[phoneme] += len(re.findall(phoneme, reader))
                            
    
                names = list(dico_consonnes.keys())
                values = [round((v / sum(dico_consonnes.values())) * 100, 2) for v in dico_consonnes.values()]
                return names, values


                
Nhugo, Vhugo = stats_phonemes("../../resultats/transcriptions_prose/hugo_prose.txt")
Nbaudelaire, Vbaudelaire = stats_phonemes("../../resultats/transcriptions_prose/baudelaire_prose.txt")
Nmusset, Vmusset = stats_phonemes("../../resultats/transcriptions_prose/musset_prose.txt")
Nlamartine, Vlamartine = stats_phonemes("../../resultats/transcriptions_prose/lamartine_prose.txt")


N = 4
ind = np.arange(len(Nhugo))
width = 0.20

xvals = Vhugo
bar1= plt.bar(ind, xvals, width, color = "black")

yvals = Vbaudelaire
bar2 = plt.bar(ind + width, yvals, width, color = "lightgrey")

zvals = Vmusset
bar3 = plt.bar(ind+width*2, zvals, width, color = "dimgrey")

uvals = Vlamartine
bar4 = plt.bar(ind+width*3, uvals, width, color = "whitesmoke")


plt.ylabel("%")
plt.title("Pourcentage de chaque consonne (prose)")

plt.xticks(ind+width, Nhugo)
plt.ylim(0,20)
plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
plt.show()


def table() :
    data = [
             [str(x) + "%" for x in xvals],
             [str(y) + "%" for y in yvals],
             [str(z) + "%" for z in zvals],
             [str(u)+ "%" for u in uvals]
           ]
    header = [x for x in Nhugo]
    print(tabulate(data, headers = header, tablefmt="fancy_grid", showindex="always"))
    with open("../../resultats/statistique/tableaux_fin.txt", "a") as tab :
        tab.write("----- Pourcentage Consonnes par auteur (corpus prose) ----- \n \n")
        tab.write(tabulate(data, headers = header, tablefmt="fancy_grid", showindex="always"))
        

table()


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

camembert(Nhugo, Vhugo, "Répartition consonnes pour Hugo (prose)")
camembert(Nbaudelaire, Vbaudelaire, "Répartition consonnes pour Baudelaire (prose)")
camembert(Nmusset, Vmusset, "Répartition consonnes pour Musset (prose)")
camembert(Nlamartine, Vlamartine, "Répartition consonnes pour Lamartine (prose)")

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
    bar1= plt.bar(ind, valeurs_tous, color = "tab:blue")
    plt.xticks(ind+width, Nhugo)
    plt.ylim(0,20)
    plt.title("Pourcentage consonnes l'ensemble du corpus (prose)")
    plt.show()
    
    plt.figure(figsize = (8,8))
    plt.pie(valeurs_tous, 
            labels = Nhugo, 
            normalize = True, 
            autopct = '%1.1f%%',
            #pctdistance = 0.7, labeldistance = 1.4,
            shadow = True)
    plt.title("Pourcentage consonnes sur l'ensemble du corpus (prose)")

    plt.show()
    data = [valeurs_tous]
    head = [x for x in Nhugo]
    print(tabulate(data, headers = head, tablefmt="fancy_grid", showindex="always"))
    with open("../../resultats/statistique/tableaux_fin.txt", "a") as tab :
         tab.write("------ Pourcentage Consonnes sur l'ensemble du corpus ------- \n \n")
         tab.write(tabulate(data, headers = head, tablefmt="fancy_grid", showindex="always"))
    

    
histogramme_sup(Vhugo, Vbaudelaire, Vmusset, Vlamartine)