#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:10:56 2023

@author: orane
"""
import os
import re



with open("hugo_test.txt", "r") as poeme :
    for line in poeme.readlines() :
        vers = re.sub(r"[^\w\s\n\'-]", "", line).lower()
        vers_phonetique = ""
        for mot in vers.split() :
            with open("dico1.txt", "r") as dico :
                for line in dico.readlines() :
                    ortho = line.split()[0]
                    phonetique = line.split()[1]
                    if mot == ortho :
                        vers_phonetique += phonetique + " "
                        break


        print(vers, vers_phonetique)
                
                