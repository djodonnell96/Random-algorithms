# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:24:35 2016

@author: Dennis
"""

import random

#Choose random character from list, check if it's the right one
def lasVegasSearch (A):
    found = False
    while not found:
        temp = random.choice(A)
        if temp == 'a':
            found = True
    return temp
    
#Check if a random character in the list is your desired character k times
def monteCarloSearch (A,k):
    i=0
    found = False
    while not found or i == k:
        temp = random.choice(A)
        if temp == 'a':
            return temp
            found = True
        i+=1+i
        
def checkSorting(A):
    if A == sorted(A):
        return True
    else:
        return False
            
def bogosort(A):
    while checkSorting(A) == False:
        random.shuffle(A)
    return A