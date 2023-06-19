#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:29:50 2023

@author: orane
"""

import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
import numpy as np

liste_phonemes = ["a", "A", "b", "C", "k", "d", "e", "E", "f", "g", "H", "i", "j", "J", "t", "Z", "z", "e~", "w", "@", "s", "R", "2", "u", "y", "o", "O", "9", "v", "m", "n", "N", "S"]
liste_e = ["@", "2", "9"]
liste_o = ["o", "O"]
liste_voyelles = ["a", "@", "2", "9", "o", "O", "e", "E", "u", "y", "i", "e~", "A", "C", "H", "j"]
liste_voyelles_dico = ["a", "@", "o", "e", "E", "u", "y", "i", "e~", "A", "C"]

liste_consonnes = ["p", "t", "k", "f", "s" ,"S","b", "d", "g", "v", "z" "j", "l","R", "n" "N", "m"]

regex_consonnes = "(p|t|k|f|s|S|b|d|g|v|z|j|l|R|n|N|m|Z|w|H)"
regex_voyelles = "(a|@|2|9|o|O|e|E|u|y|i|e~|A|C|H|j)"

regex = ( "(" + regex_consonnes + "?" + regex_voyelles + regex_consonnes + "?" + ")" + "$")



def stats_rime(fichier):
                dico_cesure = {}
                nb_row = 0
    
                with open(fichier, "r") as filecsv:
                    print(fichier)
                    csvreader = csv.reader(filecsv)
                    for row in csvreader :
                        if row[2] == "12":
                            nb_row += 1
        
                            if  re.search(regex, row[1]) :
                                rex = re.search(regex, row[1])
        
                                if dico_cesure.get(rex.group().strip("|")) == None :
                                    dico_cesure[rex.group().strip("|")] = 1
                                else :
                                    dico_cesure[rex.group().strip("|")] += 1
                                
                            

                            
    
                
                print(nb_row)
                values = [round((v / sum(dico_cesure.values())) * 100, 2) for v in dico_cesure.values()]
                sorted_dic = sorted(dico_cesure.items(), key=lambda x:x[1], reverse = True)
                lst_names = []
                lst_value = []
                
                keys = ["Syllabe", "Occurrences", "Pourcentage"]
                print(sum(dico_cesure.values()))
                with open("../resultats/statistique/rime/csv/syllabes_rime_lamartine.csv", "w") as csvfile :
                    writer =  csv.writer(csvfile)
                    writer.writerow(keys)
                    for key, value in dico_cesure.items() :
                        writer.writerow([key, value, round(value / sum(dico_cesure.values()) * 100, 2)])
    
                    
                     
                for names, values in sorted_dic[0:10] :
                    lst_names.append(names)
                    lst_value.append(round(values/sum(dico_cesure.values()) * 100, 2))
                names = sorted_dic[0:10]
                return lst_names, lst_value


                
#Nhugo, Vhugo = stats_rime("../resultats/csv_transcriptions/hugo.csv")
#Nbaudelaire, Vbaudelaire = stats_rime("../resultats/csv_transcriptions/baudelaire.csv")
#Nmusset, Vmusset = stats_rime("../resultats/csv_transcriptions/musset.csv")
Nlamartine, Vlamartine = stats_rime("../resultats/csv_transcriptions/lamartine.csv")


fig, ax = plt.subplots()

syl = Nlamartine
counts = Vlamartine


ax.bar(syl, counts)

ax.set_ylabel('Pourcentage parmi tous les vers')
ax.set_title('Syllabes à la rime les plus fréquentes pour Lamartine')