# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 01:08:23 2020

@author: funw0
"""


def perm(a,b):
    c=[]
    for item in a:
        for i in range(0,len(b)):
            c.append(item+b[i])
    return c

source=r'C:\Users\funw0\Downloads\rosalind_lexf.txt'
f=open(source)
char=f.readline()
n=int(f.readline())
chars=char.split()
chars.sort()

pp=perm(chars,chars)

for i in range(0,n-2):
    pp=perm(pp,chars)

for i in pp:
    print(i)