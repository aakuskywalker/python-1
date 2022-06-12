# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 06:41:23 2022

@author: Aakriti
"""
"""
from array import array
arr1=array('i',[1,2,3,4,5])
print(arr1)
print(type(arr1))
print(isinstance(arr1,array))
print(id(arr1))
print(max(arr1))
print(min(arr1))
print(sum(arr1))
print(len(arr1))
"""
"""
#exploring array class
print(dir(array))
print(help(array))
"""
"""
#append(self, v, /)
arr1.append(9)
print(arr1)
arr1.append(6)
print(arr1)

#count(self, v, /)
res=arr1.count(3)
print(res)
arr1.append(9)
res2=arr1.count(9)
print (res2)
res3=arr1.count(10)
print(res3)
"""

from array import array
arr1=array('i',[1,8,7,6,7,8,9,0,5,5,4,5,34,45,23,13,4,5,6,7,1,1,1,2,3,4,5,6,7,8,9,0,0,0,8,7,6,5,5,4,3,3,3,2,1,6])
print(arr1.count(8))
result=arr1.index(8)
print(result)

"""
#extend(self, bb, /)
print(len(arr1))
arr1.extend([1,2,3,4,5,6,7,8,9,0])
print(arr1)
print(len(arr1))
arr1.extend((1,2,3,4,5))
print(len(arr1))
print(arr1)
arr2=array('i',[4,5,3,7,1,9,6,4])
arr1.extend(arr2)
print(len(arr1))
print(arr1)
"""