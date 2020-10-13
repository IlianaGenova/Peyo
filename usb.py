import os
from omxplayer.player import OMXPlayer
from omxplayer.keys import PREVIOUS_AUDIO
from time import sleep
import RPi.GPIO as GPIO
from play_audio_files import play_list_of_songs



def play_usb(button):
    ls=os.listdir('/media/pi')
    
    dir='/media/pi/'+ ls[0]
    track_paths=[]
    for i in os.listdir(dir):
        track_paths.append(str(dir) + '/' + i)
    print(track_paths)
    play_list_of_songs(track_paths,button)
    
   
    
   
   
    #os.chdir(dir)
    # for i in os.listdir(dir):
    #     if(str(i)=='.Trash-1000'):
    #         continue

    #     print('omxplayer {}'.format( '"' + "'"+ str(dir)+'/' + str(i) + "'" + '"'))
    #     os.system('omxplayer {}'.format(str(dir)+'/' + str(i)))
if __name__ == "__main__":
    #play_usb()
    pass