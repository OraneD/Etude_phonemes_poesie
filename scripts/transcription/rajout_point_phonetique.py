#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 18:41:32 2023

@author: orane
"""

#rajouter un point à la fin du vers phonétique pour pouvoir attraper la syllabe avec regex
import csv

def rajouter(fichier, output) :
    with open(fichier, "r") as csvfile :
        csv_reader = csv.reader(csvfile)
        with open(output, "w") as f :
            for row in csv_reader :
                f.write(row[0] + "," + row[1] + ".," + row[2] + "\n")
        


rajouter(
    "../../resultats/csv_transcriptions/corpus_corrige/baudelaire_corrig.csv",
    "../../resultats/csv_transcriptions/corpus_corrige/baudelaire_corrig_p.csv",
)
rajouter("../../resultats/csv_transcriptions/corpus_corrige/hugo_corrig.csv",
                           "../../resultats/csv_transcriptions/corpus_corrige/hugo_corrig_p.csv",
)

rajouter("../../resultats/csv_transcriptions/corpus_corrige/musset_corrig.csv", 
                           "../../resultats/csv_transcriptions/corpus_corrige/musset_corrig_p.csv",
)

rajouter("../../resultats/csv_transcriptions/corpus_corrige/lamartine_corrig.csv",
                           "../../resultats/csv_transcriptions/corpus_corrige/lamartine_corrig_p.csv",

)