import os
from omxplayer.player import OMXPlayer
from omxplayer.keys import PREVIOUS_AUDIO
from time import sleep
import RPi.GPIO as GPIO
from buttons import read_pin
from volume_control import volume_control
def play_song(path):
    player=OMXPlayer(path,args=['-o' 'alsa'])
    return player

def play_list_of_songs(song_list,button):
    i=0
    
    NEXT=19
    PAUSE=11
    PREV=22
    playing=0
    while(i<len(song_list)):
        print(song_list[i])
        volume_control()
        if(not(playing)):
            player=play_song(song_list[i])
            playing=1
        if(not(read_pin(button))):
            player.quit()
            break
        # a=input()
        if(read_pin(NEXT)):
            player.quit()
            sleep(0.5)
            playing=0
            i=i+1
            continue
        elif(read_pin(PREV)):
            player.quit()
            sleep(0.5)
            playing=0
            i=i-1
            continue
        elif(read_pin(PAUSE)):
            player.play_pause()
            sleep(0.5)
        else:
            pass
        
        
        try:
            player.is_playing()
                
        except:
            player.quit()
            playing=0
            i=i+1
        
        #player.quit()
# def play_list_of_songs_software(song_list):
#     i=0
    
#     #NEXT=17
#     #PAUSE=27
#     #PREV=22
#     playing=0
#     while(i<len(song_list)):
#         print(song_list[i])
#         #volume_control()
#         if(not(playing)):
#             player=play_song(song_list[i])
#             playing=1
#         #if(not(read_pin(button))):
#         #    player.quit()
#         #    break
#         # a=input()
#         if(read_pin(NEXT)):
#             player.quit()
#             sleep(0.5)
#             playing=0
#             i=i+1
#             continue
#         elif(read_pin(PREV)):
#             player.quit()
#             sleep(0.5)
#             playing=0
#             i=i-1
#             continue
#         elif(read_pin(PAUSE)):
#             player.play_pause()
#             sleep(0.5)
#         else:
#             pass
        
        
#         try:
#             player.is_playing()
                
#         except:
#             player.quit()
#             playing=0
#             i=i+1