# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:49:57 2020

@author: funw0
"""


source=r'C:\Users\funw0\Downloads\abcd.txt'
f=open(source)
dna=f.readline().upper()
r_dna=dna[::-1]
rc_dna=r_dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G','c')
rc_dna=rc_dna.upper()

orf=[dna[0:],dna[1:],dna[2:],rc_dna[0:],rc_dna[1:],rc_dna[2:]]


i=0
cd={}
protein=''
codon='''TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G'''

codon=codon.replace('      ', '\n').replace('   ', '\n')
while i<64:
    line=codon.splitlines()[i]
    cd[line[0:3]]=line[4:]
    i+=1
    
 
i=0
while i==0:
    t=0
    while t<len(orf[i]):
        if orf[i][t:t+3]=='ATG':
            protein=''
            while t<len(orf[i])-3:
                cc=orf[i][t:t+3]
                if cd[cc] !='Stop':
                    protein=protein+cd[cc]
                    t=t+3
                else:
                    print(protein)
                    break
        else:
            t=t+3
    i+=1
            