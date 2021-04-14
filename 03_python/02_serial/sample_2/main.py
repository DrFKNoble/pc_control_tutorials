import serial
import time


def main():

    try:

        ser = serial.Serial("COM3", 115200, timeout=1.0, bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        time.sleep(2.0)

        # ser = serial.Serial()

        # ser.port = "COM1"
        # ser.baudrate = 115200
        # ser.bytesize = serial.EIGHTBITS
        # ser.parity = serial.PARITY_NONE
        # ser.stopbits = serial.STOPBITS_ONE
        # ser.timeout = 0.5

        # ser.open()

        data = "Hello World!\n".encode()
        print("Data: {}".format(data))

        byts = ser.write(data)
        print("Bytes written: {}".format(byts))
        ser.flush()

        read = True

        while read:

            if ser.inWaiting() > 0:

                c = ser.read(1)

                if c == '\r'.encode():
                    continue
                elif c == '\n'.encode():
                    read = False
                    break

                print(c)

        ser.reset_input_buffer()
        ser.reset_output_buffer()

        ser.close()

        return

    except Exception as e:

        print(e)

    return


if __name__ == "__main__":

    main()
