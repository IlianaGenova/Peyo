
import RPi.GPIO as GPIO
import serial


def read_serial(ser):
    if(ser.in_waiting>0):
        line=ser.readline().decode('utf-8').rstrip()
        print(line)
        return line