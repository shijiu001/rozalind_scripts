# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:01:14 2020

@author: funw0
"""

from scipy.special import comb

sourse=r'C:\Users\funw0\Downloads\rosalind_lia.txt'
f=open(sourse)
data=f.readline().replace('\n','').split(' ')
k=int(data[0])
n=int(data[1])

p=2**k
pr=0
i=n

while i<=p:
    pr=pr + (0.25**i) * (0.75**(p-i)) *comb(p,i)
    i+=1