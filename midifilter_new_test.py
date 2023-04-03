# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:53:37 2023

@author: rolfe
"""

### Testing out MidiFilter 

import mido as mido




class Filter:
    '''
    this filter only trigger callbacks with 
    midi messages with a channel property  

    '''    
    def __init__(self, cb_bass, cb_controlchord):
        
        self._cbBass=cb_bass
        self._cb_controlchord=cb_controlchord
        
        self._basschannel=None
        self._controlChordChannel=None
        

    def midichannelBass(self, channel):
        self._basschannel=channel
        print('Filter midichannel bass set: ', channel)
    

    def midichannelChordControl(self, channel):
        self._controlChordChannel=channel
        print('Filter control-chord midi channel bass set: ', channel)
        
    def _onlychannelmessages(self, msg):
        try:
            msg.channel #access attribute to check 
            return True
        except AttributeError:
            return False

    def trigBass(self, msg):
        # here we filter out and make sure all messages 
        # triggered got a channel property
        if not self._onlychannelmessages(msg): 
            print("non cannel msg ignored: ", msg)
            return 
                
        if msg.channel in [self._basschannel]: 
            self._cbBass(msg) #calling callback fun
            
            
    def trigControlChord(self, msg):
        if not self._onlychannelmessages(msg): 
            print("non cannel msg ignored ", msg)
            return 
        
        if msg.channel in [self._controlChordChannel]: 
            self._cb_controlchord(msg) #calling callback fun
    
    
 ### messages triggered always have the channel property   


def main():
    
    def _cbBass(msg):
        print("I am _cbBass: ", msg)
        #https://pynative.com/python-class-variables/
    
    
    def _cbControlChord(msg):
        print("I am _cbControlChord: ", msg)

    
    global msg
    
    msg1=mido.Message('note_on', channel=10, note=64) #a testing 
    msg2=mido.Message('note_off', channel=12, note=64) #a testing 
    msg3=mido.Message('sysex', data=(), time=0) # no channel message
    msg4=mido.Message('clock', time=0)
    msg5=mido.Message('note_off', channel=15, note=64) #a testing 
    msg6=mido.Message('note_on', channel=15, note=64) #a testing 
    msg7=mido.Message('sysex', data=(), time=0) # no channel message
    
    
    f1=Filter(_cbBass, _cbControlChord) #class not instance do not use Filter() only Filter
    
    f1.midichannelBass(10)
    f1.midichannelChordControl(15)
    
    f1.trigBass(msg1) 
    f1.trigBass(msg2) 
    f1.trigBass(msg3)
    f1.trigBass(msg4)
    f1.trigBass(msg5)
    
    f1.trigControlChord(msg6)
    f1.trigControlChord(msg7)
    
    # 1.make a callback 
    # midi.setinPort_chordButtons(ports._....., callbackChord_Control_Buttons) 
    # midi.setinPort_chordButtons(ports._.....,  f1.trigControlChord)  ### try this ....

    

    ###################### OLD CODE
    # -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 13:26:01 2023

@author: rolfe
# """

# from chord_classes1 import MidimsgType
# import mido




# class MidiFilter:
#     #class Attributes:
#     def __init__(self, midimesstypes, callback):
#         #some default values
#         self.channel=0
#         self.midimsgtype=midimesstypes
#         self._reportfilters()
#         self._callback=callback
        
#     def filteroutchannelMessages(object): pass

#     def _reportfilters(self):
#         i=1
#         print('This filter handles these messages:')
#         for property, value in (vars(self.midimsgtype).items()):
#             if not property.startswith('__'): 
#                 print("{} \t {}".format(i, property.ljust(15))) 
#                 i=i+1
                            
#     def filteroutNotebyChannel(self, msg):
#         #return a filter instance for use ...
        
#         if msg.channel == self.channel: #check with property ...
            
#             self._callback(msg)
            
#             return(msg)
#         else:
#             self._callback(None)
            
#             return(None)	
        
        
# def _callback(msg): pass        
        
        
# def callback(msg):
#     print('--- cb ---')    
#     if msg is None: 
#         print("msg ignored")
#     else:
#         print(msg)
           

# #make some messages for test ...
# msg1=mido.Message(MidimsgType.note_off, channel=10, note=64)   
# msg2=mido.Message(MidimsgType.note_on, channel=0, note=64)   
# msg3=mido.Message(MidimsgType.note_off, channel=10, note=64)   
# msg4=mido.Message(MidimsgType.note_off, channel=9, note=44)   

# MidimsgTypes=MidimsgType


# mf1=MidiFilter(MidimsgTypes, _callback)   #construct the filter, load it with messages

# mf1.channel=10

# #one type of filter, there will be more , fill in the channel property before use
# m=mf1.filteroutNotebyChannel(msg1)
# print(m)
# m=mf1.filteroutNotebyChannel(msg2)   
# print(m)
# m=mf1.filteroutNotebyChannel(msg3) 
# print(m)
# m=mf1.filteroutNotebyChannel(msg4) 
# print(m)

# #        #if .... the rest of all Midi message constructors ....
# #        #    mido.new('polytouch', channel=0, note=0, value=0, time=0)
# #        #    mido.new('program_change', channel=0, program=0, time=0)
# #        #    mido.new('aftertouch', channel=0, value=0, time=0)
# #        #    mido.new('pitchwheel', channel=0, value=0, time=0)
# # note_on
# #note_off

# ##no channel info .......        
# #        #    mido.new('sysex', data=(), time=0)
# #        #    mido.new('undefined_f1', time=0)
# #        #    mido.new('songpos', pos=0, time=0)
# #        #    mido.new('song', song=0, time=0)
# #        #    mido.new('undefined_f4', time=0)
# #        #    mido.new('undefined_f5', time=0)
# #        #    mido.new('tune_request', time=0)
# #        #    mido.new('sysex_end', time=0)
# #        #    mido.new('clock', time=0)
# #        #    mido.new('undefined_f9', time=0)
# #        #    mido.new('start', time=0)
# #        #    mido.new('continue', time=0)
# #        #    mido.new('stop', time=0)
# #        #    mido.new('undefined_fd', time=0)
# #        #    mido.new('active_sensing', time=0)
# #        #    mido.new('reset', time=0)
    
    
    
    
    

    
    
    






   
if __name__ == "__main__":

    main()  