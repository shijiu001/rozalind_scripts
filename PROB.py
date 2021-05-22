# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:07:28 2021

@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\rosalind_prob.txt'
f=open(sourse)

data = f.readlines()
seq=data[0].replace('\n','')
a=data[1].split(' ')

import math

for x in a:
    pcg = float(x)
    pat = 1-pcg
    pa = pt = pat/2
    pc = pg = pcg/2
    
    p=0
    
    for c in seq:
        if c == 'A' or c == 'T':
            p = p + math.log(pa,10)
        if c == 'C' or c == 'G':
            p = p + math.log(pc,10)
    
    print(round(p,3),end=' ')