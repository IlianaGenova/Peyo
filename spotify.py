from os import system
from time import sleep
from volume_control import volume_control
from buttons import read_pin
def spotify_on(button):
    system('sudo systemctl start raspotify.service')
    print('Spotify started')
    while(read_pin(button)):
        sleep(0.1)
        volume_control()
    system('sudo systemctl stop raspotify.service')
    
def spotify_on_software():
    system('sudo systemctl start raspotify.service')
    print('Spotify started')

def spotify_off_software():
    system('sudo systemctl stop raspotify.service')
    print('Spotify stopped')


if __name__ == "__main__":

    # spotify_on()
    # input()
    # spotify_off()
    # input()
    pass