#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 00:50:24 2024

@author: mathildajonsson
"""


originalList = [3,   4, 4,   3, 2,   5, 1,   3, 3,   9, 3,   3]

#originalList = originalList.split()

index = 0

listA =[]
listB =[]

for index in range(len(originalList)):
    if index % 2 == 0:
        listA.append(originalList[index])
    elif index % 2 == 1:
        listB.append(originalList[index])

for x in range(len(listA)):
   listA[x] = float(listA[x])
   listB[x] = float(listB[x])


print(len(listA))
print(len(listB))
print('listA')
print(listA)

print('listN')
print(listB)
totDistance = 0
disance = []

for y in range(len(listA)):
#    A=listA[y]
 #   B=listB[y]
  #  A= [int(A)]
   # B= [int(B)]
   print(listA[y])
   nrOfTimes = listB.count(listA[y])
   print(nrOfTimes)
   disance = listA[y] * nrOfTimes
   totDistance = totDistance + disance
    
print(totDistance)
