import RPi.GPIO as GPIO
import serial
from os import system
from serial1 import read_serial
from buttons import read_pin
from volume_control import volume_control
import time
from spotify import spotify_on
from radios import radio_on
from usb import play_usb
import multiprocessing
from omxplayer.player import OMXPlayer
from local import play_local
system('sudo systemctl stop raspotify.service')
SPOTIFY=18
RADIO=14#was 23, made 14
CB=26#was 24, made 26
MUTE=15#was 25, made 15
#KB=12 Hardware Problem
YKB=16
GPIO.setmode(GPIO.BCM)
#music control buttons
NEXT=19#was 17, made 19
PAUSE=11#made 11, was 27
PREV=22
GPIO.setup(NEXT, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(PAUSE, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(PREV, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  




buttons=(SPOTIFY,RADIO,CB,YKB)





GPIO.setup(SPOTIFY, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(RADIO, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(CB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(MUTE, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
#GPIO.setup(KB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(YKB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  

# ser=serial.Serial('/dev/ttyACM0',57600,timeout=1)
# ser.flush()

omx_killed=0
while(1):
    if(not(omx_killed)):
        system('sudo killall omxplayer.bin')
    omx_killed=1
    
    button=0
    for i in buttons:
        if(read_pin(i)):
            button=i
            break
    if(not(button)):
        time.sleep(0.1)
        continue
    print(button)



    if(button==SPOTIFY):#Spotify
        spotify_on(button)
        
        
    

    if(button==RADIO): #radio
        radio_on(button)
        omx_killed=0

    if(button==CB):#USB
        play_usb(button)
        omx_killed=0
    if(button==YKB):#Local
        play_local(button)
        omx_killed=0