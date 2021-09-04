# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:32:24 2021

@author: funw0
"""

def catalan(n):
    """
    a function to return catalan number
    """
    h=[1,1]
    if n <= 1:
        return 1
    else:
        for i in range(2,n+1):
            tmp = 0
            for k in range(1,i+1):
                c = h[k-1]*h[i-k]
                tmp = tmp + c
            h.append(tmp)
        return h[n]

mem={
     '':1,'AU':1,'UA':1,'CG':1,'GC':1
     }


def ismatch(c1,c2):
    s=c1+c2
    if s in ['AU','UA','CG','GC']:
        return True
    else:
        return False

def noncross(seq):
    if seq in mem.keys():
        return mem[seq]
    else:
        n=len(seq)
        c=0
        for m in range(1,n,2):
            if ismatch(seq[0],seq[m]):
                c += noncross(seq[1:m])*noncross(seq[m+1:])
        mem[seq]=c
        return mem[seq]
 
    
sourse=r'C:\Users\funw0\Downloads\rosalind_cat.txt'
f=open(sourse)
data=f.read().split('\n')
seq=''
for i in range(1,len(data)):
    seq = seq + data[i]

print(noncross(seq)%1000000)
    