# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:31:49 2021

@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\rosalind_corr (3).txt'
res = open(r'C:\Users\funw0\Downloads\res.txt','w')
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

def revc(s):
    s=s.upper()
    rs=s[::-1]
    rcs=rs.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G','c')
    rcs=rcs.upper()
    return rcs

def hamming(s1,s2):
    n=0
    for i in range(max(len(s1),len(s2))):
        if i < min(len(s1),len(s2)) and s1[i]!=s2[i]:
            n += 1
        if i > min(len(s1),len(s2)):
            n += 1
    return n

mem={}
for s in ss:
    if s in mem.keys():
        mem[s]=mem[s]+1
    elif revc(s) in mem.keys():
        mem[revc(s)]=mem[revc(s)]+1
    else:
        mem[s]=1

r=[]
w=[]
for key,value in mem.items():
    if value == 1:
        w.append(key)
    if value > 1:
        r.append(key)

for ws in w:
    for ref in r:
        if hamming(ws,ref) == 1:
            print('{}->{}'.format(ws,ref),file=res)
        if hamming(revc(ws),ref) == 1:
            print('{}->{}'.format(ws,revc(ref)),file=res)
        