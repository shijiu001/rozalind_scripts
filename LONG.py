# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 00:25:32 2020
    !!!参见https://leetcode-cn.com/problems/find-the-shortest-superstring/solution/zui-duan-chao-ji-chuan-by-leetcode/
@author: funw0
"""

sourse=r'C:\Users\funw0\Downloads\rosalind_long.txt'
fasta=open(sourse)


ss=[]
seq=''
for line in fasta:
    if line.startswith('>'):
        if seq!='':
            ss.append(seq)
        seq=''        
    else:
        seq=seq+line.replace('\n','').strip(' ')
ss.append(seq)

fasta.close()

N=len(ss)
ovl=[[0] * N for _ in range(N)]

for i, x in enumerate(ss):
    for j, y in enumerate(ss):
        if i != j:
            for ans in range(min(len(x),len(y)), -1, -1):
                if x.endswith(y[:ans]):
                    ovl[i][j]=ans
                    break

dp=[[0]*N for _ in range(1<<N)]
parent=[[None]*N for _ in range(1<<N)]
for mask in range(1,1<<N):
    for bit in range(N):
        if (mask>>bit) & 1:
            pmask=mask^(1<<bit)
            if pmask==0:
                continue
            for i in range(N):
                if (pmask>>i) & 1:
                    value=dp[pmask][i]+ovl[i][bit]
                    if value > dp[mask][bit]:
                        dp[mask][bit]=value
                        parent[mask][bit]=i
                        
                        
perm=[]
mask=(1<<N)-1
i=max(range(N), key=dp[-1].__getitem__)
while i is not None:
    perm.append(i)
    t=parent[mask][i]
    mask=mask^(1<<i)
    i=t
    
perm=perm[::-1]
seen=[False]*N
for x in perm:
    seen[x]=True
perm.extend([i for i in range(N) if not seen[i]])

ans=ss[perm[0]]
for i in range(1,len(perm)):
    overlap=ovl[perm[i-1]][perm[i]]
    ans=ans+ss[perm[i]][overlap:]