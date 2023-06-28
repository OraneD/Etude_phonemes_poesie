#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 16:57:47 2023

@author: orane
"""
import csv
def compte_erreur(erreur, correction) :
    c = 0
    i = 0
    with open(erreur, "r") as csverreur :
        reader = csv.reader(csverreur)
        for row in reader :
            c += 1
    
  
    with open(correction, "r") as csvcorrection :
        reader2 = csv.reader(csvcorrection) 
        for row in reader2 :
            if row[2] == "12" :
                i += 1
    print(erreur + " " + str(i) + " vers corrigés sur " + str(c) + " erreurs")



compte_erreur("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_baudelaire.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_baudelaire.csv")
compte_erreur("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_hugo.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_hugo.csv")
compte_erreur("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_musset.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_musset.csv")
compte_erreur("../../resultats/csv_transcriptions/erreurs_vers/erreur_vers_lamartine.csv", "../../resultats/csv_transcriptions/erreurs_vers/correction_lamartine.csv")