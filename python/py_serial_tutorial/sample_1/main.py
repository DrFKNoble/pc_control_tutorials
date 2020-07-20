import serial

from serial.tools import list_ports


def main():

    serial_ports = list_ports.comports()

    for i, sp in enumerate(serial_ports):

        print("Port {}: {}".format(i, sp))
        print("Device: {}".format(sp.device))
        print("Name: {}".format(sp.name))
        print("Description: {}".format(sp.description))
        print("HWID: {}".format(sp.hwid))
        print("VID: {}".format(sp.vid))
        print("PID: {}".format(sp.pid))
        print("Serial Number: {}".format(sp.serial_number))
        print("Location: {}".format(sp.location))
        print("Manufacturer: {}".format(sp.manufacturer))
        print("Product: {}".format(sp.product))
        print("Interface: {}".format(sp.interface))
        print()

    return


if __name__ == "__main__":

    main()
