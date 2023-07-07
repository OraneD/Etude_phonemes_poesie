#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 15:33:37 2023

@author: orane
"""

import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np


couple_k_g = ["k" , "g"]
couple_f_v = ["f", "v"]
couple_p_b_m = ["p", "b", "m"]
couple_s_z = ["s", "z"]
couple_S_Z = ["S", "Z"]
couple_t_d = ["t", "d"]
liste_consonnes =  ["p", "t", "k", "f", "s", "S","b", "d", "g", "v", "z", "j", "l","R", "n", "m", "w", "H", "Z"]
liste_consonnes_couple = ["k, g", "f, v", "p, b, m", "s, z", "S, Z", "t, d", "j", "l", "R", "n", "w", "H"]

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
                    

                    dico_consonnes = {"k, g" : 0, "f, v" : 0, "H" : 0, "s, z" : 0, "S, Z" : 0, "R" : 0, "l" : 0, "j" : 0, "p, b, m" : 0, "w" : 0, "t, d" : 0, "n" : 0}
                    with open(fichier, "r") as filecsv:
                        csvreader = csv.reader(filecsv)
                        for row in csvreader :
                            if row[2] == "12":
                                for phoneme in liste_consonnes :
                                    if phoneme in couple_k_g  and len(re.findall(phoneme, row[1])) == nb :
                                        dico_consonnes["k, g"] += 1
                                    
                                        
                                    elif phoneme in couple_f_v and len(re.findall(phoneme, row[1])) == nb :
                                        dico_consonnes["f, v"] += 1
                                        
                                    elif phoneme in couple_p_b_m and len(re.findall(phoneme, row[1])) == nb :
                                        dico_consonnes["p, b, m"] += 1
                                        
                                    elif phoneme in couple_s_z and len(re.findall(phoneme, row[1])) == nb :
                                        dico_consonnes["s, z"] += 1
                                        
                                    elif phoneme in couple_S_Z and len(re.findall(phoneme, row[1])) == nb :
                                        dico_consonnes["S, Z"] += 1
                                    
                                    elif phoneme in couple_t_d and len(re.findall(phoneme, row[1])) == nb :
                                        dico_consonnes["t, d"] += 1
                                         
                                    elif len(re.findall(phoneme, row[1])) == nb :
                                        dico_consonnes[phoneme] += 1
                            
                    for key, value in dico_consonnes.items() :
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
    dico_consonnes = {"k, g" : 0, "f, v" : 0, "H" : 0, "s, z" : 0, "S, Z" : 0, "R" : 0, "l" : 0, "j" : 0, "p, b, m" : 0, "w" : 0, "t, d" : 0, "n" : 0}
    for consonne in liste_consonnes_couple :
        c = 0
        for phoneme in lst_phoneme :

            if consonne == phoneme.phoneme :
               # print(phoneme.phoneme, phoneme.repetition.occurrences, phoneme.repetition.compte)
                c += phoneme.repetition.occurrences * phoneme.repetition.compte
        dico_consonnes[consonne] += round(c / nb_vers, 2)
        
        
        
    return(dico_consonnes)
    
dico_hugo = moyenne_phoneme(pho_hugo,27693 )
dico_baudelaire = moyenne_phoneme(pho_baudelaire, 2790)
dico_musset = moyenne_phoneme(pho_musset, 7231)
dico_lamartine = moyenne_phoneme(pho_lamartine, 16018)






    
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
plt.title("Occurrence moyenne d'une consonne par vers")

plt.xticks(ind+width, names)
plt.ylim(0,5)
plt.legend( (bar1, bar2, bar3, bar4), ('Hugo', 'Baudelaire', 'Musset', "Lamartine") )
plt.show()


        
                
        


