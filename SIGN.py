# -*- coding: utf-8 -*-
"""
Created on Thu May 20 00:37:05 2021

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\abcd.txt'
f=open(sourse,'w')
n = 6

na=[]
for i in range(1,n+1):
    na.append(i)

d=[]
for i in range(n):
    d.append(1)
    d.append(-1)

import math
num = math.factorial(n) * (2**n)

print(num,file=f)

import itertools

x=list(itertools.permutations(na))
y=list(itertools.permutations(d))

yy=[]
for i in y:
    if i[0:n] not in yy:
        yy.append(i[0:n])

ans=[]
for i in x:
    for j in yy:
        anss=[]
        for k in range(n):
            ansss = i[k]*j[k]
            print(ansss,end=(' '),file=f)
            anss.append(ansss)
        print('',file=f) 
        ans.append(anss)
   
    


    
    