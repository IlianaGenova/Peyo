import RPi.GPIO as GPIO
import serial
from serial1 import read_serial
from buttons import read_pin
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

if __name__ == "__main__":
    while(1):
        read_pin(SPOTIFY)
        input()
        read_serial(ser)
        input()
    pass
