import os
NAMES=(
    "Radio 1 Rock",
    "Z-Rock",
)
STREAMS=(
    "http://149.13.0.81/radio1rock.ogg",
    "http://46.10.150.243:80/z-rock.mp3",
)

def play_radio(STREAM):
    os.system('omxplayer {}'.format(STREAM))
    



if __name__ == "__main__":
    play_radio(STREAMS[NAMES.index('Z-Rock')])
    pass