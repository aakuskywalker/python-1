# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 07:14:10 2022

@author: Aakriti
"""
import sys
choice=None
num1=None
num2=None
result=None

print("Main Menu:")
print("1. Add")
print("2. Sub")
print("3. Prd")
print("4. Div")
print("5. Rem")
print("6. Exit")
choice=input("Enter your choice:")
choice=int(choice)
if choice==6:
    sys.exit()
    quit()
if choice>6 or choice<1:
    print("wrong input")
    sys.exit()
    quit()
num1=input("Enter first number:")
num2=input("Enter second number:")
num1=int(num1)
num2=int(num2)
if choice==1:
    result=num1+num2
elif choice==2:
    result=num1-num2
elif choice==3:
    result=num1*num2
elif choice==4:
    result=num2/num1
elif choice==5:
    result=num2%num1
else:
    print("wrong input")
print("result:",result)




      