# -*- coding: utf-8 -*-
"""
Created on Sat May 22 17:52:56 2021

@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\rosalind_tran.txt'
f=open(sourse)

ss=[]
seq=''
for line in f:
    if line.startswith('>'):
        if seq!='':
            ss.append(seq)
        seq=''        
    else:
        seq=seq+line.replace('\n','').strip(' ')
ss.append(seq)

transitions=['AG','GA','CT','TC']
transversions=['AC','CA','AT','TA','CG','GC','GT','TG']

ts=tv=0
for i in range(len(ss[0])):
    s=ss[0][i]+ss[1][i]
    if s in transitions:
        ts += 1
    if s in transversions:
        tv += 1

r=ts/tv
print(r)