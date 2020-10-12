import os
from omxplayer.player import OMXPlayer
from omxplayer.keys import PREVIOUS_AUDIO
from time import sleep



def play_song(path):
    player=OMXPlayer(path,args=['-o' 'alsa'])
    return player

def play_list_of_songs(song_list):
    i=0
    while(i<len(song_list)):
        player=play_song(song_list[i])
        a=input()
        if(a=='n'):
            player.quit()
            i=i+1
            continue
        elif(a=='p'):
            player.quit()
            i=i-1
            continue
        else:
            pass

        while(1):
            try:
                while(player.is_playing()):
                    sleep(0.1)
            except:
                player.quit()
                break
        i=i+1
        #player.quit()
