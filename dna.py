# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:26:08 2020

@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\rosalind_dna.txt'
a,t,c,g=0,0,0,0
opps=0

dna=open(sourse,'r')
seq=dna.readline()
seq=seq.lower()

for char in seq:
    if char=='a':
        a+=1
    elif char=='t':
        t+=1
    elif char=='c':
        c+=1
    elif char=='g':
        g+=1
    else:
        opps+=1

print(a,c,g,t)
print(opps)