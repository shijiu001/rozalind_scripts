# -*- coding: utf-8 -*-
"""
Created on Sun May 23 01:06:53 2021

@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\abcd.txt'
f=open(sourse)

data=f.readlines()
edges={}
for i in range(len(data)):
    if i == 0:
        node = int(data[i].replace('\n', ''))
        for j in range(node):
            edges[j+1] = 0            
    else:
        edge = data[i].replace('\n', '').split(' ')
        if edges[int(edge[0])] == 0:
            edges[int(edge[0])] = [int(edge[1])]
        else:
            edges[int(edge[0])].append(int(edge[1]))
            
        if edges[int(edge[1])] == 0:
            edges[int(edge[1])] = [int(edge[0])]
        else:
            edges[int(edge[1])].append(int(edge[0]))

nodes=[]            
for i in range(int(node)):
    nodes.append(i+1)
    
for i in range(1,node+1):
    con = edges[i]
    if con != 0:
        if i in nodes:
            nodes[i-1] = -1*nodes[i-1]
        for j in con:
            nodes[j-1] = nodes[i-1]