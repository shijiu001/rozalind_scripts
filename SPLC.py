# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:46:19 2020

@author: funw0
"""

def transDNA(dnaseq):
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
       
    codon = codon.split()  #split不加参数，直接按空白字符分割字符串就行了
    #print(codon)
    for i in range(0,len(codon) - 1,2):  
        cd.update({codon[i]:codon[i+1]})

    i=0
    while i<= len(dnaseq)-3:
        cc=dnaseq[i:i+3]
        #print(cc,cd[cc])
        if cd[cc] !='Stop':
            protein=protein+cd[cc]
            i=i+3
        else:
            break
    if cd[cc]=='Stop':
        return protein
    else:
        return ''

source=r'C:\Users\funw0\Downloads\rosalind_splc.txt'
f=open(source)

seqs=[]
prna=''

for line in f:
    if line.startswith('>'):
        seqs.append('')
    else:
        seqs[len(seqs)-1]=seqs[len(seqs)-1]+line.strip()

prna=seqs[0]
del seqs[0]

for intron in seqs:
    if intron in prna:
        prna=prna.replace(intron,'')
        
print(transDNA(prna))
        

    
