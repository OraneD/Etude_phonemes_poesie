#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:10:27 2023

@author: orane
"""


import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np



liste_e = ["@", "2", "9"]
liste_o = ["o", "O"]
liste_voyelles = ["a", "@", "2", "9", "o", "O", "e", "E", "u", "y", "i", "e~", "A", "C"]
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
                    
                    dico_voyelles = {}
                    for voyelle in liste_voyelles_dico :
                        dico_voyelles[voyelle] = 0
                    with open(fichier, "r") as filecsv:
                        csvreader = csv.reader(filecsv)
                        for row in csvreader :
                            if row[2] == "12":
                                for phoneme in liste_voyelles :
                                    if  phoneme in liste_e and len(re.findall(phoneme, row[1])) == nb :
                                        dico_voyelles["@"] += 1
                                    elif  phoneme in liste_o and len(re.findall(phoneme, row[1])) == nb :
                                        dico_voyelles["o"] += 1
                                    elif  len(re.findall(phoneme, row[1])) == nb:
                                        dico_voyelles[phoneme] += 1

                    for key, value in dico_voyelles.items() :
                        lst_class.append(Phonemes(key, Repetition(nb, value)))
                    return lst_class


#for phoneme in lst_class :
   # print("###########")
   # print(phoneme.phoneme, phoneme.repetition.occurrences, phoneme.repetition.compte)
                


for num in range(6) :
    pho_hugo = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/hugo_corrig.csv", num)
    
lst_class = []
  
for num in range(6)  :
    pho_baudelaire = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/baudelaire_corrig.csv", num)
    
lst_class = []

for num in range(6) :
    pho_musset = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/musset_corrig.csv", num)

lst_class = []

for num in range(6) :
    pho_lamartine = stats_phonemes("../../resultats/csv_transcriptions/corpus_corrige/lamartine_corrig.csv", num)


    
def moyenne_phoneme(lst_phoneme, nb_vers) :
    dico_voyelles = {}
    for voyelle in liste_voyelles_dico :
        dico_voyelles[voyelle] = 0

    for voyelle in liste_voyelles_dico :
        c = 0
        for phoneme in lst_phoneme :
            if voyelle == phoneme.phoneme :
               # print(phoneme.phoneme, phoneme.repetition.occurrences, phoneme.repetition.compte)
                c += phoneme.repetition.occurrences * phoneme.repetition.compte
        dico_voyelles[voyelle] += round(c / nb_vers, 2)
        
        
        
    return(dico_voyelles)
    
dico_hugo = moyenne_phoneme(pho_hugo,27693 )
dico_baudelaire = moyenne_phoneme(pho_baudelaire, 2790)
dico_musset = moyenne_phoneme(pho_musset, 7231)
dico_lamartine = moyenne_phoneme(pho_lamartine, 16018)


print(dico_hugo)
print(dico_baudelaire)
print(dico_musset)
print(dico_lamartine)



    
names = [k for k in dico_hugo.keys()]


N = 4
ind = np.arange(len(names))
width = 0.20

xvals = [v for v in dico_hugo.values()]
bar1= plt.bar(ind, xvals, width, color = "tab:blue")

yvals = [v for v in dico_baudelaire.values()]
bar2 = plt.bar(ind + width, yvals, width, color = "tab:orange")

zvals = [v for v in dico_musset.values()]
bar3 = plt.bar(ind+width*2, zvals, width, color = "tab:green")

uvals = [v for v in dico_lamartine.values()]
bar4 = plt.bar(ind+width*3, uvals, width, color = "tab:red")


plt.ylabel(" Occurrences")
plt.title("Occurrence moyenne d'une voyelle par vers")

plt.xticks(ind+width, names)
plt.ylim(0,5)
plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
plt.show()
