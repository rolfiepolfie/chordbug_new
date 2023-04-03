# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 03:12:16 2022

@author: rolfe
"""

# chord_classes1.py

import time
import copy
import keyboard
from chord_classes2 import CCvalues





class ChordIndex_simpler:
    
    def printAllChords(theObject):
        i=0
        for property, value in (vars(theObject).items()):
            if property.startswith('C'): 
                i=i+1
                print("{}\t {}  {}".format(i, property.ljust(15), value))
            
    C_major =           [0,4,7]
    C_minor =           [0,3,7]
    C_7_major    =      [0,4,7,10]
    C_7_minor =         [0,3,7,10]
    
    C_sus2=             [0,2,7]         #does C_sus2 add7 exist?
   
    C_maj_minor   =     [0,3,7,11]
    C_maj_major=        [0,4,7,11]      #Cmaj = C7 with sharpen7 (dominant7)
    
    C_major_add2=       [0,2,4,7]
    
    C_6_major=          [0,4,7,9]       
    C_6_minor   =       [0,3,7,9]
    
    C_aug=              [0,4,8]          #C+
    C_aug_add7=         [0,4,8,10]
    
    C_9_major=          [0,4,7,10,14]    #C7 add9   - the 9th imply 7th
    C_9_minor=          [0,3,7,10,14]    #sharpen the 7 to get an variation?
        
    C_dim=              [0,3,6]
    C_dim_add7=         [0,3,6,10]  #is really Cm7(b5)  
    C_dim_add6=         [0,3,6,11] # real name is Cdim7  (I think: flat7)

class ChordIndex_simple:
    
    def printAllChords(theObject):
        i=0
        for property, value in (vars(theObject).items()):
            if property.startswith('C'): 
                i=i+1
                print("{}\t {}  {}".format(i, property.ljust(15), value)) 
            
    C_major =           [0,4,7]
    C_minor =           [0,3,7]
    C_7_major    =      [0,4,7,10]
    C_7_minor =         [0,3,7,10]
    
    C_sus2=             [0,2,7]         #does C_sus2 add7 exist?
   
    C_maj_minor   =     [0,3,7,11]
    C_maj_major=        [0,4,7,11]      #C7 with sharpen7
    
    C_major_add2=       [0,2,4,7]
    C_major_add9=       [0,4,7,13]      #not  a real 9th chord , missing 7th

    
    C_6_major=          [0,4,7,9]        #same as C6
    C_6_minor   =       [0,3,7,9]
    
    C_aug=              [0,4,8]          #C+
    C_aug_add7=         [0,4,8,10]
    
    C_9_major=          [0,4,7,10,14]    #C7 add9   - the 9th imply 7th
    C_9_minor=          [0,3,7,10,14]
    C_9_maj_major=      [0,4,7,11,14]    #C9 sharpen7
    C_9_flat7_major=    [0,4,7,9,14]     #C6/9 , flat7 = 6
    C_9_flat7_minor=    [0,3,7,9,14]   
        
    C_dim=              [0,3,6]
    C_dim_add6=         [0,3,6,10] #is really Cdim7
    C_dim_add7=         [0,3,6,11] #is really Cm7(b5) 
    
    
class ChordIndex:
    """
    A collection of all chords possible that could be made use of ...
    """
    def printAllChords(theObject):
        i=0
        for property, value in (vars(theObject).items()):
            if property.startswith('C'): 
                i=i+1
                print("{}\t {}  {}".format(i, property.ljust(15), value))
            
    # 7th = index 10
    # maj = index 11     maj = sharpen7
    # 9th = index 13
    # 11th = index 16
    # 13th = index 20
    #https://www.pianochord.org/

    C_major =           [0,4,7]
    C_7_major    =      [0,4,7,10]
    C_7_minor =         [0,3,7,10]
    C_7_flat5   =       [0,4,6,10]   #does Cminor_flat5 exist? = yes: Cdim ,, Cmajor flat5?
    C_7_addsharp9 =     [0,4,7,10,15]
    
    C_maj_minor   =     [0,3,7,11]
    C_maj_major=        [0,4,7,11]   #C7 with sharpen7
    
    C_major_add2=       [0,2,4,7]
    C_major_add9=       [0,4,7,13]  #not  a real 9th chord , missing 7th
    
    C_6_major=          [0,4,7,9]    #same as C6
    C_6_minor   =       [0,3,7,9]
    C_6_add9_major=     [0,4,7,9,14]     #C6/9 , flat7 = 6
    C_6_add9_minor=     [0,3,7,9,14] 
    
    C_minor =           [0,3,7]

    C_aug=              [0,4,8]           #C+
    C_aug_add7=         [0,4,8,10] #Caug_minor exist?
        
    #The note for 9th chord is always the same , not sharpen nor flatten
    C_9_major=          [0,4,7,10,14]    #C7 add9   - the 9th imply 7th
    C_9_minor=          [0,3,7,10,14]
    C_9_maj_major=      [0,4,7,11,14]    #C9 sharpen7
   
    C_9_flat7_minor=    [0,3,7,9,14]   

    C_sus2=             [0,2,7]          #does C_sus2 add7 exist?
    C_sus4=             [0,5,7]
    C_sus2_add9=        [0,2,7,10,14]
    C_sus2_add7=        [0,2,7,10] 
    C_sus4_add9=        [0,5,7,10,14]
    C_sus4_add7=        [0,5,7,10] 
    
    #sus chords can be added with 7 and 9 or only7?
    
    C_dim=              [0,3,6]
    C_dim_add6=         [0,3,6,10] #is really Cdim7
    C_dim_add7=         [0,3,6,11] #is really Cm7(b5) 
    
    C_11_major=         [0,4,7,10,14,17]  
    C_11_minor=         [0,3,7,10,14,17]  
    
    C_13_major=         [0,4,7,10,14,17,21]  #same as: C7 in addition to D_minor
    C_13_minor=         [0,3,7,10,14,17,21]
    C_13_maj=           [0,4,7,11,14,17,21]  # sharp7 
    
    #C13 with a 7th = dominant 13 
    # ---


#1.control: convert minor
#2.control: add7
#3.control: sharpen the 7th
#4.control: add 2

#collect all small classes in a datatypes class ?

class MidimsgType():  
    note_on = 'note_on'
    note_off = 'note_off' 
    controlchange = 'control_change'
    programchange = 'program_change'
    sysex_data = 'sysex_data'
    pitchwheel = 'pitchwheel'
    aftertouch = 'aftertouch'
    
class Actiontype:
    momentary = 'momentary'
    toggle = 'toggle'
    other = 'other'


class Midimess:
    def __init__(self, msg):
    
        self.type = msg.type


        if msg.type == 'note_on' or msg.type == 'note_off':
            self.channel = msg.channel
            self.velocity=msg.velocity
            self.note = msg.note
        
        if msg.type == 'control_change':
            self.control=msg.control
            self.value =msg.value
            self.channel = msg.channel
            
        if msg.type == 'program_change':
            pass
            
    def isnoteOn(self, msg): return msg.type == MidimsgType.note_on and msg.velocity > 0
    def isnoteOff(self, msg): return msg.type == MidimsgType.note_on and msg.velocity == 0 or msg.type == MidimsgType.note_off
    def isControlChange(self, msg): return msg.type == MidimsgType.controlchange
    def isProgramChange(self, msg): return False
    def totext(self):
        
        if self.type == 'control_change':
            if self.control==0: return "" #sensor fcb bug
            return "{} \t control:{} ch:{} val:{}".format("CC", self.control, self.channel, self.value)
        
        if self.type == 'note_on' or self.type == 'note_off':
            return "{} \t note:{} ch:{} vel:{}".format(self.type, self.note, self.channel, self.velocity)
        
        else: 
            #return "unsup mess: " + str(self.type) #enable this line if you want to show unnsop messages
            return ''

        

class Control:
    """
    Base class for all user defined controls
    """
    # def printall(Object): #move to the Control class ?
    #     i=0
    #     for property, value in (vars(Object).items()):
    #         #if not property.startswith('_'): 
    #         i=i+1
    #         print("{}\t {}  {}".format(i, property.ljust(15), value))
                
    
        
class Controls:
    __doc__="""
    A collection of controls with their function
    """
    #def printall(Object): super(Control, obj) 
    def printall(Object): 
        print("all possible controls that can be handled if  assigned to a midi message: ") 

        i=0
        for property, value in (vars(Object).items()):
            if not property.startswith('__'): 
                if not property.startswith('printall'): 
                    i=i+1
                    #print("{}\t {}  {}".format(i, property.ljust(15), value))
                    print("{}\t {}  ".format(i, property.ljust(15)))


    class freezeRoot(Control):
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')

            """
            Freeze, means that the bass input do not change the root 
            of the cord
            These Controls classes got a optional constructor, but also have the 
            note_cc=value as a default value 
            """
            self.name = "FreezeRoot_control"
            self.msgtype=[MidimsgType.note_on, MidimsgType.note_off]
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None):
            #Globals, msgtype,note_cc,mess=arg 

            global global_Control_disable_chord_root
            print("evoked: ", self.name)
            global global_Control_disable_chord_root
                       
            Globals, msgtype, note_cc, mess = arg
            
            if msgtype == MidimsgType.note_on:
                Globals.global_Control_disable_chord_root = True
            
            if msgtype == MidimsgType.note_off:
                Globals.global_Control_disable_chord_root = False
                
    class add_seventh(Control):
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            
            self.name = "Add_7th_control"
            self.msgtype=[MidimsgType.note_on]
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None):
            """
            take current chord , return converted chord  , no need for retrig
            """
            Globals, msgtype,note_cc,mess=arg 
            print(note_cc)

            
    class convert_to_minor(Control):
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
            
            self.name = "Convert chord to minor"
            self.msgtype=[MidimsgType.note_on]
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None):
            """
            take current chord, return converted minor chord, re-play 
            """
            Globals, msgtype,note_cc,mess=arg 
           
            print(note_cc)
    
    class slash_transpose_minus5_chord_minor7(Control):
        """
        Transpose -5 , then engage the minor seven  chord
        
        """
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
            
            self.name = "Slash_transpose_minus5_chord_minor7"
            self.msgtype=[MidimsgType.note_on] #rename to trigger Messages
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None): 
            Globals, msgtype,note_cc,mess=arg 
            pass

        
        
    class chordroot_silentmode(Control):
        """
        The idea is: solves the problem selecting a chord_root with the foot controller
        with help of feks pressure-parameter or unusual midi parameter
        """
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
            
            self.name = "chordroot_silentmode"
            self.msgtype=[MidimsgType.note_on] #rename to triggerMessages
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None): 
            Globals, msgtype,note_cc,mess=arg 
            pass
        
    
    class first_alteration_chord(Control):
        """
        for example: when sus accord is engaged
        this control will select the first alteration in the alteration=[...] list 
        in this case between sus2 and sus4
        
        """
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
            
            self.name = "Slash_transpose_minus5_chord_minor7"
            self.msgtype=[MidimsgType.note_on, MidimsgType.note_off] #rename to triggerMessages
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None): 
            Globals, msgtype,note_cc,mess=arg 
            pass

    class read_chord_keyboard(Control):
        """
        if you need a special chord not registered 
        this will read a chord from the pianist's keyboard
        """
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
            
            self.name = "read_chord_right_hand"
            self.msgtype=[MidimsgType.note_on, MidimsgType.note_off] #rename to triggerMessages
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None):
            #change to these parameter names to add to the understanding 
            #of that paramters exept globals are attributes of mess
            Globals, mess_msgtype, mess_note_cc, mess=arg 
            pass

    class invert_chord(Control):
        """
        engage inversions of a chord 
        this could be done by an expression pedal up or down 
        """
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
            
            self.name = "invert_chord"
            self.msgtype=[MidimsgType.controlchange] #rename to triggerMessages
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None): 
            Globals, msgtype,note_cc,mess=arg 
            pass
    
    
    class sequence_chords(Control):
        """
        idea: make a list of chords
        sequence trough them with a pedal press
        """
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
            
            self.name = "sequence_chord"
            self.msgtype=[MidimsgType.note_on] #rename to triggerMessages
            self.note_cc=note_cc
            self.action=Actiontype.momentary
        
        def function(self, arg=None): 
            Globals, msgtype,note_cc,mess=arg 
            pass

   
    class special_control(Control):
        """
        experimental control for testing new features
        """
        #name="special control dummy message---fix this"
        
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc

            self.name = "special control that needs special handling! "
            self.msgtype=[MidimsgType.controlchange] #change to msgtrig=[]
            
            self.note_cc=note_cc #change to note_cc trig
            self.action=Actiontype.toggle
        
        #in controls using CC, we also can make use of the CC.val paramter 
        # distnguish down and up knob changes
        def function(self, arg=None):
            
            def detectUpDown(msg, _callbackup, _callbackdown):
                pass
                
                
            
            Globals, msgtype, note_cc, mess=arg # mess parameter contains everything
            
            #if self.msgtypetrig in [control] ... [notes .... ] etc ...
            
            ##
            ## Here I simulate noteon/off with 
            ## the message control+control.value  
            ##
            if msgtype == MidimsgType.controlchange:
                if mess.value > 0: 
                # if we define msgtype as [MidimsgType.controlchange,.. , 
                # we should not need this check
                # we can access the val paramter in mess
                #print("special control: ")
                #print("cc: ", note_cc)
                #print("val: ", mess.value)
                    print("DOWN")
                else:
                   print("UP")
               
            
        
class Chord:  # all chords are instance of this class , isinstance....()
    """
    Base class for all user defined chords
    """
    def classname(): return "Chord"
    
class Chords:
    """
       msgtype and note..cc are all lists
       Class structure of chord indexes and its names 
       ChordId.dim.index = [0, 3, 6, 9] \n
       ChordId.dim.name = 'Dim'
       
    """
    def printall(Object):
        print("\n -- chords class structure, chords that can be invoked if  assigned to a midi message: ") 
        i=0
        for property, value in (vars(Object).items()):
            if not property.startswith('__'): 
                if not property.startswith('printall'): 
                    i=i+1
                    print("{}\t {} ".format(i, property.ljust(15)))
                
    class major(Chord):
        """
        Comments goes here
        """
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_major
        name= Chord.classname() + " - Major"
        msgtype=[MidimsgType.note_on]
        note_cc=[60] #default value if constructor not used
        action=Actiontype.momentary
           
    class sus4(Chord):
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index= ChordIndex.C_sus4
        name= Chord.classname() + " - Sus2" 
        msgtype=[MidimsgType.note_on]
        note_cc=[61]
        action=Actiontype.momentary
        alternations =["sus4", "add7", "add9"] # new idea to help algorithm def function(self, arg=None): pass

        
        def function(self, arg=None): pass
    
    class minor(Chord):
        def __init__(self, note_cc): 
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_minor
        name = Chord.classname() + " - Minor"
        msgtype=[MidimsgType.note_on]
        note_cc=[62]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
    class normal_7th(Chord):  #not the maj7 or sharped 7
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_7_major
        name= Chord.classname() + " - 7th-septim"
        msgtype=[MidimsgType.note_on]
        note_cc=[63]
        action=Actiontype.momentary
        def function(self, arg=None): pass
    
    
    class normal_6th(Chord):  #not the maj7 or sharped 7
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_6_major
        name= Chord.classname() + " - 6th"
        msgtype=[MidimsgType.note_on]
        note_cc=[70]
        action=Actiontype.momentary
        def function(self, arg=None): pass
    
    
    class maj7(Chord): #sharpen 7th
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index=ChordIndex.C_maj_major
        name=Chord.classname() + " - maj7-sharpen7th"
        msgtype=[MidimsgType.note_on]
        note_cc=[64]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
    class minor7(Chord):
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index=ChordIndex.C_7_minor
        name=Chord.classname() + " - Minor7"
        msgtype=[MidimsgType.note_on]
        note_cc=[65]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
        
    class dim(Chord):  
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_dim 
        name= Chord.classname() + " - Dim"
        msgtype=[MidimsgType.note_on]
        note_cc=[66]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
        
    class aug(Chord):
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index= ChordIndex.C_aug
        name = Chord.classname() + " - augmented"
        msgtype=[MidimsgType.note_on]
        note_cc=[67]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
        
    class nine9(Chord):
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index = ChordIndex.C_9_major
        name= Chord.classname() + " - 9th"
        msgtype=[MidimsgType.note_on]
        note_cc=[69]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
    class major11(Chord):
        def __init__(self, note_cc): #make constructor on all classes?
            if type(note_cc) != list: raise TypeError('__init__ parameter value must be a list []')
            self.note_cc=note_cc
        index= ChordIndex.C_11_major
        name = Chord.classname() + " - 11th"
        msgtype=[MidimsgType.note_on]
        note_cc=[70]
        action=Actiontype.momentary
        def function(self, arg=None): pass
        
    ## sus 2 + 7 = 9th chord
    
    # def invertChordLeft(self, chordId):
    #     it=deque(self, chordId)
    #     it.rotate(1)    
    #     return(list(it)) 
      
    # def invertChordRight(chordId):
    #     it=deque(chordId)
    #     it.rotate(-1)    
    #     return(list(it)) 

class Ports:
    """         
    """
    def __init__(self, mido):
        
        # a port corresponds to a physical device
       
        self._inPort_bass_name=None
        self._inPort_chords_name=None
        self._inPort_control_name=None
        
       
        self._inPort_bass = None
        self._inPort_chord = None
        self._inPort_control = None
        
        self._outPort = [] #Fix
        self._inport_piano = None # thinking of recieving sustain-pedal controls
        self._outputNames = mido.get_output_names()
        self._inputNames = mido.get_input_names()
        self._mido=mido
        
    def classname(self): return __class__.__name__

    
    #before using these , make sure they are not None ....
    def bassIsOpen(self):
        return not self._inPort_bass.closed
    
    def controlIsOpen(self):
        return not self._inPort_control.closed
    
    def chordIsOpen(self):
        return not self._inPort_chord.closed
        
        
    def report_devices(self):
          
            print(" --- OUTPUTS --- ")
            for i in self._outputNames:
                print('{} - {}'.format(i[:-1].ljust(30), "index: " + i[-1]))
                
            print('\n')       
            
            print(" --- INPUTS --- ") 
            for i in self._inputNames:
                print('{} - {}'.format(i[:-1].ljust(30), "index: " + i[-1]))
                
            print('\n')
            

    def report_port_status(self): 
        #print("report_port_status")
        
        # these lists may got devices not assigned, they will have a None value 
       
        ports = [self._inPort_bass, self._inPort_chord, self._inPort_control, self._outPort]
        #print("all ports: ", ports)
        #port_names=[self._inPort_bass_name, self._inPort_chords_name, self._inPort_control_name, "outname"]
        
        #remove entries with None values (None = not assigned devices)
        #port_names=[i for i in port_names if i != None]
        ports=[i for i in ports if i != None]
        #print("all ports which is not None: ", ports)

        
        print("\n - list port status -")  
        try:
            for i, port in enumerate(ports):
                
                if not port.closed:
                    
                    print("{} - {} {}".format(i, port.name[:-1].ljust(30), "\t open"))
                else:
                    
                    print("{} - {} {}".format(i, port.name[:-1].ljust(30), "\t closed "))
                    
        except Exception as e:
            print("error - report_port_status: " + str(e)) 
            
        print('\n')
        
        
    def startmessageQueue():
        pass
    
    
    def checkIfPortsEmpty(self):
        """ 
        Detect if there are no ports.
        The purpose is to warn the user/app that there is no point going further
        """
        input_names = self._inputNames
        return len(input_names) == 0
    
    def openInport_bass(self, index):
        input_names = self._inputNames
            
        try:
            self._inPort_bass_name = input_names[index]
            self._inPort_bass=self._mido.open_input(input_names[index]) 
        except Exception as e:
           print("error - openInport_bass - : " + str(e)) 
           
           
    def openInport_control(self, index):
        
        input_names = self._inputNames
        try:
            self._inPort_control_name = input_names[index]
            
            #if not self._inPort_control.closed: print("port control is already open!!")
            self._inPort_control=self._mido.open_input(input_names[index])             
        except Exception as e:
           print("error - openInport_controls - : " + str(e)) 


    def openInport_chords(self, index):

        input_names = self._inputNames
        try:
            self._inPort_chords_name = input_names[index]
            self._inPort_chord=self._mido.open_input(input_names[index])             
        except Exception as e:
           print("error - openInport_chords - : " + str(e)) 
    
    
    def openOutPort(self, nr): #opens everything at the moment 
        out_names=self._outputNames
        try:
            name = out_names[nr]
            self._outPort = self._mido.open_output(name)            
        except Exception as e:
            print("error - openOutPort: " + str(e))
    
    def closeAllPorts(self):
        #global original, ports
        original=[self._outPort, self._inPort_chord, self._inPort_bass, self._inPort_control]
        #print("closeAllPorts - all ports : ", original)
        ports = [i for i in original if i is not None] 
        #print("ports not None is: ", ports)
        try:         
            for i , port in enumerate(ports): 
                #print("i: ", i)
                #print("this port is being closed: ", port)
                port.close()
                
                    
        except Exception as e:
            print("closeallports: - error: "+ str(e))
            #return
        print("ports closed")
        
    
class MidiComm():
    """ 
    supports one out and many inports 
    
    """
    def __init__(self, mido, offset, chordTimeLength):
        self._outPort = []  
        
        
        self._inPortBass = None 
        self._inPortChordButtons = None 
        self._inPortControlButtons = None 
        
        self._inPortBass_name=None
        self._inPortChordButtons_name=None
        self._inPortControlButtons_name=None
        
        self._offset = offset
        self._chordLength = chordTimeLength
        
        self._mido =mido

        self._midichannel_bass = 0
        self._midichannel_chords_controls = 0
        
        self._midichannel_chord = 0

        
        self._midiChannel_out = 0
        
        
        
    def sendAllSoundOff(self):
        """
        send note_off CC to all 16 channels ....
        """
        print("sending ALL_SOUND_OFF Control message")
        
        for chan in range(16):
            m=self._mido.Message('control_change', channel=chan, control=CCvalues.ALL_SOUND_OFF)
            self._send(m) 
        
    def sendAllNotesOff(self):
        """
        send note_off CC to all 16 channels ....
        """        
        for chan in range(16):
            m=self._mido.Message('control_change', channel=chan, control=CCvalues.ALL_NOTES_OFF)
            self._send(m) 
            
            #yield self._send(m) #is yield needed?
    

    def sendProgamChange(self, program):
        # sent to out port
        #  return Mido.Message('control_change', channel=self.channel, control=self.control, value=self.value, time=self.time)
        #        
        

        msg=self._mido.Message(MidimsgType.programchange, channel=self._midiChannel_out, program=program) 
        if not self._outPort: print("output port not selected!")
        try:
            self._outPort.send(msg)
        except Exception as e:
            print("error - sendProgamChange: " + str(e))
        
        return program
            
        
    def report(self):
        print(" --- MidiComm report --- ")
        print("Midi channel out", self._midiChannel_out)
        print("Midi channel chord", self._midichannel_chord)
        print("Midi channel bass", self._midichannel_bass)
        
        
    def printMidiChannels(self):
        
        midi=self
        s = f"""midichannels:
        midi out: \t\t\t {midi._midiChannel_out}  
        midi bass in: \t\t {midi._midichannel_bass} 
        midi ctrl+chords in: {midi._midichannel_chords_controls}"""
        return s
    
        
    def setOutPort(self, port):
        self._outPort = port
        
    
    def setMidiChannelOut(self, midichannel):
        """
        If no midiout channel is set, it will default to channel 0 
        (corresponds with channel 1 for users)
        """        
        self._midiChannel_out = midichannel
    
    
    #midicom    
    def setMidiChannelBass(self, midichannel):
        self._midichannel_bass=midichannel
        
    def setMidiChannelChordControl(self, midichannel):
        self._midichannel_chords_controls = midichannel
        
    
    def playChord(self, global_Chord, global_root): 
        """ 
        The goal is send the chord indexes to midi out port
        
        """
        print("**************** playchord, ch: ", self._midiChannel_out)
        notes= copy.deepcopy(global_Chord.index)  
        root = copy.deepcopy(global_root)
        
        offset = self._offset
    
        notes=list(map(lambda x: x + root-offset, notes))
        #print("notes: ", notes)
        
        for note in notes:
            message=self._mido.Message(MidimsgType.note_on, channel=self._midiChannel_out, note=note)
            self._send(message)
        
        #turn the chord off    
        time.sleep(self._chordLength)    
        for note in notes:     
            self._send(self._mido.Message(MidimsgType.note_off, channel=self._midiChannel_out, note=note))    
        
    
    def sendMessageOut(self, msg):
        '''
        
        '''  
        self._send(msg) #, channel=5) #### fix this 
        
        
    
    
    def startLoop(self):     
        """ 
        we loop on input ports only 
        """
        def messageloopEmpty():
            return all(i is None for i in ports)
        
        def removeUnusedPorts(ports):
            return [i for i in ports if i != None] #remove None, or ports not in use
             
        ports=[self._inPortChordButtons, self._inPortBass, self._inPortControlButtons]
        ports=removeUnusedPorts(ports)
 
        print('\n Engage in message loop: ')
        try:
            for port in ports:
                print("{} {}".format('\t *', port.name[:-1].ljust(30))) # "is open - "# + str(c)))
        
        except Exception as e:
            print("error - function startLoop: " + str(e))
                
       
        if messageloopEmpty():
            print("no input devices available message-polling, returning: ", ports)
            return
            
        while True:   #loop is engaged
            for port in ports: 
                port.poll
                
    def startLoop_keyboardlistener(self, _callback):     
        """ 
        we loop on input ports only 
        """
        def messageloopEmpty():
            return all(i is None for i in ports)
        
        def removeUnusedPorts(ports):
            return [i for i in ports if i != None] #remove None, or ports not in use
             
        ports=[self._inPortChordButtons, self._inPortBass, self._inPortControlButtons]
        ports=removeUnusedPorts(ports)
 
        print('\n Engage in message loop: ')
        try:
            for port in ports:
                print("{} {}".format('\t *', port.name[:-1].ljust(30))) # "is open - "# + str(c)))
        
        except Exception as e:
            print("error - function startLoop: " + str(e))
                
       
        if messageloopEmpty():
            print("no input devices available message-polling, returning: ", ports)
            return
            
        while True:   #loop is engaged
            if keyboard.read_key() == "q": # q=quits
                #print('\n')
                #print("sendAllNotesOff")
                #self.sendAllNotesOff()
                
                #portInstance.closeAllPorts() 
                #portInstance.report_port_status()
                _callback()
                
                raise SystemExit(0) #clean way to exit , no traceback
                
            for port in ports: 
                port.poll()  
                
        
    #midicom
    def setinPort_bass(self, port, name, callbackfunction=None):
        self._inPortBass=port
        self._inPortBass_name=name
    
        print("bass input assigned to: ", self._inPortBass_name)
        
        try:   
            self._inPortBass.callback = callbackfunction
        except Exception as e:
            print("error - setinPort_bass" + str(e))
    
    def setinPort_chordButtons(self, port, name, callbackfunction=None):
        self._inPortChordButtons = port 
        self._inPortChordButtons_name=name
        print("chord input assigned to: ", self._inPortChordButtons_name)
        try:     
            self._inPortChordButtons.callback = callbackfunction
        except Exception as e:
            print("error - setinPort_chord" + str(e))

    def setinPort_controlButtons(self, port, name, callbackfunction=None):
        self._inPortControlButtons = port 
        self._inPortControlButtons_name=name
        print("control input assigned to : ", self._inPortControlButtons_name)
        
        try:     
            self._inPortControlButtons.callback = callbackfunction
        except Exception as e:
            print("error - setinPort_control" + str(e))        
            
        
        
    def testOut(self, velocity=100):
        """
        play 4 tones to check for sound
        """
        print("*** tones are playing ***")
        notes=[0,4,7,12]
        notes=list(map(lambda x: x + 64, notes))
   
        for note in notes:
            message=self._mido.Message(MidimsgType.note_on, channel=self._midiChannel_out, note=note, velocity=64)
            self._send(message)
            time.sleep(0.2)
            self._send(self._mido.Message(MidimsgType.note_off, channel=self._midiChannel_out, note=note))
            
        time.sleep(0.5)
 
    def _send(self,   message): #
        """
        the message must be a mido.Message()
        """
        p=self._outPort
        try:
            p.send(message)
        except Exception as e:
            print("Error in send: " + str(e))
            return
 



        

    