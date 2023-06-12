#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 23:04:37 2023

@author: orane
"""
import csv 
from pathlib import Path
import re 
import matplotlib.pyplot as plt
liste_phonemes = ["a", "A", "b", "C", "k", "d", "e", "E", "f", "g", "H", "i", "j", "J", "t", "Z", "z", "e~", "w", "@", "s", "R", "2", "u", "y", "o", "O", "9", "v", "m", "n", "N", "S"]
def stats_phonemes():
        corpus = Path("../resultats/csv_transcriptions")
        for fichier in corpus.iterdir() :
            dico_stats = {}
            for phoneme in liste_phonemes :
                dico_stats[phoneme] = 0

            with open(fichier, "r") as filecsv:
                csvreader = csv.reader(filecsv)
                for row in csvreader :
                    if row[2] == "12":
                        for phoneme in liste_phonemes :
                            if len(re.findall(phoneme, row[1])) != 0 :
                                dico_stats[phoneme] += len(re.findall(phoneme, row[1]))
                            
            names = list(dico_stats.keys())
            values = list(dico_stats.values())
            plt.bar(range(len(dico_stats)), values, tick_label = names)
            plt.title("Compte phonèmes corpus " + str(fichier).split("/")[-1].split(".")[0])
            plt.show()
            
stats_phonemes()