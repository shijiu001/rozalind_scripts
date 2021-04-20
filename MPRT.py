# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:54:30 2020

@author: funw0
"""


import requests
import re

sourse=r'C:\Users\funw0\Downloads\rosalind_mprt.txt'
f=open(sourse)

purl=[]
url=[]

for line in f:
    purl.append(line.replace('\n',''))
f.close()

for etr in purl:
    url.append('http://www.uniprot.org/uniprot/'+etr+'.fasta')

for iurl in url:
    r=requests.get(iurl)
    fa=open('bbb.fasta','a')
    fa.write(r.text)
fa.close()

ss={}
t=0
fa=open('bbb.fasta')
for line in fa:
    if line.startswith('>'):
        name=purl[t]
        t+=1
        ss[name]=''
    else:
        ss[name]=ss[name]+line.replace('\n','').strip(' ')
fa.close()

motif=re.compile(r'N[^P][ST][^P]')
for key,value in ss.items():
    mtc=motif.finditer(value)
    print(key)
    for i in mtc:
        print(i.start()+1,end=' ')
    print('\n')