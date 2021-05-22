# -*- coding: utf-8 -*-
"""
Created on Wed May 19 21:36:19 2021

@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\rosalind_pmch.txt'
fasta=open(sourse)

seq=''
for line in fasta:
    if line.startswith('>'):
        index = line.replace('\n','')
    else:
        seq = seq + line.replace('\n','')

a = seq.count('A')
c = seq.count('C')

import math
ap = math.factorial(a)
cp = math.factorial(c)

p = ap*cp
print(p)