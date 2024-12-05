#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:14:38 2024

@author: VenilaM
"""

originalFile = open("input.txt", "r")

originalList = originalFile.read()

originalList = originalList.split()

index = 0

listA =[]
listB =[]

for index in range(len(originalList)):
    if index % 2 == 0:
        listA.append(originalList[index])
    elif index % 2 == 1:
        listB.append(originalList[index])
    pass

for x in range(len(listA)):
   listA[x] = float(listA[x])
   listB[x] = float(listB[x])
print('listA')
print(listA)

#
print('listN')
#
print(listB)
listA.sort()
listB.sort()



totalDisance = 0
y = 0
for y in range(len(listA)):
#    A=listA[y]
 #   B=listB[y]
  #  A= [int(A)]
   # B= [int(B)]
    totalDisance += abs(listA[y]-listB[y])
print(totalDisance)