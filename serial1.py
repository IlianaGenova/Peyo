
import RPi.GPIO as GPIO
import serial
import time

def read_serial(ser):
    if(ser.in_waiting>0):
        line=ser.readline().decode('utf-8').rstrip()
        print(line)
        if(line):
            return line
    

if __name__ == "__main__":
    ser=serial.Serial('/dev/ttyACM0',57600,timeout=1)
    ser.flush()
    #time.sleep(0.4)
    while(1):
        ser.reset_input_buffer()
        time.sleep(0.1)
        print(read_serial(ser))
        
    pass