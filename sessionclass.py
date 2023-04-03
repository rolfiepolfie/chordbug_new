# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:51:35 2023

@author: rolfe
"""
  
from dataclasses import dataclass

class Session():
    """
    Contains everything that enables a session 
    These data will be loaded/saved to storage for retrieval     
    """
    @dataclass
    class Data:
        '''
        data used during a typical session setup
        '''
        out_port_index: int
        in_port_index_bass: int
        in_port_index_chord: int
        in_port_index_control: int
        
        midi_channel_in_bass=3 
        midi_channel_in_control_chords=10 
        midi_channel_out=15 
        
        filepath: str
        
        chordScheme: int # or another type
        controlScheme: int
        
        
        
    def __init__(self, mido):
        self._mido=mido
        #self.Data 
        print("NB! - turn down instrument at chord-detect channel at mix")
    
    def userinfo(self):
        pass
    
    def _addFilter(self, filt):
        pass
    
    def _addport(self, ports):
        pass
        
    
    def addMidiChannels(self, md):
        pass
        
    def _addChordScheme(self, chords):
        pass
    
    def _addControlScheme(self, controls):
        pass
        
    def _addUserData(self, structure):
        self.Data = structure ## make a copy?
        


    def new(chords, controls, userdata, filt):
        pass
    
    
    def load():
        pass
    
    def save():
        pass
    
        
    def destruct(self, midi, ports):
        print("- Cleaning up before leaving -")
        print('* sending all notes off')
        midi.sendAllNotesOff()
        print('* sending all sounds off')
        midi.sendAllSoundOff() #needed?
        print('* closing all ports')
        ports.closeAllPorts() 
        ports.report_port_status()
        print('* byebye')
        
        raise SystemExit(0) #clean way to exit , no traceback
        
    def listClassMembers(theObject):
        print([m for m in dir(theObject) if not m.startswith('__')])
        
        
        
class Misc():
    
    def functionalityreport(chords, controls):
        """
        Prints all the chords and controls loaded in this session 
        
        """
        print("\n")
        print("--- CHORDS registered for controller messages in this session---")
        
        for c in chords:
            print("chord name: \t", c.name + " - " + str(c.index))   
            print("triggered by: \t", c.msgtype)
            print("note_cc: \t\t", c.note_cc)
            print("action: \t\t", c.action)
        
        print("\n")
                 
        print("--- CONTROLS registered for controller messages this session ---")
        for c in controls:        
            print("control name: \t", c.name)   
            print("triggered by: \t", c.msgtype)
            print("note_cc: \t\t", c.note_cc)
            print("action: \t\t", c.action)
        
        print("\n")
  
    
    def classname(self): return __class__.__name__
    
    #def isControlChange(msg):
    #    return msg.type == 'control_change'
    
    #def isNote(msg):
    #    return msg.type == 'note_on' or msg.type == 'note_off'
    #    #return msg.type in ('note_on', 'note_off') # alternative
    
    def undefined_CC():
        t1=" Undefined MIDI CC List"

        t2="CC 3 "
        t3="CC 9 "
        t4="CC 14-15 "
        t5="CC 20-31 "
        t6="CC 85-87 "
        t7="CC 89-90 "
        t8="CC 102-119 "
        return t1+t2+t3+t4+t5+t6+t7+t8
        
        
    def listClassMembers(theObject):
        
        for property, value in vars(theObject).items():
            print(property, ":", value)
    
    def printUserprotertiesClass(clas):
        print([ m for m in dir(clas) if not m.startswith('__')])
    
    def clearSpyderTerminal():
        print("\033[H\033[J")  
    

    
    def printTitle(mido, rt, sys): # the app's name .... 
        print("\033[H\033[J")  
        print("  / ____| |                 | |")
        print(" | |    | |__   ___  _ __ __| |")
        print(" | |__  | '_ \ / _ \| '__/ _` |")
        print(" \_____ |_| |_|\___/|_|  \__,_|")    
     ### a testing function ... shall be removed and replaced with Chord-Service  
        print("Python installed: \t", sys.version_info[0], sys.version_info[1])
        print("Mido version:   \t", mido.__version__)
        print("Backend version RT:\t", rt.__version__)
     
     
    def overviewChords():
        return """
                    https://www.pianochord.org/c5.html
            
            C - C major (C△)
            Cm - C minor
            C7 - C dominant seventh
            Cm7 - C minor seventh
            
            Cmaj7 - C major seventh (C△7)
            CmM7 - C minor major seventh
            
            C6 - C major sixth
            Cm6 - C minor sixth
            C6/9 - C sixth/ninth (sixth added ninth)
            
            C5 - C fifth   (interval - 2 notes)
            
            C9 - C dominant ninth
            Cm9 - C minor ninth
            Cmaj9 - C major ninth
            
            C11 - C eleventh
            Cm11 - C minor eleventh
            
            C13 - C thirteenth
            Cm13 - C minor thirteenth
            Cmaj13 - C major thirteenth
            
            Cadd - C add
            C7-5 - C seven minus five
            C7+5 - C seven plus five
            Csus - C suspended
            
            Cdim - C diminished (C°)
            Cdim7 - C diminished seventh (C°7)
            Cm7b5 - C minor seventh flat five (Cø)
            
            Caug - C augmented (C+)
            Caug7 - C augmented seventh
        """
        

     
     
     
    