#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 18:53:48 2023

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

regex_cesure = (regex_consonnes + "{0,2}" + regex_voyelles + regex_consonnes + "?\|")

regex_rime = (regex_consonnes + "{0,2}" + regex_voyelles + regex_consonnes + "?\.")


def stats_cesure(fichier, csv_output):
                dico_cesure = {}
                nb_row = 0
    
                with open(fichier, "r") as filecsv:
                    print(fichier)
                    csvreader = csv.reader(filecsv)
                    for row in csvreader :
                        if row[2] == "12":
                            nb_row += 1
        
                            if  re.search(regex_cesure, row[1]) :
                                rex_cesure = re.search(regex_cesure, row[1])   
        
                                if dico_cesure.get(rex_cesure.group().strip("|")) == None :
                                    dico_cesure[rex_cesure.group().strip("|")] = 1
                                    
                                    if  re.search(regex_rime, row[1]) :
                                        rex_rime = re.search(regex_rime, row[1])   
                
                                        if dico_cesure.get(rex_rime.group().strip(".")) == None :
                                            dico_cesure[rex_rime.group().strip(".")] = 1
                                        else :
                                            dico_cesure[rex_rime.group().strip(".")] += 1
                                    
                                    
                                else :
                                    dico_cesure[rex_cesure.group().strip("|")] += 1
                                    
                                    if  re.search(regex_rime, row[1]) :
                                        rex_rime = re.search(regex_rime, row[1])   
                
                                        if dico_cesure.get(rex_rime.group().strip(".")) == None :
                                            dico_cesure[rex_rime.group().strip(".")] = 1
                                        else :
                                            dico_cesure[rex_rime.group().strip(".")] += 1
                                
                            

                            
    
                
                print(nb_row)
                values = [round((v / sum(dico_cesure.values())) * 100, 2) for v in dico_cesure.values()]
                sorted_dic = sorted(dico_cesure.items(), key=lambda x:x[1], reverse = True)
                lst_names = []
                lst_value = []
                
                keys = ["Syllabe", "Occurrences", "Pourcentage"]
                print(sum(dico_cesure.values()))
                with open(csv_output, "w") as csvfile :
                    writer =  csv.writer(csvfile)
                    writer.writerow(keys)
                    for key, value in dico_cesure.items() :
                        writer.writerow([key, value, round(value / sum(dico_cesure.values()) * 100, 2)])
    
                    
                     
                for names, values in sorted_dic[0:10] :
                    lst_names.append(names)
                    lst_value.append(round(values/sum(dico_cesure.values()) * 100, 2))
                names = sorted_dic[0:10]
                return lst_names, lst_value


                
Nhugo, Vhugo = stats_cesure("../../resultats/csv_transcriptions/corpus_corrige/hugo_corrig_p.csv",
                            "../../resultats/statistique/rime_cesure/csv/hugo_syllabe_cesure_rime.csv")

Nbaudelaire, Vbaudelaire = stats_cesure("../../resultats/csv_transcriptions/corpus_corrige/baudelaire_corrig_p.csv",
                                        "../../resultats/statistique/rime_cesure/csv/baudelaire_syllabe_cesure_rime.csv")

Nmusset, Vmusset = stats_cesure("../../resultats/csv_transcriptions/corpus_corrige/musset_corrig_p.csv",
                               "../../resultats/statistique/rime_cesure/csv/musset_syllabe_cesure_rime.csv" )

Nlamartine, Vlamartine = stats_cesure("../../resultats/csv_transcriptions/corpus_corrige/lamartine_corrig_p.csv", 
                                      "../../resultats/statistique/rime_cesure/csv/lamartine_syllabe_cesure_rime.csv")


fig, ax = plt.subplots()

syl = Nlamartine
counts = Vlamartine


ax.bar(syl, counts)

ax.set_ylabel('Pourcentage parmi tous les vers')
ax.set_title('Syllabes à la césure les plus fréquentes pour Lamartine')