# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:48:11 2020

@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\rosalind_rna.txt'
dna=open(sourse,'r')

dnaseq=dna.readline()
dnaseq=dnaseq.upper()
rnaseq=dnaseq.replace('T', 'U')
print(rnaseq)
dna.close()