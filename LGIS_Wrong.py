# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:01:31 2020

@author: funw0
"""


import numpy

def cal_de(xyz):
    a=xyz[:,2].tolist()
    a_index=a.index(max(a))
    a_max=int(max(a))
    print(int(xyz[a_index][1]),end=' ')
    
    n=len(a)
    ls=[]
    for i in range(a_index,n):
        if xyz[i][1]<xyz[a_index][1]:
            ls.append(i)
    new_xyz=xyz[ls[:]]
            
    if a_max==0:
        return
    else:
        cal_de(new_xyz)
        
def cal_in(xyz):
    a=xyz[:,3].tolist()
    a_index=a.index(max(a))
    a_max=int(max(a))
    print(int(xyz[a_index][1]),end=' ')
    
    n=len(a)
    ls=[]
    for i in range(a_index,n):
        if xyz[i][1]>xyz[a_index][1]:
            ls.append(i)
    new_xyz=xyz[ls[:]]
            
    if a_max==0:
        return
    else:
        cal_in(new_xyz)
    

sourse=r'C:\Users\funw0\Downloads\abcd.txt'
f=open(sourse)

data=f.read().replace('\n',' ').split(' ')
data=list(map(int,data))
n=data[0]
del data[0]

comp_de=[]
for i in range (0,n):
    comp_de.append(0)
    for k in range(i,n):
        if data[i]>data[k]:
            comp_de[i]+=1
comp_in=[]
for i in range (0,n):
    comp_in.append(0)
    for k in range(i,n):
        if data[i]<data[k]:
            comp_in[i]+=1    


xyz=numpy.zeros((n,4))

for i in range(0,n):
    xyz[i,0]=i
for i in range(0,n):
    xyz[i,1]=data[i]
for i in range(0,n):
    xyz[i,2]=comp_de[i]
for i in range(0,n):
    xyz[i,3]=comp_in[i]
    

cal_in(xyz)
print('')
cal_de(xyz)