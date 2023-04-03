# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 20:59:54 2023

@author: rolfe
"""

from dataclasses import dataclass

count=11

class mytype:
    count=10
    
class notmytype:
    count=22
    

@dataclass
class Returnvalue:
    y0: int
    y1: float
    y3: mytype




class Offer(object):
    Channel = 'Channel'
    CC = 'CC'
    SysEx = 'SysEx'
    
    Types = (
        Channel,
        CC,
        SysEx,
    )
    

mt=notmytype
    
test=Returnvalue(10,11,mt)
