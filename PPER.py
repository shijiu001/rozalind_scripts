# -*- coding: utf-8 -*-
"""
Created on Wed May 19 22:40:18 2021

@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\rosalind_pper.txt'
f=open(sourse)


data = f.readline().split(' ')
n = int(data[0])
k = int(data[1])
pnk = 1
while k > 0:
    pnk = pnk * (n-k+1)
    k = k-1
    
pnkm = pnk % 1000000