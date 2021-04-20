# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:02:40 2020

@author: funw0
"""


sourse=r'C:\Users\funw0\Downloads\rosalind_lgis.txt'
#sourse=r'C:\Users\funw0\Downloads\abcd.txt'
f=open(sourse)
global data
data=f.read().replace('\n',' ').split(' ')
data=list(map(int,data))
n=data[0]
del data[0]

dp=[1]*len(data)
ind=[]
for i in range(0,n):
    ind.append(i)
    
for i in range(0,len(data)):
    for j in range(0, i):
        if data[j]>data[i] and (dp[j]+1)>dp[i]:
        #if data[j]<data[i] and (dp[j]+1)>dp[i]:
            dp[i]=dp[j]+1
            ind[i]=j
            

maxind=dp.index(max(dp))
preind=ind[maxind]

rlis=[]
rlis.append(data[maxind])

while preind != maxind:
    maxind=preind
    rlis.append(data[maxind])
    preind=ind[maxind]
    
lis=rlis[::-1]

for i in range(0,len(lis)):
    print(lis[i],end=' ')
    