import os





def play_usb():
    ls=os.listdir('/media/pi')
    
    dir='/media/pi/'+ ls[0]
    
    print(dir)
    #os.chdir(dir)
    for i in os.listdir(dir):
        if(str(i)=='.Trash-1000'):
            continue

        print('omxplayer {}'.format( '"' + "'"+ str(dir)+'/' + str(i) + "'" + '"'))
        os.system('omxplayer {}'.format(str(dir)+'/' + str(i)))
if __name__ == "__main__":
    play_usb()
    pass