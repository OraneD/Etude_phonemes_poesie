#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:21:29 2023

@author: orane
"""

import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np
import os
from tabulate import tabulate

print(os.getcwd())

liste_phonemes = ["a", "A", "b", "C", "k", "d", "e", "E", "f", "g", "H", "i", "j", "J", "t", "Z", "z", "e~", "w", "@", "s", "R", "2", "u", "y", "o", "O", "9", "v", "m", "n", "N", "S"]
liste_e = ["@", "2", "9"]
liste_o = ["o", "O"]
liste_nasales = ["A", "C"]
liste_i = ["e", "i"]
liste_voyelles = ["a", "@", "2", "9", "o", "O", "e", "E", "u", "y", "i", "e~", "A", "C"]
liste_voyelles_dico = ["a", "@", "o", "E", "u", "y", "i, e", "e~", "A, C"]
#Pourcentage par phonème
def stats_phonemes(fichier):
                dico_voyelles = {}
                for voyelle in liste_voyelles_dico :
                    dico_voyelles[voyelle] = 0
    
                with open(fichier, "r") as filecsv:
                    print(fichier)
                    csvreader = csv.reader(filecsv)
                    for row in csvreader :
                        if row[2] == "12":
                            for phoneme in liste_voyelles :
                                if  phoneme in liste_e and len(re.findall(phoneme, row[1])) != 0 :
                                    dico_voyelles["@"] += len(re.findall(phoneme, row[1]))
                                elif  phoneme in liste_o and len(re.findall(phoneme, row[1])) != 0 :
                                    dico_voyelles["o"] += len(re.findall(phoneme, row[1]))
                                elif  phoneme in liste_nasales and len(re.findall(phoneme, row[1])) != 0 :
                                    dico_voyelles["A, C"] += len(re.findall(phoneme, row[1]))
                                elif  phoneme in liste_i and len(re.findall(phoneme, row[1])) != 0 :
                                    dico_voyelles["i, e"] += len(re.findall(phoneme, row[1]))
                                elif  len(re.findall(phoneme, row[1])) != 0 :
                                    dico_voyelles[phoneme] += len(re.findall(phoneme, row[1]))

                                    

                print(dico_voyelles)
                names = list(dico_voyelles.keys())
                values = [round((v / sum(dico_voyelles.values())) * 100, 2) for v in dico_voyelles.values()]
                return names, values


                
Nhugo, Vhugo = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/hugo_corrig.csv")
Nbaudelaire, Vbaudelaire = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/baudelaire_corrig.csv")
Nmusset, Vmusset = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/musset_corrig.csv")
Nlamartine, Vlamartine = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/lamartine_corrig.csv")


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

plt.ylim(0,35)
plt.ylabel("%")
plt.title("Pourcentage de chaque voyelle (parmi toutes les voyelles)")

plt.xticks(ind+width, Nhugo)

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
    with open("../../resultats/statistique/tableaux.txt", "a") as tab :
        tab.write("----- Pourcentage voyelles par auteur (corpus vers) ----- \n \n")
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

camembert(Nhugo, Vhugo, "Répartition voyelles pour Hugo")
camembert(Nbaudelaire, Vbaudelaire, "Répartition voyelles pour Baudelaire")
camembert(Nmusset, Vmusset, "Répartition voyelles pour Musset")
camembert(Nlamartine, Vlamartine, "Répartition voyelles pour Lamartine")

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
    plt.ylim(0,35)
    plt.title("Pourcentage voyelles sur l'ensemble du corpus")
    plt.show()
    
    plt.figure(figsize = (8,8))
    plt.pie(valeurs_tous, 
            labels = Nhugo, 
            normalize = True, 
            autopct = '%1.1f%%',
            #pctdistance = 0.7, labeldistance = 1.4,
            shadow = True)
    plt.title("Pourcentage voyelles sur l'ensemble du corpus")

    plt.show()
    data = [valeurs_tous]
    head = [x for x in Nhugo]
    print(tabulate(data, headers = head, tablefmt="fancy_grid", showindex="always"))
    with open("../../resultats/statistique/tableaux.txt", "a") as tab :
         tab.write("------ Pourcentage voyelles sur l'ensemble du corpus (corpus vers) ------- \n \n")
         tab.write(tabulate(data, headers = head, tablefmt="fancy_grid", showindex="always"))
    

    
histogramme_sup(Vhugo, Vbaudelaire, Vmusset, Vlamartine)