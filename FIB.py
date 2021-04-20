# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:22:56 2020

@author: funw0
"""


rbt=[1,1]
n=33
k=1
i=1

while i+2<=n:
    new=rbt[i]+rbt[i-1]*k
    rbt.append(new)
    i+=1

print(new)

