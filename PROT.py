# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:00:58 2020

@author: funw0
"""

i=0
cd={}
protein=''
codon='''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G '''

codon=codon.replace('      ', '\n').replace('   ', '\n')
while i<64:
    line=codon.splitlines()[i]
    cd[line[0:3]]=line[4:]
    i+=1
    

sourse=r'C:\Users\funw0\Downloads\rosalind_prot.txt'
#sourse=r'C:\Users\funw0\Downloads\GDP.txt'
rna=open(sourse)

rnaseq=rna.readline()
rnaseq=rnaseq.replace(' ','').replace('\n','')

if i==64:
    i=0

#if len(rnaseq)%3==0:
while i<len(rnaseq):
    cc=rnaseq[i:i+3]
    if cd[cc] !='Stop':
        protein=protein+cd[cc]
        i=i+3
    else:
        break

protein=protein.replace('\n','')
print(protein)