# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 06:08:49 2022

@author: Aakriti
"""

"""
start=1
result=0
stop=10
avg=None
while start<=stop:
    result+=start
    start+=1
avg=result/10
print(result)
print(avg)
"""
"""
for i in range(1,61,2):
    for j in range(1,61,2):
        print (i,":",j)
  """
"""
from array import array
total=0
avg=0
result=None
arr1=array('i',[78,9,9,23,55,67,8,88,93,56,23,12,4,45,4,5,6,7,8])
print(arr1)  
for i in range(0,len(arr1),1):
    total+=arr1[i]
print(total)   
avg=total/len(arr1)
print (avg) 
print(min(arr1))
print(max(arr1))
n=input("enter any no. to search within an array:")
n=int(n)
for i in range(0,len(arr1),1):
    if arr1[i]==n:
        print("Found at ",i," index")
        result=True
        break
if (result==False):
    print("Not found")
  """

for n in range(11):
    if(n==5):
        break
    print(n)
    
for n in range(11):
    if(n==5):
        continue
    print(n)
    
    





