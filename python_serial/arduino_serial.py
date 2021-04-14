import os
import sys

import serial
from serial.tools.list_ports import comports

def main():

    ser = serial.Serial()

    print("BAUDRATES:\n{}".format(ser.BAUDRATES))
    print("BYTESIZES:\n{}".format(ser.BYTESIZES))
    print("PARITIES:\n{}".format(ser.PARITIES))
    print("STOPBITS:\n{}".format(ser.STOPBITS))
    print("COMPORTS:\n{}".format([str(c) for c in comports()]))

    ser.baudrate = 9600
    ser.bytesize = 8
    ser.parity = 'N'
    ser.stopbits = 1
    ser.port = 'COM3'
    ser.timeout = 0.5

    try:
        ser.open()
    except Exception as e:
        print(e)
        return 1

    while True:
        pin = input("Enter a pin to toggle (00 - 13), Q/q to break: ")
        
        if pin == 'Q' or pin == 'q':
            break

        data = '{}\n'.format(pin)
        ser.write(data.encode("utf-8"))
        
        data = ser.readline()
        print('{}'.format(data.decode("utf-8")))

    ser.close()

    return 0 

if __name__ == "__main__":

  sys.exit(main())