from os import system
from time import sleep
from omxplayer.player import OMXPlayer
def radio_on(STREAM):
    #system('omxplayer {}'.format(STREAM))
    
    try:
        player=OMXPlayer(STREAM, args=['-o' 'alsa'])
    except:
        return 0
    return player




def radio_off(player):
    #system('killall omxplayer.bin')
    player.quit()

if __name__ == "__main__":
    player=radio_on('http://46.10.150.243:80/z-rock.mp3')
    print(player)
    sleep(15)
    radio_off(player)
    pass
