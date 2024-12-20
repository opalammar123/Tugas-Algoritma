# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 08:36:04 2024

@author: USER
"""

n = int (input("Masukkan nilai n : "))
total = 0
for i in range (1,n+1):
    total +=i
    print(f"Jumlah bilangan dari 1 hingga {n}adalah {total}")