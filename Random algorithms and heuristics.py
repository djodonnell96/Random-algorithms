# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:24:35 2016

@author: Dennis
"""

import random

def lasVegasSearch (A):
    found = False
    while not found:
        temp = random.choice(A)
        if temp == 'a':
            found = True
    return temp
    
def monteCarloSearch (A,k):
    i=0
    found = False
    while not found or i == k:
        temp = random.choice(A)
        if temp == 'a':
            return temp
            found = True
        i+=1+i
        
A = ['a','a','a','b','b','b']
print(str(lasVegasSearch(A)))
print(str(monteCarloSearch(A, len(A))))