# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:02:46 2020

@author: funw0
"""


import requests

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


for key,value in ss.items():
    print(key)
    i=0
    while i < len(value)-4:
        if value[i]=='N' and value[i+1]!='P' and (value[i+2]=='S' or value[i+2]=='T') and value[i+3] != 'P':
            print(i+1,end=' ')
        i+=1
    print('\n')