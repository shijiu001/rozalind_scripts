# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 00:53:21 2020

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\rosalind_hamm.txt'
seq=open(sourse)

seq1=seq.readline().replace('\n','').strip(' ')
seq2=seq.readline().replace('\n','').strip(' ')

i=0
n=0

while i<len(seq1):
    if seq1[i] != seq2[i]:
        n+=1
    else:
        pass
    i+=1

print(n)