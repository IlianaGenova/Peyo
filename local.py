import os
from omxplayer.player import OMXPlayer
from omxplayer.keys import PREVIOUS_AUDIO
from time import sleep
import RPi.GPIO as GPIO
from play_audio_files import play_list_of_songs


def play_local(button):
    dir='/home/pi/Music'
    
   
    track_paths=[]
    for i in os.listdir(dir):
        track_paths.append(str(dir) + '/' + i)
    print(track_paths)
    play_list_of_songs(track_paths,button)
    

if __name__ == "__main__":
    play_usb(1)

    pass