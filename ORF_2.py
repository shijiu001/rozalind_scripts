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
    
    #codon=codon.replace('      ', '\n').replace('   ', '\n') #这里replace出的问题，可能是每一行最后一个后面的空格数和其他的不一样，
    #所以codon这么replace过是这样的
    # TTC F  前面会多一个空格
    #CTC L
    #ATC I
    #GTC V
    #然后在转换为字典的话，就比如' TTC' 那一项就会被存成{' TT':' F'} ,没有'TTC'这一个键了，所以在用TTC密码子索引字典的时候（cd['TTC']）就会报错key error

    # print(codon)
    # while i<64:
    #     line=codon.splitlines()[i]
    #     cd[line[0:3]]=line[4:]
    #     i+=1


#--------上面那段改成这个就行了--
    codon = codon.split()  #split不加参数，直接按空白字符分割字符串就行了
    #print(codon)
    for i in range(0,len(codon) - 1,2):  
        cd.update({codon[i]:codon[i+1]})
#-----------------------------


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

#source=r'C:\Users\funw0\Downloads\abcd.txt'
source=r'C:\Users\funw0\Downloads\rosalind_orf (1).txt'
f=open(source)
dna=f.readline()
f.close()

orf=orfgen(dna)


subseq=[]
prot=[]
for seq in orf:
    for i in range(0,len(seq)-2,3):
        if seq[i:i+3]=='ATG':
            subseq.append(seq[i:])

for seq in subseq:
    p=transDNA(seq)
    if p not in prot and p !='':
        prot.append(p)

for p in prot:
    print(p)


