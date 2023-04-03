# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:55:20 2023

@author: rolfe
"""

import numpy as np

a=1

def f1(a):
    return 11


def f2(b=f1(a)):
    return b


# ---------------------
print(f2(44))


r=np.random.binomial(size=100, n=10, p=0.5)


#from numpy import random

#x = random.binomial(n=10, p=0.5, size=10)

print(r)

