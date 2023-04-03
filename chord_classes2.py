# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 06:19:09 2022

@author: rolfe
"""
### chord_classes2


from typing import Any, List
from dataclasses import dataclass


class UserInteraction:
    def askuseropenports(rv, midi, filt, ports):
        
        
         ans = input("open inport for bass (default y): ") or "y"
         if ans == 'y':
             ports.openInport_bass(rv.in_index_bass) 
             midi.setinPort_bass(ports._inPort_bass, ports._inPort_bass_name, filt.trigBass) 
             
        
         ans = input("open inport for chord (default y): ") or "y"
         if ans == 'y':   
             ports.openInport_chords(rv.in_index_chord) 
             midi.setinPort_chordButtons(ports._inPort_chord, ports._inPort_chords_name, filt.trigControlChord) 
        
         ans = input("open inport for control (default y): ") or "y"
         if ans == 'y':
        
             ports.openInport_control(rv.in_index_control) 
             midi.setinPort_controlButtons(ports._inPort_control, ports._inPort_control_name, filt.trigControlChord) 

    def readportnumbers():
        
        @dataclass
        class Returnvalue:
            out_index: int
            in_index_bass: int
            in_index_chord: int
            in_index_control: int
            
        while True: # read in a midi port device 
            try:
                out_index = int(input("For chord out, enter a number (default 4): ") or "4")
                print('\n')
                in_index_bass = int(input("For bass input, enter a number(default 0): ") or "0") #1
                in_index_chord = int(input("For chord input, enter a number(default 2): ") or "2") #3
                in_index_control = int(input("For control input, enter a number(default 1): ") or "1") #0
                
                break
            except Exception as e:
                print("er, ror: " + str(e))
                
        return Returnvalue(out_index, in_index_bass, in_index_chord, in_index_control)
          



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











class Filter:
    '''
    1. Mido system first calls these functions as first layer
    2. Functions are then filtered dependent on their parameter 
    3. New function is then called and indicated with an _
    
    This filter handles Midi input only
    This filter only trigger callbacks with 
    midi messages with the correct channel property value
    
    future: 
    
    '''    
    def __init__(self, callback_bass, callback_controlchord): 
        
        self._cbBass=callback_bass
        self._cb_controlchord=callback_controlchord
        
        self._basschannel=None
        self._controlChordChannel=None
    
    def filteroutBass(MidimsgTypes):
        '''
        Messages are removed, but messages with correct channel is triggered
        add an array or class properties woth datatyps to ignore 
        in the message stream 
        '''
        pass
    
    
    def filteroutControlChord(MidimsgTypes):
        '''
        add an array or class properties woth datatyps to ignore 
        in the message stream 
        '''
        pass
    
    def report(self):
        print('--- The Midi Filter ---')
        print("bass midi: ", self._basschannel)
        print("control-chord midi: ", self._controlChordChannel)
        
    

    def setmidichannelBass(self, channel):
        self._basschannel=channel
        #print('Filter midichannel bass set: ', channel)
    
    def getMidiChBass(self):
        return self._basschannel
    
    def getMidiChCtrlChord(self):
        return self._controlChordChannel
        
    
    def setmidichannelChordControl(self, channel):
        self._controlChordChannel=channel
        #print('Filter control-chord midi channel bass set: ', channel)
        
    def _onlychannelmessages(self, msg):
        try:
            msg.channel #access attribute to check 
            return True
        except AttributeError:
            return False

    def trigBass(self, msg):
        # returns true of message contains channel property
        # here we filter out and make sure all messages 
        # triggered got a channel property
        # print('filter - trigBass: ', msg)
        
        if not self._onlychannelmessages(msg): 
            print("non cannel msg ignored: ", msg)
            return 
                
        if msg.channel == self._basschannel: 
            self._cbBass(msg) #calling callback fun
            
            
    def trigControlChord(self, msg):
        #print('filter - trigControlChord: ', msg)
        if not self._onlychannelmessages(msg): 
            print("non cannel msg ignored ", msg)
            return 
        
        if msg.channel == self._controlChordChannel: 
            self._cb_controlchord(msg) #calling callback fun
    
 ### messages triggered always have the channel property   
 

class CCvalues:
    """
    defines values that follows a CC (Control Change) message (CC, value)
    """
    ALL_SOUND_OFF = 120 #check midi spec for this one 
    RESET_ALL_CONTROLLERS = 121
    ALL_NOTES_OFF = 123
   
    # 122 Local Control On/Off  -  interrupt the internal control path between the keyboard and the sound-generating circuitry
    # 123 All Notes Off
    # 124 Omni Mode Off
    # 125 Omni Mode On
    # 126 Poly Mode On/Off
    # 127 Poly Mode Mono Off

    #https://www.lim.di.unimi.it/IEEE/MIDI/SOT0.HTM#Local

class utils:
    def availableCC():
        s="""
        These is free to use Control Change Messages ...
        """
        print(s)
        print("CC 3")
        print("CC 9")
        print("CC 14-15")
        print("CC 20-31")
        print("CC 85-87")
        print("CC 89-90")
        print("CC 102-119")
    
    # def showkeyb():
    #     img = mpimg.imread('keyb.png')
    #     plt.imshow(img)
    #     plt.show()
    


class GmSounds():
    
    def _class_to_list(the_object: Any) -> List[str]:
        """
        gets the public attributes of an object, if possible 
        the creation order is preserved
        this funtion's name starts with _ to not get inlcuded in the output
        """
        if hasattr(the_object, '__dict__'):
            fields = the_object.__dict__.keys()
        elif hasattr(the_object, '__slots__'):
            fields = the_object.__slots__
        else:
            fields = dir(the_object)
        fields = [field for field in fields if not field.startswith('_')]
        return fields
    
    AcousticGrandPiano = 0
    BrightAcousticPiano = 1
    lectricGrandPiano =2
    Honky_tonkPiano = 3
    ElectricPiano=4
    ElectricPiano=5
    Harpsichord=6
    Clavi=7
    Celesta=8
    Glockenspiel=9
    MusicBox=10
    Vibraphone=11
    Marimba=12
    Xylophone=13
    TubularBells=14
    Dulcimer=15
    DrawbarOrgan=16
    PercussiveOrgan=17
    RockOrgan=18
    ChurchOrgan=19
    
    ReedOrgan=20
    Accordion=21
    Harmonica=22
    TangoAccordion=23
    AcousticGuitar_nylon=24
    AcousticGuitar_steel=25
    Electric_Guitar_jazz=26
    Electric_Guitar_clean=27
    Electric_Guitar_muted=28
    Overdriven_Guitar=29
    Distortion_Guitar=30
    Guitar_harmonics=31
    AcousticBass=32
    ElectricBass_finger=33
    Electric_Bass_pick=34
    Fretless_Bass=35
    SlapBass_1 =36
    SlapBass_2=37
    SynthBass_1=38
    SynthBass_2=39
    Violin=40
    Viola=41
    Cello=42
    Contrabass=43
    TremoloStrings=44
    Pizzicato_Strings=45
    OrchestralHarp=46
    Timpani=47
    String_Ensemble1=48
    String_Ensemble2=49
    SynthStrings1=50
    SynthStrings2=51
    ChoirAahs=52
    VoiceOohs=53
    SynthVoice=54
    OrchestraHit=55
    Trumpet=56
    Trombone=57
    Tuba=58
    MutedTrumpet=59
    FrenchHorn=60
    BrassSection=61
    SynthBrass1=62
    SynthBrass2=63
    SopranoSax=64
    AltoSax=65  
    TenorSax=66
    BaritoneSax=67
    Oboe=68
    EnglishHorn=69
    Bassoon=70
    Clarinet=71
    Piccolo=72
    Flute=73
    Recorder=74
    PanFlute=75
    BlownBottle=76
    Shakuhachi=77
    Whistle=78
    Ocarina=79
    Lead1square =80
    Lead2sawtooth=81
    Lead3calliope=82
    Lead4chiff=83
    Lead5charang=84
    Lead6voice=85
    Lead7fifths=86
    Lead8basslead=87
    Pad1newage=88
    Pad2warm=89
    Pad3polysynth=90
    Pad4choir=91
    Pad5bowed=92
    Pad6metallic=93
    Pad7halo=94
    Pad8sweep=95
    FX1rain=96
    FX2soundtrack=97
    FX3crystal=98
    FX4atmosphere=99
    FX_5_brightness = 100
    FX6_goblins = 101
    FX7_echoes = 102
    FX8_sci_fi = 103
    Sitar=104
    Banjo=105
    Shamisen=106
    Koto=107
    Kalimba=108
    Bagpipe=109
    Fiddle=110
    Shanai=111
    TinkleBell=112
    Agogo=113
    SteelDrums=114
    Woodblock=115
    TaikoDrum=116
    MelodicTom=117
    SynthDrum=118
    ReverseCymbal=119
    GuitarFretNoise=120
    BreathNoise=121
    Seashore=122
    BirdTweet=123
    TelephoneRing=124
    Helicopter=125
    Applause=126
    Gunshot=127







