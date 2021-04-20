# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:32:47 2020

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\rosalind_gc.txt'
fasta=open(sourse)

i=0
n=0
name=''
ss={}

for line in fasta:
    if line.startswith('>'):
        name=line.replace('>','').strip(' ')
        ss[name]=''
    else:
        ss[name]=ss[name]+line.replace('\n','').strip(' ')
fasta.close()

for key,value in ss.items():
    for char in value:
        if char=='C' or char=='G':
                i+=1
    cg=i/len(value)*100
    i=0
    if n<cg:
        a=key
        n=cg

print(a, n)
            