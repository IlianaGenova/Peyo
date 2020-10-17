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
RADIO=23
CB=24
MUTE=25
#KB=12 Hardware Problem
YKB=16

buttons=(SPOTIFY,RADIO,CB,YKB)
GPIO.setmode(GPIO.BCM)




GPIO.setup(SPOTIFY, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(RADIO, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(CB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(MUTE, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
#GPIO.setup(KB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(YKB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  

# ser=serial.Serial('/dev/ttyACM0',57600,timeout=1)
# ser.flush()


while(1):
    system('sudo killall omxplayer.bin')
    
    
    button=0
    for i in buttons:
        if(read_pin(i)):
            button=i
            break
    if(not(button)):
        time.sleep(0.1)
        continue
    print(button)



    if(button==18):#Spotify
        spotify_on(button)
        
    

    if(button==23): #radio
        radio_on(button)
    

    if(button==24):#USB
        play_usb(button)

    if(button==16):#Local
        play_local(button)
        