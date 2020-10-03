from os import system

def spotify_on():
    system('sudo systemctl start raspotify.service')
    print('Spotify started')

def spotify_off():
    system('sudo systemctl stop raspotify.service')
    print('Spotify stopped')

if __name__ == "__main__":

    spotify_on()
    input()
    spotify_off()
    input()
    pass