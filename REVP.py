# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:51:34 2020

@author: funw0
"""


source=r'C:\Users\funw0\Downloads\rosalind_revp (2).txt'
f=open(source)


seq=''
for line in f:
    if line.startswith('>'):
        pass
    else:
        seq=seq+line
seq=seq.replace('\n','') 
rseq=seq[::-1]
rcseq=rseq.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G','c')
rcseq=rcseq.upper()

for l in range(4,13):
    for i in range(0,len(seq)-l+1):
        a=seq[i:i+l]
        b=rcseq[len(seq)-i-l:len(seq)-i]
        if a == b:
            print(i+1,l)