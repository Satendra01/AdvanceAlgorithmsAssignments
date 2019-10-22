#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:56:18 2019

@author: shatendra
"""
import operator,sys
keyvalpair={}
def loadBalancing(machines,jobweights=[]):
    machinelist=[0]*machines
    occupiedlength=[0]*machines
    keyvalpair={}
    for i in range(len(machinelist)):
        occupiedlength[i]=0
    for j in range(len(jobweights)):
        minimum=sys.maxsize
        minindex=-1
        for k in range(len(occupiedlength)):
            if occupiedlength[k]<minimum:
                minimum=occupiedlength[k]
                minindex=k
        occupiedlength[minindex]+=jobweights[j]
        if bool(keyvalpair)==False:
            jobslist=[]     
            jobslist.append(j+1)
            keyvalpair[minindex]=jobslist
        else:
            flag=0
            for key in list(keyvalpair.keys()):
                if key==minindex:
                    flag=1
                    break
            if flag==1:
                value=list(keyvalpair[key])
                value.append(j+1)
                tempdict={key:value}
                keyvalpair.update(tempdict)
            else:
                jobslist=[]     
                jobslist.append(j+1)
                keyvalpair[minindex]=jobslist
    maximumoccupiedduration=max(occupiedlength) 
    maxindex=occupiedlength.index(max(occupiedlength))
    print("The machine which has maximum load is {} and the maximum load is {}".format(maxindex+1,maximumoccupiedduration))
    print("The list of jobs at the {} machine is {}".format(maxindex+1,keyvalpair[maxindex]))

print('Enter the no of machines')
machines=int(input())
print('Enter the no of jobs')
jobs=int(input())
print('Enter the jobs weights')
jobweights=[]
for i in range(jobs):
    jobweights.append(int(input()))
loadBalancing(machines,jobweights)