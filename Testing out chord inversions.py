# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 16:21:40 2023

@author: rolfe
"""

### Testing out chord inversions 

"""

These inversions can be done from any ocntinuous controllers 
like expression pedal , potmeters 

"""

from chord_classes1 import ChordIndex
import numpy


# a shift is needed max 4 times 

#ChordIndex.printAllChords(ChordIndex)


cmajor=ChordIndex.C_major


print(cmajor)   


def afunction(test):
    MESSAGE1=100
    MESSAGE2=100
    
    
print(afunction.MESSAGE1)
    
    
        
        
class ChordMan():
    """
    Different methods uasing to manipulate chords 
    
    nb! 
    """
    class direction:
        up=1
        down=2

        
    def __init__(self, chord):
        self._numbers_shifted=0
        self.chord = chord
        
    def rollchord(self, rolltype=direction.up):
        if len(self.chord)==0: return
        
        if rolltype == self.direction.up:
            self._numbers_shifted -=1
            self.chord= numpy.roll(self.chord,1).tolist()
        
        if rolltype == self.direction.down:
            self._numbers_shifted +=1
            self.chord= numpy.roll(self.chord,-1).tolist()
        
        
    def octave_updown():
        pass
    
    def spread(): pass
    
    def collect(): pass


d=ChordMan.direction

cm=ChordMan(cmajor)           
        
print("original: ", cmajor)

cm.rollchord(d.up)
print("shifted left: ", cm.chord) 

cm.rollchord(d.down)
print("shifted left: ", cm.chord) 
cm.rollchord(d.down)
print("shifted left: ", cm.chord) 
cm.rollchord(d.down)
print("shifted left: ", cm.chord) 
cm.rollchord(d.down)
print("shifted left: ", cm.chord) 
#print("shifted right: ", shifted)  #returns an array ... need list 
print(cm._numbers_shifted)
#shifted=cm.rollchord(shifted, Rolltype.left)