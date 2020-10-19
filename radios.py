from os import system
from time import sleep
from omxplayer.player import OMXPlayer
from play_audio_files import play_list_of_songs, play_song
def radio_on(button):
    
    # NAMES=(
    #     "Radio 1 Rock",
    #     "Z-Rock",
    # )
    STREAMS=(
        "http://46.10.150.243:80/z-rock.mp3",
        "http://149.13.0.81/radio1rock.ogg",
        "http://play.global.audio:80/bgradio128",
        "http://149.13.0.80/radio1.ogg",
        "http://live.btvradio.bg/jazz-fm.mp3",
        "http://149.13.0.80/city.ogg",

    )

    play_list_of_songs(STREAMS,button)

def radio_on_software():
    STREAMS=(
        "http://46.10.150.243:80/z-rock.mp3",
        "http://149.13.0.81/radio1rock.ogg",
        "http://play.global.audio:80/bgradio128",
        "http://149.13.0.80/radio1.ogg",
        "http://live.btvradio.bg/jazz-fm.mp3",
        "http://149.13.0.80/city.ogg",

    )
    player=play_song(STREAMS[0])
    return player

def radio_off_software(player):
    #system("sudo killall omxplayer.bin")
    player.quit()
    
    
    
    
    
    

if __name__ == "__main__":
    # player=radio_on('http://46.10.150.243:80/z-rock.mp3')
    # print(player)
    # sleep(15)
    # radio_off(player)
    # pass


    #radio_on()
    input()

