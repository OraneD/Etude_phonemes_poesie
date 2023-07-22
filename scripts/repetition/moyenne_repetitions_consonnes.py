#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:01:52 2023

@author: orane
"""


import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate



liste_e = ["@", "2", "9"]
liste_o = ["o", "O"]
liste_voyelles = ["a", "@", "2", "9", "o", "O", "e", "E", "u", "y", "i", "e~", "A", "C"]
liste_consonnes =  ["p", "t", "k", "f", "s", "S","b", "d", "g", "v", "z", "j", "l","R", "n", "m", "w", "H", "Z"]
liste_voyelles_dico = ["a", "@", "o", "e", "E", "u", "y", "i", "e~", "A", "C"]

class Repetition :
    def __init__(self, occurrences, compte) :
        self.occurrences = occurrences
        self.compte = compte
        
class Phonemes:
    
    def __init__(self, phoneme, repetition) :
        self.phoneme = phoneme
        self.repetition = repetition
        

        

#for consonne in liste_consonnes_couple :
    #for num in range(1,7) :
        #lst_class.append(Phonemes(consonne, Repetition(num, 0)))
        
#print(lst_class)

#for phoneme in lst_class :
    #print(phoneme.phoneme, phoneme.repetition.occurrences, phoneme.repetition.compte)

lst_class = []
def stats_phonemes(fichier, nb):
                    
                    rep_consonnes = {"2" : 0, "3":0, "4":0}

                    with open(fichier, "r") as filecsv:
                        csvreader = csv.reader(filecsv)
                        for row in csvreader :
                            if row[2] == "12":
                                for phoneme in liste_consonnes :
                                    if  len(re.findall(phoneme, row[1])) == 2 :
                                        rep_consonnes["2"] += 1
                                    elif len(re.findall(phoneme,row[1])) == 3 :
                                        rep_consonnes["3"] += 1
                                    elif len(re.findall(phoneme, row[1])) == 4 :
                                        rep_consonnes["4"] += 1
                                #for phoneme in liste_consonnes :
                                   # if len(re.findall(phoneme, row[1])) > 1 :
                                       # consonnes_rep += 1
                    names = [k for k in rep_consonnes.keys()]
                    values = [round(v / nb, 2) for v in rep_consonnes.values()]

        
                    return names, values

Nhugo, Vhugo = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/hugo_corrig.csv", 27693)
Nbaudelaire, Vbaudelaire = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/baudelaire_corrig.csv", 2790)
Nmusset, Vmusset = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/musset_corrig.csv", 7231)
Nlamartine, Vlamartine = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/lamartine_corrig.csv", 16018)




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
    
    
    plt.ylabel("Moyenne")
    plt.title("Moyenne des occurrences de consonnes par vers")
    plt.xlabel("Occurrences")
    
    plt.xticks(ind+width, Nhugo)
    
    plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
    plt.show()
    data = [
             [str(x)  for x in xvals],
             [str(y)  for y in yvals],
             [str(z)  for z in zvals],
             [str(u)  for u in uvals]
           ]
    header = [x for x in Nhugo]
    print(tabulate(data, headers = header, tablefmt="fancy_grid", showindex="always"))
    with open("../../resultats/statistique/tableaux.txt", "a") as tab :
        tab.write("----- MOyenne des occurrences de consonnes par vers ----- \n \n")
        tab.write(tabulate(data, headers = header, tablefmt="fancy_grid", showindex="always"))

histogramme(Vhugo, Vbaudelaire, Vmusset, Vlamartine)