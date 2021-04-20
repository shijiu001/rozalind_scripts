# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:48:24 2020

@author: funw0
"""


import numpy
sourse=r'C:\Users\funw0\Downloads\rosalind_lgis.txt'
f=open(sourse)
global data
data=f.read().replace('\n',' ').split(' ')
data=list(map(int,data))
n=data[0]
del data[0]

ls=[[],[],[],[]]
dp=[1]*len(data)
for i in range(0,len(data)):
    for j in range(0, i):
        if data[j]>data[i] and (dp[j]+1)>dp[i]:
            dp[i]=dp[j]+1
            ls[0].append(j)
            ls[1].append(i)
            ls[2].append(dp[i])
            ls[3].append(data[i])
            global arr
            arr=numpy.mat(ls)
lis=max(dp)
for t in range(0,arr.shape[1]):
        if arr[2,t]==lis:
            break
global abcd
abcd=[]

def findj(i):
    ll=[]
    for t in range(0,arr.shape[1]):
        if arr[1,t]==i:
            ll.append(t)
            
    new_arr=arr[:,ll[:]]
    a=new_arr[0,numpy.argmax(new_arr[2,:])]
    b=new_arr[3,numpy.argmax(new_arr[2,:])]
    abcd.append(b)
    
    if a not in arr[1]:
        abcd.append(data[a])
        return abcd
    else:
        findj(a)
    
findj(arr[1,t])
incr=abcd[::-1]