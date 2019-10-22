#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 01:35:38 2019

@author: shatendra
"""
import copy
import sys
def findIntersectionOfSets(givenset=[],subsets=[]):
    intersection=[]
   # print(givenset)
    #print(subsets)
    tempset=copy.deepcopy(givenset)
    for i in range(len(givenset)):
        for j in range(len(subsets)):
            if givenset[i]==subsets[j]:
                intersection.append(givenset[i])
                tempset.pop(tempset.index(givenset[i]))
    return tempset,intersection
cost=0
subsets=[]
givenset=[]
subsetsizes=[]
weightsetratio=[]
subsetweights=[]
print('Enter the size of set')
setsize=int(input())
print('Enter the values of a set')
for i in range(setsize):
    givenset.append(int(input()))
print('Enter the number of subsets')
nos=int(input())
print('Enter the subsets')
for i in range(nos):
    print('Enter the size of subset {}'.format(i+1))
    subsetsize=int(input())
    subsetsizes.append(subsetsize)
    print('Enter the subset elements')
    subsetelements=[]
    for j in range(subsetsize):
        subsetelements.append(int(input()))
    subsets.append(subsetelements)
    print('Enter the weights of subsets')
    subsetweights.append(int(input()))

globalcost=0
while len(givenset)>0:
    subsetslist=[]
    tempcost=[]
    givenlist=[]    
    for i in range(nos):
        given,intersection=findIntersectionOfSets(givenset,subsets[i])
        subsetslist.append(intersection)
        if len(intersection)>0:
            tempcost.append(subsetweights[i]/len(intersection))
        else:
            tempcost.append(sys.maxsize)
        givenlist.append(given)
    minimumcost=min(tempcost)    
    minindex=tempcost.index(minimumcost)
    newmincost=subsetweights[minindex]
    givenset=givenlist[minindex]
    globalcost+=newmincost

print('The minimum weight for set cover is {}'.format(globalcost))