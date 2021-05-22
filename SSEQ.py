# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:55:31 2021

@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\bbbb.txt'
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

def findseq(c,n):
    return(ss[0].find(c,n))

n=0
for i in range(len(ss[1])):
    if findseq(ss[1][i], n) != -1:
        n =findseq(ss[1][i], n)+1
        print(n,end=(' '))
        i += 1
    else:
        break

if i != len(ss[1]):
    print('error!')
    

    