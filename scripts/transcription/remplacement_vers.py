#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:07:45 2023

@author: orane
"""

import csv 

def remplacement_vers_corriges(fichier_corpus, fichier_correction) :
        c = 0
        with open(fichier_corpus) as fcorpus :
            reader = csv.reader(fcorpus)
            with open(fichier_correction) as fcorrection:
                correction = csv.reader(fcorrection) 
                
                for i, row in enumerate(correction):
                    print(i)
                    for j, row2 in enumerate(reader):
                        print(j)
                        if row[0] == row2[0]:
                            if row[2] == "12" :
                                print(row[0], row2[0])
                                c += 1
                            break
        
        print(c)
                
            
                        


 
                    

                       
remplacement_vers_corriges("../../resultats/csv_transcriptions/baudelaire.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_baudelaire.csv")
#compte_erreur("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_hugo.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_hugo.csv")
#compte_erreur("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_musset.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_musset.csv")
#compte_erreur("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_lamartine.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_lamartine.csv")
        