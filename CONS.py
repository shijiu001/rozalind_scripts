# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:55:33 2020

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\rosalind_cons.txt'
f=open(sourse)


'''生成一个二级列表mt，模仿矩阵，用于储存序列'''
mt=[]
i=-1
seq=''

for line in f:
    if line.startswith('>'):
        i=i+1
        mt.append('')
    else:
        mt[i]=mt[i]+line.replace('\n','').strip(' ')
f.close()


'''生成一个二级列表acgt，模仿矩阵，用于储存碱基出现频率'''
#首先将其充满足够长度的0
i=0
acgt=[[],[],[],[]]
mu=[]
cons=[]
l=len(mt[0])

while i<l:
    acgt[0].append(0)
    acgt[1].append(0)
    acgt[2].append(0)
    acgt[3].append(0)
    mu.append(0)
    cons.append('')
    i=i+1

#接下来统计碱基出现频率
i=0
n=0
while i<len(mt):
    while n<l:
        if mt[i][n]=='A':
            acgt[0][n]+=1
        if mt[i][n]=='C':
            acgt[1][n]+=1
        if mt[i][n]=='G':
            acgt[2][n]+=1
        if mt[i][n]=='T':
            acgt[3][n]+=1
        n+=1
    i+=1
    n=0
    
'''选择每个位点出现次数最多的碱基'''
i=0
n=0

#首先得出每个位点最大的频率是多少
while n<l:
    mu[n]=max(acgt[0][n],acgt[1][n],acgt[2][n],acgt[3][n])
    n+=1

#接下来将每个位点出现频率最多的碱基存储如列表cons，因为可能存在一个位点两个碱基出现频率相同且都为最大，所以使用了列表'
n=0
while n<l:
    if acgt[0][n]==mu[n]:
        cons[n]=cons[n]+'A'
    if acgt[1][n]==mu[n]:
        cons[n]=cons[n]+'C'
    if acgt[2][n]==mu[n]:
        cons[n]=cons[n]+'G'
    if acgt[3][n]==mu[n]:
        cons[n]=cons[n]+'T'
    n+=1

n=0
while n<l:
    print(cons[n][0],end='')    #输出时仅输出其中一种'
    n+=1