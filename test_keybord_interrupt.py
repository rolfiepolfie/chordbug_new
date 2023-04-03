# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:43:42 2023

@author: rolfe
"""

### TEst out keyboard listener



#from pynput.keyboard import *
import keyboard


def press_on(key):
    print("press on")
    
    
def press_off(key):
    pass
    
    
    
#1. create a infinite loop

#2 create a custom keyboard interrupt that breaks the lopp in a controlled way 

def testyield():
    
    MESSAGE=100
    
    
    for i in range(10):
        yield MESSAGE


    
#    try:
#        while True:
#            ...
#            ...
#    except KeyboardInterrupt:
#        exit

def main():
    msg=testyield()
    print(msg)    
    
    
    def thebreak():
        print("send a panic message ...")
       
        raise SystemExit(0) #clean way to exit , not traceback
        #https://stackoverflow.com/questions/25928377/how-to-exit-a-script-in-spyder
        
        
        
        
    while True:
        if keyboard.read_key() == "p":
            print("You pressed p")
            thebreak()
            break
        



    
    
    
    

  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
    
    
    