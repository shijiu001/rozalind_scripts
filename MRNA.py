# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:43:35 2020

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
UGG W      CGG R      AGG R      GGG G'''

codon=codon.replace('      ', '\n').replace('   ', '\n')
while i<64:
    line=codon.splitlines()[i]
    cd[line[0:3]]=line[4:]
    i+=1
    
tr={}
for key,value in cd.items():
    if value in tr:
        tr[value]=tr[value]+1
    else:
        tr[value]=1

source=r'C:\Users\funw0\Downloads\rosalind_mrna (1).txt'
f=open(source)
aa=f.read().replace('\n','').split(' ')

m=1
t=0
while t<len(aa[0]):
    i=tr[aa[0][t]]
    print(i)
    m=m*i % 1000000
    t+=1
m=m*3 %1000000