# -*- coding: utf-8 -*-


import mido as mido
from sessionclass import Misc, Session
from chord_classes1 import Chords, MidimsgType, Ports, MidiComm , Midimess
from chord_classes1 import Controls, Control, Chord
from chord_classes2 import GmSounds
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
    chords = [] #being invoked during session
    controls = [] #being invoked during session

# the mess parameter contains the whole parameter, you will the parameters in there 
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
                
    if iscontrol(classinstance): 
        # some controls might need special handling ...
        #if classinstance.__class__.__name__  == 'special_control': #better method of doing this?
        #    args=Globals, msgtype, note_cc, mess
        #    classinstance.function(args)
            
            #print(classinstance.name)
            
        #else: 
            #args=Globals, msgtype, note_cc, mess #is all needed? common parameters for all control.function(...)
            #classinstance.function(args)
            #print("evoked control: ", classinstance.name)
        args=Globals, msgtype, note_cc, mess #is all needed? common parameters for all control.function(...)
        classinstance.function(args)
        
def callbackChord_Control_Buttons(msg):
    
    mess=Midimess(msg)
    print(mess.totext()) #for visual inspection of midi messages 
    
    def scan(msgtype, note_cc, Globals, msg, callback, extraparams=None):
        """
        Scanning to se if a midi message match anything in the global lists: 
            chords = [] 
            controls = []
        If so, the _callback_scan() is invoked.
        msgtype: the type midi message cousing the triggering is a list [.....]
        note_cc: the midi note or CC (control change) causing the triggering
        callback: the function to be evoked if all parameters match 
        """
        for chord in Globals.chords:
            if msgtype in chord.msgtype:
                if note_cc in chord.note_cc:
                    callback(chord, msgtype, note_cc, msg) #returns class instance of the matched chord
            
        for control in Globals.controls:
            if msgtype in control.msgtype: 
                if note_cc in control.note_cc:
                    callback(control, msgtype, note_cc, msg) #returns class instance
        
        # we need to transfer the val parameter too ...
    
    ## scan the chord and control structure for chord-control   
    if mess.isnoteOn(msg):
        scan(MidimsgType.note_on, msg.note ,Globals, mess, _callback_scan)
        
    elif mess.isnoteOff(msg):
        scan(MidimsgType.note_off, msg.note ,Globals, mess, _callback_scan)
        
    elif mess.isControlChange(msg):
        #params=msg.value, msg.channel
        scan(MidimsgType.controlchange, msg.control ,Globals, mess, _callback_scan)
    
    elif mess.isProgramChange(msg): 
        pass
    
    #elif mess.isSysexdata( ...)
                  
    else:
        pass
        #print("callbackChord_Control_Buttons - message not supported! - ") 
        #print(msg)
    
def callbackBass(msg):

    global global_chord_root, global_chord_triggered
    global global_chord, note_on_off_flag
        
    print(Midimess(msg).totext())

    if Globals.global_chord_triggered: 
        return #for only once trig of chord
     
    if msg.type == MidimsgType.note_on:
        
        if not Globals.global_Control_disable_chord_root:
            Globals.global_chord_root=msg.note
        
        midi.playChord(Globals.global_chord, Globals.global_chord_root)
        
        #Globals.global_chord_triggered=True   # was true
        
        if Globals.note_on_off_flag == True: # the chord knob is still down
        #we want to give cancel and give the chord trigger another try
            Globals.global_chord_triggered=False
        
        else: 
            Globals.global_chord_triggered=True
            
    if msg.type == MidimsgType.note_off:
        pass
            
            
# -- global objects, later to be compiled into a session object     
midi=MidiComm(mido, offset=12, chordTimeLength=0.07)
ports=Ports(mido)
glb_ins_misc=Misc()

session=Session(mido) # everthing in a session will be happening from this object

def main():
    default_midi_channel_in=0 
    default_midi_channel_out=0
    
    
    global session, midi, ports
    ### fcb chords - conclusion 17.01
    #### C_maj,   C_aug,  Cdim,   ,C6,      C9
    #### C_major, C_sus2, C_minor, C7_minor, C7
    
    u=[Chords.dim([65]),Chords.aug([66]), Chords.normal_6th([67]), Chords.maj7([68]), Chords.nine9([69])]
    l=[Chords.major([60]), Chords.sus4([61]), Chords.minor([62]), Chords.minor7([63]), Chords.normal_7th([64])]
    Globals.chords=u+l    
                    
    c=[Controls.freezeRoot([12]), Controls.add_seventh([13]), Controls.convert_to_minor([14]), Controls.special_control([30])]
    Globals.controls=c
    
    Misc.printTitle(mido)
    
    Misc.functionalityreport(Globals.chords, Globals.controls)
    print("all possible controls that can be handled if  assigned to a midi message: ") 
    Controls.printall(Controls)
    print("\n -- chords class structure, chords that can be invoked if  assigned to a midi message: ") 
    Chords.printall(Chords)    
    print('\n')    
    
    # if ports.checkIfPortsEmpty():
    #     ports.report_devices()
    #     ports.closeAllPorts() 
    #     print("--- NB! No input-ports available ---")
    #     print("quitting program")
    #     raise SystemExit(0)   
        
    ports.report_devices()
   
    print("Midichannels are from [0-15]")
    while True: # read in a midi port device 
        try:
            out_index = int(input("For chord out, enter a number (default 0): ") or "0")
            
            in_index_bass = int(input("For bass input, enter a number(default 1): ") or "1") #1
            in_index_chord = int(input("For chord input, enter a number(default 3): ") or "3") #3
            in_index_control = int(input("For control input, enter a number(default 0): ") or "0") #0
            
            break
        except Exception as e:
            print("error: " + str(e))
            
    #try to keep to midichannel 1 (coded as 0 ) as much as possible 

    
    midi.setMidiChannelBass(midichannel=default_midi_channel_in)
    midi.setMidiChannelChord(midichannel=default_midi_channel_in)
    midi.setMidiChannelControl(midichannel=default_midi_channel_in)
    
    midi.setMidiChannelOut(default_midi_channel_out)
    
    midi.report()
    
    ports.openOutPort(out_index) #usually there is an outport on a computer
        
    ans = input("open inport for bass (default y): ") or "y"
    if ans == 'y':
        ports.openInport_bass(in_index_bass) 
        midi.setinPort_bass(ports._inPort_bass, ports._inPort_bass_name, callbackBass) 
   
    ans = input("open inport for chord (default y): ") or "y"
    if ans == 'y':   
        ports.openInport_chords(in_index_chord) 
        midi.setinPort_chordButtons(ports._inPort_chord, ports._inPort_chords_name, callbackChord_Control_Buttons) 

    ans = input("open inport for control (default y): ") or "y"
    if ans == 'y':
        ports.openInport_control(in_index_control) 
        midi.setinPort_controlButtons(ports._inPort_control, ports._inPort_control_name, callbackChord_Control_Buttons) 

    
    ports.report_port_status()
    
    midi.setOutPort(ports._outPort)
    
    programnr=midi.sendProgamChange(GmSounds.FX1rain)
    
    propertylist=GmSounds._class_to_list(GmSounds)

    print("GM sound selected for PC: ", propertylist[programnr-1])
    
        
    midi.testOut()   

    midi.startLoop_keyboardlistener(ports) # polling the keyboard 

   # close down app in a callback?
   
if __name__ == "__main__":

    main()    
    
    
    
