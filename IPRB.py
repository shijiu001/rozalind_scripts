# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:19:15 2020

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\rosalind_iprb.txt'
file=open(sourse)
data=file.readline()
data=data.replace('\n','')
d=data.split(' ')
k=int(d[0])
m=int(d[1])
n=int(d[2])

# =============================================================================
# k=2
# m=2
# n=2
# =============================================================================

ppl=k+m+n

ct=ppl*(ppl-1)/2
cn=n*(n-1)/2
cm=m*(m-1)/2
cmn=m*n

p=cn/ct+cm/(ct*4)+cmn/(ct*2)

print (1-p)