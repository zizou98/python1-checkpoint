# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:10:44 2020

@author: azizb
"""
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(str(year)+" is a leap year")
       else:
           print(str(year)+"is not a leap year")
   else:
       print(str(year)+"is a leap year")
else:
   print(str(year)+"is not a leap year")
   


