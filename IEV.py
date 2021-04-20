# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:39:17 2020

@author: funw0
"""


#genotype=[[AA,AA],[AA,Aa],[AA,aa],[Aa,Aa],[Aa,aa],[aa,aa]]
p=[2,2,2,1.5,1,0]
sourse=r'C:\Users\funw0\Downloads\rosalind_iev.txt'
f=open(sourse)
data=f.readline().replace('\n','').split(' ')
data=list(map(int,data))

e=0
i=0
while i<6:
   e=e+p[i]*data[i]
   i+=1
   
print(e)