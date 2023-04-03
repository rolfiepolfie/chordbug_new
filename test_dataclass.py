# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:40:14 2023

@author: rolfe
"""

from dataclasses import dataclass


@dataclass
class Returnvalue:
    y0: int
    y1: float
    y3: int
    
        
    
def total_cost(x):
    y0 = x + 1
    y1 = x * 3
    y2 = y0 ** y1
    
    return Returnvalue(y0, y1, y2)

dc=total_cost(1)
print(dc.y0)
print(dc.y1)


class test:
    @dataclass
    class Returnvalue2:
        y0: int
        y1: float

    
    

    def calc(self, x):
        y=x+1
        return test.Returnvalue2(y, 1.2)
    
    
t=test()  

#rv=t.Returnvalue2


ans=t.calc(2)

print(ans.y1)


  
    
        
        
        
