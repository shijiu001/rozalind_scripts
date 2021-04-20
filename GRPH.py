# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:26:13 2020

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\rosalind_grph.txt'
f=open(sourse)

k=3
ss={}
i=0
edge=[]

for line in f:
    if line.startswith('>'):
        name=line.replace('>','').strip(' ').replace('\n','')
        ss[name]=''
    else:
        ss[name]=ss[name]+line.replace('\n','').strip(' ')
f.close()

kc={}
for key,value in ss.items():
    kc[key]=(value[:k],value[len(value)-k:])
    
for key1,value1 in kc.items():
    for key2,value2 in kc.items():
        if value1[1]==value2[0] and key1!=key2:
            ca=[key1,key2]
            edge.append(ca)
          
for e in edge:
    print(e[0],e[1])            