
import RPi.GPIO as GPIO
import serial

def read_pin(pin):
    i=GPIO.input(pin)#i e stoinost
    print(i)
    #input()
    if(pin==25):
        i=1-i
    print(i)
    return i
