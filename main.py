import RPi.GPIO as GPIO
import serial
from os import system
from serial1 import read_serial
from buttons import read_pin
from volume_control import volume_control
import time
from spotify import spotify_off, spotify_on

SPOTIFY=18
RADIO=23
CB=24
PLAY_PAUSE=25
#KB=12 Hardware Problem
YKB=16
serial_device='/dev/ttyACM0'
buttons=(SPOTIFY,RADIO,CB,PLAY_PAUSE,YKB)
GPIO.setmode(GPIO.BCM)


GPIO.setup(SPOTIFY, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(RADIO, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(CB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(PLAY_PAUSE, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
#GPIO.setup(KB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(YKB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  

ser=serial.Serial('/dev/ttyACM0',57600,timeout=1)
ser.flush()

sound=0 # flag for playback
player=' ' # flag for omx/alsa
scan = 1 #if a button is pressed, 0

while(1):
    if(sound):
        ser.reset_input_buffer()
        time.sleep(0.1)
        volume = read_serial(ser)
        if(volume):
            volume_control(volume, player)
    if(scan):
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
        spotify_on()
        player='alsa'
        scan=0
        sound=1

    if(button==23): #radio
        

    if(not(read_pin(button))):
        spotify_off()
        scan=1
        sound=0
    time.sleep(0.1)
    




