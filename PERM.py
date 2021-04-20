# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 01:21:48 2020

@author: funw0
"""


from itertools import permutations

a=5
b=[]
c=[]
for i in range(0,a):
    b.append(i+1)
    
c=list(permutations(b,a))

i=0
while i<len(c):
    cc=str(c[i]).replace('(','').replace(')','').replace(', ',' ')
    c[i]=cc
    i+=1
    
print(len(c))
for cc in c:
    print(cc)