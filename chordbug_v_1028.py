# -*- coding: utf-8 -*-

import mido as mido
from sessionclass import Misc, Session
from chord_classes1 import Chords, MidimsgType, Ports, MidiComm , Midimess
from chord_classes1 import Controls, Control, Chord
from chord_classes2 import Filter, scan, printMidiChannels, readportnumbers, askuseropenports
#report_ideas.txt - also take backup of this file

class Globals():
    """        
    This class contains variables utilized during a session
    """
    global_chord = Chords.major
    global_chord_root=64    
    global_chord_triggered = False   #mto ake sure chord is triggered once
    global_Control_disable_chord_root = False # set to false the chord root is frozen in position 
    note_on_off_flag=False
    global_bassdown=False #bass note is down or up 
    chords = [] #being invoked during session
    controls = [] #being invoked during session

# the mess parameter contains the whole parameter, you will the parameters in there 
## this callback scans for CHORDS and CONTROLS
def _callback_scan(classinstance, msgtype, note_cc, mess): #class instance , messagetype that triggered 
    global global_chord_triggered, global_chord    
    def ischord(instance):  return isinstance(instance, Chord)       
    def iscontrol(instance): return isinstance(instance, Control)
    print("found: ", classinstance.name)
    
    if ischord(classinstance): 
        #print(note_cc)
        # a chord's function is the same in each case so we do that externally       
        Globals.global_chord_triggered=False
        Globals.global_chord = classinstance #the whole instance
        return
                
    if iscontrol(classinstance): 
        args=Globals, msgtype, note_cc, mess #is all needed? common parameters for all control.function(...)
        classinstance.function(args)
        return

def callbackChord_Control_Piano():
    # for reading chords from piano/keyboard/right hand keys .... future 
    pass


## used of both controls and chord buttons ....        
def callbackChord_Control_Buttons(msg):
    global global_bassdown
    mess=Midimess(msg)
    print('callbackChord_Control_Buttons', mess.totext()) 
    
    def activateChord(bassdown):
        #if a bass note is down , then we are allowed to activate a chord
        if bassdown:
            midi.playChord(Globals.global_chord, Globals.global_chord_root)

    ## scan the chord and control structure for chord-control   
    if mess.isnoteOn(msg):       
        scan(MidimsgType.note_on, msg.note ,Globals, mess, _callback_scan)        
        activateChord(Globals.global_bassdown) 
        return
            
    if mess.isnoteOff(msg):
        return
    
    if mess.isControlChange(msg):
        scan(MidimsgType.controlchange, msg.control ,Globals, mess, _callback_scan)
        #activateChord(Globals.global_bassdown) 
        return
    
def callbackBass(msg):  
    '''
    recall that note_off = note_on with vel=0 
    '''
    midi.sendMessageOut(msg) #mimics the same as midi-through
    
    global global_chord_root, global_chord_triggered
    global global_chord, note_on_off_flag, global_bassdown
        
    midimsg=Midimess(msg) #copy constructor 
    print('callbackBass - ', midimsg.totext())
    
    if midimsg.isnoteOn(msg):
        Globals.global_bassdown=True
        
        if Globals.global_chord_triggered: #what if msg was not note?
            return #for only once trig of chord
             
        if not Globals.global_Control_disable_chord_root:
            Globals.global_chord_root=msg.note
        
        midi.playChord(Globals.global_chord, Globals.global_chord_root)
        
        if Globals.note_on_off_flag == True: # the chord knob is still down
        #we want to give cancel and give the chord trigger another try
            Globals.global_chord_triggered=False
        
        else: 
            Globals.global_chord_triggered=True
        return
    
    if midimsg.isnoteOff(msg):
        Globals.global_bassdown=False
        return
    
        
# -- global objects, later to be compiled into a session object     
midi=MidiComm(mido, offset=12, chordTimeLength=0.10) #offset = transpose 
ports=Ports(mido)
glb_ins_misc=Misc()

#Other objects should ask the filter about the midi-channels
filterMidi=Filter(callbackBass, callbackChord_Control_Buttons)
session=Session(mido) # everything in a session will be happening from this object


def main():
            
    #midi_channels = [0...15]
    default_midi_channel_in_bass=3 #default channel after reset T4 
    default_midi_channel_in_control_chords=10 # my fcb was at this channel at the moment ..
    default_midi_channel_out=15 #the chords are sent out here 
    
    global session, midi, ports
    ### fcb chords - conclusion 17.01
    #### C_maj,   C_aug,  Cdim,   ,C6,      C9
    #### C_major, C_sus2, C_minor, C7_minor, C7
    
    #check if the numbers in constructor are CC or Notes
    u=[Chords.dim([65]),Chords.aug([66]), Chords.normal_6th([67]), Chords.maj7([68]), Chords.nine9([69])]
    l=[Chords.major([60]), Chords.sus4([61]), Chords.minor([62]), Chords.minor7([63]), Chords.normal_7th([64])]
    Globals.chords=u+l    
                    
    # the 2nd controller got 6 (ntoes+CC) + 2 externally CC
    c=[Controls.freezeRoot([20]), Controls.add_seventh([21]), Controls.convert_to_minor([22]), Controls.special_control([23])]
    Globals.controls=c
            
    Misc.printTitle(mido)
    
    Misc.functionalityreport(Globals.chords, Globals.controls)
    print("all possible controls that can be handled if  assigned to a midi message: ") 
    Controls.printall(Controls)
    print("\n -- chords class structure, chords that can be invoked if  assigned to a midi message: ") 
    Chords.printall(Chords)    
    print('\n')    
     
    ports.report_devices()   
    #reads port indexes from user
    out_index, in_index_bass, in_index_chord, in_index_control=readportnumbers()
           
    midi.setMidiChannelBass(midichannel=default_midi_channel_in_bass)
    midi.setMidiChannelChordControl(midichannel=default_midi_channel_in_control_chords)
    
    midi.setMidiChannelOut(default_midi_channel_out) 
    midi.report()
    ports.openOutPort(out_index) #usually there is an outport on a computer
        
    askuseropenports(ports, midi, out_index, in_index_bass, in_index_chord, in_index_control, filterMidi)
    
    print("NB! - turn down instrument at chord-detect channel at mix")
    ports.report_port_status()    
    midi.setOutPort(ports._outPort)
    
    midi.testOut()   
    
    print('--- The Midi Filter ---')
    filterMidi.midichannelBass(default_midi_channel_in_bass)
    filterMidi.midichannelChordControl(default_midi_channel_in_control_chords)
    
    print(printMidiChannels(midi))     
    
    def _callback_destruct():
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
        

    midi.startLoop_keyboardlistener(_callback_destruct)# polling the keyboard 

   
if __name__ == "__main__":

    main()    
    
    