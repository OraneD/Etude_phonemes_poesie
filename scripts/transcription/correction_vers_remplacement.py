#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:30:00 2023

@author: orane
"""
import csv

class Verse:
    def __init__(self, verses_csv_row):
        self.text = verses_csv_row[0]
        self.phonemes = verses_csv_row[1]
        self.n_syllables = int(verses_csv_row[2])

    def is_corrected(self):
        return self.n_syllables == 12


def remplacement_vers_corriges(fichier_corpus, fichier_correction, nouveau_fichier) :
        c = 0
        lst_correction_index = []
        lst_corpus_index = []
        lst_vers_corpus = []
        with open(fichier_corpus) as fcorpus :
            reader = csv.reader(fcorpus)
            with open(fichier_correction) as fcorrection:
                correction = csv.reader(fcorrection)
                
                for correction_index, correction_row in enumerate(correction):
                    for corpus_index, corpus_row in enumerate(reader):
                        if corpus_row[0] == correction_row[0]:
                            if correction_row[2] == "12" :
                                print(correction_index, corpus_index, correction_row[0], corpus_row[0])
                                lst_correction_index.append(correction_index)
                                lst_corpus_index.append(corpus_index)
                                lst_vers_corpus.append(corpus_row[0])
                                c += 1
                            break
                        
        print(c)
        
        with open(fichier_corpus) as fcorpus :
            reader = csv.reader(fcorpus)
            with open(fichier_correction) as fcorrection:
                correction = csv.reader(fcorrection)
                with open(nouveau_fichier, "w") as nf :
                    for correction_index, correction_row in enumerate(correction) :
                        if correction_index in lst_correction_index :
                            nf.write(correction_row[0] + "," + correction_row[1] + "," + correction_row[2] + "\n")
                    
                    for corpus_index, corpus_row in enumerate(reader) :
                        if corpus_row[0] not in lst_vers_corpus :
                            nf.write(corpus_row[0] + "," + corpus_row[1] + "," + corpus_row[2] + "\n")
        
            
            
    


remplacement_vers_corriges(
    "../../resultats/csv_transcriptions/baudelaire.csv",
    "../../resultats/csv_transcriptions/erreurs_vers/correction_baudelaire.csv",
    "../../resultats/csv_transcriptions/corpus_corrige/baudelaire_corrig.csv"
)
remplacement_vers_corriges("../../resultats/csv_transcriptions/hugo.csv",
                           "../../resultats/csv_transcriptions/erreurs_vers/correction_hugo.csv",
                           "../../resultats/csv_transcriptions/corpus_corrige/hugo_corrig.csv")

remplacement_vers_corriges("../../resultats/csv_transcriptions/musset.csv", 
                           "../../resultats/csv_transcriptions/erreurs_vers/correction_musset.csv",
                           "../../resultats/csv_transcriptions/corpus_corrige/musset_corrig.csv")

remplacement_vers_corriges("../../resultats/csv_transcriptions/lamartine.csv",
                           "../../resultats/csv_transcriptions/erreurs_vers/correction_lamartine.csv",
                           "../../resultats/csv_transcriptions/corpus_corrige/lamartine_corrig.csv")