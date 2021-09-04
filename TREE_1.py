# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:18:28 2021

@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\rosalind_tree (1).txt'
f=open(sourse)

data=f.readlines()
edges=[]
for i in range(len(data)):
    if i == 0:
        node = data[i].replace('\n', '')
    else:
        edge = data[i].replace('\n', '').split(' ')
        edges.append(edge)
        
nodes=[]
for i in range(int(node)):
    nodes.append(i+1)



# """    
# 因为树状结构中边的数目一定等于节点数目减1，所以本题的答案是易得的
# 但图论中有关连接表和连接矩阵的概念需要进一步深入