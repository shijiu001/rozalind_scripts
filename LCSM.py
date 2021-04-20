# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:17:46 2020

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\rosalind_lcsm.txt'
f=open(sourse)

seqs=[]
i=-1

for line in f:
    if line.startswith('>'):
        seqs.append('')
        i+=1
    else:
        seqs[i]=seqs[i]+line.replace('\n','').strip(' ')
f.close()

seqs=sorted(seqs,key=len)

l=len(seqs[0])
s=len(seqs)
i=l
k=0
n=0

motifs=[]
while i>=1:
    while k+i<=l:
        motif=seqs[0][k:i+k]
        for seq in seqs:
            if motif in seq:
                test=True
            if motif not in seq:
                test=False
                break
        if test==True:
            motifs.append(motif)
        k+=1
    i=i-1
    k=0