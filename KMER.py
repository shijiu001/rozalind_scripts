# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 18:34:26 2021

@author: funw0
"""
#source = r'C:\Users\funw0\Downloads\abcd.txt'
source = r'C:\Users\funw0\Downloads\rosalind_kmer.txt'
f =  open(source)

s = ''
for line in f:
    if line.startswith('>'):
        continue
    else:
        s = s + line.replace('\n','')

c = 'ACGT'
mc = {}

for i in range(4):
    for j in range(4):
        for t in range(4):
            for k in range(4):
                cc = c[i] + c[j] + c[t] + c[k]
                mc[cc] = 0
      
for i in range(len(s)-3):
    ss = s[i:i+4]
    mc[ss] = mc[ss] + 1
    i = i + 1

mcv = list(mc.values())

for i in mcv:
    print(i, end=' ')
