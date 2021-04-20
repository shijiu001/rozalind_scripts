# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:50:50 2020

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\rosalind_fibd.txt'
file=open(sourse)
data=file.readline()
data=data.replace('\n','')
d=data.split(' ')

n=int(d[0])
m=int(d[1])
rbt=[0,1]
t=1

while t<m:
    new=rbt[t]+rbt[t-1]
    rbt.append(new)
    t+=1
    if t==m:
        new=rbt[t]+rbt[t-1]-1
        rbt.append(new)
        del rbt[0]
    
i=len(rbt)-1
while i+2<=n:
    new=rbt[i]+rbt[i-1]-rbt[i-m]
    rbt.append(new)
    i+=1

print(rbt[n-1])    