from os import system
from buttons import read_pin
def volume_control(volume,mode):
    step=10
    value=float(volume)/step
    if(mode=='omx'):
        value=value*1.5

    
    if(value<=55 and mode=='alsa'):
        value=0    
    #if(value>100):
     #   value=100    #when value is less than 60%, there's no sound --> 0
    if(mode=='omx'):
        value=float(value/100)
        system('''export DBUS_SESSION_BUS_ADDRESS=$(cat /tmp/omxplayerdbus.${USER:-root})
                dbus-send --print-reply --session --reply-timeout=500 --dest=org.mpris.MediaPlayer2.omxplayer /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Set string:"org.mpris.MediaPlayer2.Player" string:"Volume" double:''' + str(value))
                                                      #works as a black box, pls don't ask
    if(mode=='alsa'):
        
        if(read_pin(25)):
            value=0
        system("amixer sset 'Headphone' " + str(value) + '%')
    return value
    


    


if __name__ == "__main__":
    #for i in range(0,1024):
    #    print(volume_control(i))
    while(1):
        a=volume_control(200,'omx')
        print(a)
    pass