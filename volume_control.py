from os import system
from buttons import read_pin
import RPi.GPIO as GPIO
from time import sleep
import serial
from serial1 import read_serial

def volume_control():
    step=10
    mute_pin=25
    ser=serial.Serial('/dev/ttyACM0',57600,timeout=1)
    ser.flush()
    ser.reset_input_buffer()
    sleep(0.1)
    volume = read_serial(ser)
    if(not(volume)):
        return
    value=float(volume)/step
    if(read_pin(mute_pin)):
        value=0

    system("amixer sset 'Headphone' " + str(value) + '%')
    return value
    


    


if __name__ == "__main__":
    #for i in range(0,1024):
    #    print(volume_control(i))
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down 
    while(1):
        a=volume_control()
        sleep(0.1)
        print(a)
    pass