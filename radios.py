from os import system

def radio_on(STREAM):
    system('omxplayer {}'.format(STREAM))

def radio_off():
    system('killall omxplayer.bin')

if __name__ == "__main__":
    play_radio(STREAMS[NAMES.index('Z-Rock')])
    pass
