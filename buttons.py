import RPi.GPIO as GPIO
import serial
SPOTIFY=18
RADIO=23
CB=24
PLAY_PAUSE=25
#KB=12 Hardware Problem
YKB=16
serial_device='/dev/ttyACM0'

GPIO.setmode(GPIO.BCM)


GPIO.setup(SPOTIFY, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(RADIO, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(CB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(PLAY_PAUSE, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
#GPIO.setup(KB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(YKB, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  

ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser.flush()



def read_pin(pin):
    i=GPIO.input(pin)#i e stoinost
    print(i)
    #input()
    if(pin==25):
        i=1-i
    print(i)
    return i

def read_serial():
    if(ser.in_waiting>0):
        line=ser.readline().decode('utf-8').rstrip()
        print(line)
        return line

if __name__ == "__main__":
    while(1):
        read_pin(SPOTIFY)
        input()
        read_serial()
        input()
    pass












