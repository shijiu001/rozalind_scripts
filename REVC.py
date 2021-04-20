# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:02:07 2020

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\rosalind_revc.txt'
dna=open(sourse,'r')

dnaseq=dna.readline()
dnaseq=dnaseq.upper()
r_dna=dnaseq[::-1]
rc_dna=r_dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G','c')
rc_dna=rc_dna.upper()

print(rc_dna)