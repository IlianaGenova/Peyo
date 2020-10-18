
import RPi.GPIO as GPIO
import serial

def read_pin(pin):
    i=GPIO.input(pin)#i e stoinost
    
    #input()
    if(pin==25):
        i=1-i
    
    return i

if __name__ == "__main__":
    pin=22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
    while(1):
        print(read_pin(pin))
    pass