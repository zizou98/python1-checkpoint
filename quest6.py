# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:22:30 2020

@author: azizb
"""
price=float(input("entrer la valeur de votre prix "))
if price>=500:
    price=price/2
elif(price>=200 and price<500):
    price=price*0.7
else:
    price=price*0.9
print (price)
