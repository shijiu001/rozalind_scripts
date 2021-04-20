# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:27:33 2020

@author: funw0
"""


mass_table='''
A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333'''

mt={}
mass_table=mass_table.split()
for aa in range(0,len(mass_table)-1,2):
    mt.update({mass_table[aa]:float(mass_table[aa+1])})

source=r'C:\Users\funw0\Downloads\rosalind_prtm.txt'
f=open(source)
seq=f.readline()
f.close()

w=0
for aa in seq:
    w=w+mt[aa]
print(round(w,3))
    