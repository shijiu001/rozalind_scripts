# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:17:33 2020

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\rosalind_subs.txt'
f=open(sourse)

seq=f.readline().replace('\n', '')
motif=f.readline().replace('\n', '')

i=0
l=len(motif)
ll=len(seq)

while (i+l)<ll:
    if seq[i:i+l]==motif:
        i=i+1
        print(i,end=' ')
    else:
        i=i+1