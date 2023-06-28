#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:22:20 2023

@author: orane
"""

import csv 
from pathlib import Path
def compte_vers():
    corpus = Path("../../resultats/csv_transcriptions")
    for fichier in corpus.iterdir() :
        if str(fichier).endswith(".csv") : 
            alex = 0
            nb_vers = 0
            with open(fichier, "r") as filecsv:
                csvreader = csv.reader(filecsv)
                for row in csvreader :
                    if row[2] == "12":
                        alex += 1
                        nb_vers += 1
                    elif row[2] == "13" or row[2] == "11" or row[2] == "14" or row[2] == "10" :
                        nb_vers += 1
            with open("compte_vers.txt", "a") as compte :
                compte.write(str(fichier) + " Vers :" + str(nb_vers) + " Alexandrins :"  + str(alex) + "\n")
           

compte_vers()
    