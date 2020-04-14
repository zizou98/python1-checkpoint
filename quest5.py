# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:15:59 2020

@author: azizb
"""
string=str(input("entrer une chaine "))
result = "" 
for i in range(len(string)):
    if i % 2 == 0:
      result = result + string[i]
print(result)

