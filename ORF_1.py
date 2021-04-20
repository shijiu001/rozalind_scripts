# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:19:17 2020

@author: funw0
"""


def orfgen(dnaseq):
    dnaseq=dnaseq.upper()
    r_dna=dnaseq[::-1]
    rc_dna=r_dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G','c')
    rc_dna=rc_dna.upper()
    orf=[dnaseq[0:],dnaseq[1:],dnaseq[2:],rc_dna[0:],rc_dna[1:],rc_dna[2:]]
    return orf

def transDNA(dnaseq):
    i=0
    cd={}
    protein=''
    codon='''
TTT F      CTT L      ATT I      GTT V
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
    print(codon)
    while i<64:
        line=codon.splitlines()[i]
        cd[line[0:3]]=line[4:]
        i+=1

    i=0
    while i<len(dnaseq)-3:
        cc=dnaseq[i:i+3]
        print(cc,cd[cc])
        if cd[cc] !='Stop':
            protein=protein+cd[cc]
            i=i+3
        else:
            break
    return protein

source=r'C:\Users\funw0\Downloads\abcd.txt'
f=open(source)
dna=f.readline()
f.close()

orf=orfgen(dna)


subseq=[]
prot=[]
for seq in orf:
    i=0
    while i<len(seq)-3:
        if seq[i:i+3]=='ATG':
            subseq.append(seq[i:])
        i=i+3

for seq in subseq:
    p=transDNA(subseq[3])
    if p not in prot:
        prot.append(p)
        