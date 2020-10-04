import os

def play_usb():
    ls=os.listdir('/media/pi')
    dir='/media/pi/'+ ls[0]
   
    os.chdir('/media/pi/flash')
    os.system('for a in *; do omxplayer "$a"; done')
    print(dir)


if __name__ == "__main__":

    play_usb()

    pass 