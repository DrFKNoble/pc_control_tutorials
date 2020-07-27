# Serial Communication with Python

Welcome to my tutorial on how to communicate over a serial port using Python's serial module.

## Section 1: Introduction

Consider the following situation: you're an engineer working at a large factory. There is a machine in the factory you are responsible for. Your employer requires regular measurements of the machine's state to ensure its safe operation. What do you do?

Here are some potential solutions:

1. You walk over to the machine and manually make a measurement.
1. You develop a system to automatically make a measurement and save the machine's state to a computer. You walk over to the computer at the end of the day and download the day's log file.

Given a desired number and frequency of measurements, there's a number of issues with the first option: you may need to constantly take measurements, you may mis-count the number of measurements you've made, you may not record a measurement accurately, etc. A more satisfactory solution is the last option: an embedded system consisting of a sensor, amplifier, microcontroller, power supply, and PC-interface that will allow for consistent, continuous measurements. The last solution could be extended further to include automatic, emergency shutdown.

The problem is, how can an embedded system communicate with a PC? Fortunately, there are a number of tools, e.g. [PuTTY](https://www.putty.org/), and software frameworks and libraries, e.g. [Python](https://www.python.org/), which have been developed to facilitate this. PuTTY allows users to connect to a desired serial port and read and write raw data, e.g. a string. Python provides its serial module, which can be used to communicate with a physical or virtual COM port.

In this tutorial, I will show you how to use Python's serial module to communicate over a serial port using the RS-232 protocol. Sample 1 shows how to list available serial ports and Sample 2 shows how to read and write to a serial port. The remainder of this tutorial is structured as follows: Section 2 describes the tutorial's requirements; Section 3 describes how to run the tutorial's samples; Section 4 presents and describes Sample 1's source code; Section 5 presents and describes Sample 2's source code; Section 6 presents an activity for you to complete; and Section 7 concludes the tutorial.

## Section 2: Requirements

### Windows

You will need the following programs and libraries installed on your computer to build the tutorial's samples and activities:

1. [Python](https://python.org/)
1. [Visual Studio Code](https://code.visualstudio.com/)
1. [Arduino IDE](http://arduino.cc/)

This tutorial has been validated using the following software versions and hardware:

1. Python 3.7
1. Visual Studio Code 1.44.2
1. Arduino 1.8.12
1. Arduino Uno REV 3 (a similar development board, e.g. an Arduino Nano and Arduino Mega, or an Arduino-clone, could be used)

If you haven't got these installed, click on each link to go to the program's respective website. To install Python, Visual Studio Code, and the Arduino IDE, run their respective installer and follow the on-screen prompts. Be sure to add Python to our PATH environment variable.

You will also need to install the Pyserial module. Type the following command into a command prompt and press <kbd>Enter</kbd>:

	python -m pip install pyserial

This will install the module and its dependencies.

Once you've Python, Visual Studio Code, the Arduino IDE, and the Pyserial module installed, you can continue with this tutorial.

## Section 3: Build Instructions

This tutorial contains the following files:

1. [./README.md](./README.md)
1. [./sample_1/main.py](./sample_1/main.py)
1. [./sample_2/main.py](./sample_2/main.py)
1. [./activity_1/main.py](./activity_1/main.py)
1. [./serial_sketch/serial_sketch.ino](./serial_sketch/serial_sketch.ino)

The sample_1 sub-directory contains source code that shows you how to list available serial ports. The sample_2 sub-directory contains source code that shows you how to read and write data via a serial port using RS-232. The activity_1 sub-directory contain source code written to help get started in order to complete the tutorial's activity. The serial_sketch sub-directory contains the source code that was uploaded to the Arduino, which was used to validate the sample programs' functionality.

### Windows

The following describe how to run the tutorial's source code using either: 1) console commands, or 2) Visual Studio Code.

### Console Commands

To run the program, browse to the program's sub-directory and use the following commands:

	python main.py

In Visual Studio Code, you can open a terminal using the <kbd>CTRL + ~</kbd> shortcut.

### Visual Studio Code

To debug the program:

1. Click 'Run' > 'Start Debugging'

You can also debug the program using the <kbd>F5</kbd> shortcut.

To run the program without debugging:

1. Click 'Run' > 'Run Without Debugging'

You can also run the program without debugging using the <kbd>CTRL + F5</kbd> shortcut.

## Section 4: Sample 1

This sample shows how to list available serial ports.

Browse to the sample_1 sub-directory. Let's have a look at the sample's source code.

[main.py](./sample_1/main.py)

```py
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

```

Let's go through the program, line by line, block by block.

On line 1,

```py
import serial
```

the `import` statement is used to access the serial module's code, e.g. its functions and classes. You can find more about the import system [here](https://docs.python.org/3.7/reference/import.html).

On line 3,

```py
from serial.tools import list_ports
```

the `from` statement is used to import the `list_ports` sub-module. The module includes the function, `comports()`, which can be used to list the available serial ports. You can find more about the `serial` module's tools [here](https://pyserial.readthedocs.io/en/latest/tools.html).

On lines 6-26, 

```py
def main():

	...

	return
```

the function `main()` is defined. `main()` has no parameters and doesn't return anything.

On line 8,

```py
serial_ports = list_ports.comports()
```

`list_port` module's `comports()` function is used to get a list of available ports. The function retuns a list containing `ListPortInfo` objects. You can find more about the `ListPortInfo` class [here](https://pyserial.readthedocs.io/en/latest/tools.html).

On lines 10-24,

```py
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
```

a `for` loop is used to iterate over each instance in the object returned by the `enumerate()` function. During each iteration, the `print()` function is used to display the contents of each instance of the `ListPortInfo` class's data members. You can find more about `enumerate()` [here]({https://docs.python.org/3/library/functions.html#enumerate}).

On lines 29-31,

```py
if __name__ == "__main__":

    main()
```

an `if` statement is used to check whether the program is running in the main scope. If `True`, then `main()` will be executed. You can find more about the top-level script environment [here](https://docs.python.org/3.7/library/__main__.html).

Now that we've looked at the sample's source code, run the program.

Run the program. You should see something similar to the following printed on the console:

	Port 0: COM1 - Communications Port (COM1)
	Device: COM1
	Name: None
	Description: Communications Port (COM1)
	HWID: ACPI\PNP0501\1
	VID: None
	PID: None
	Serial Number: None
	Location: None
	Manufacturer: (Standard port types)
	Product: None
	Interface: None

	Port 1: COM3 - Arduino Uno (COM3)
	Device: COM3
	Name: None
	Description: Arduino Uno (COM3)
	HWID: USB VID:PID=2341:0001 SER=85534313937351A0D042 LOCATION=1-1.8
	VID: 9025
	PID: 1
	Serial Number: 85534313937351A0D042
	Location: 1-1.8
	Manufacturer: Arduino LLC (www.arduino.cc)
	Product: None
	Interface: None

## Section 5: Sample 2

This sample shows how to read and write data over a serial port.

Browse to the sample_2 sub-directory. Let's have a look at the sample's source code.

[main.py](./sample_2/main.py)

```py
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
```

Let's go through the program, line by line, block by block.

On lines 1-2,

```py
import serial
```

the `import` statement is used to access the serial and time modules.

On lines 5-58, 

```py
def main():

	try:

	...

	except Exception as e:

		print(e)

	return
```

the function `main()` is defined. `main()` has no parameters and doesn't return anything. In `main()`, a `try` statement is used for handling all exceptions. You can find more about exception handling [here](https://docs.python.org/3.7/tutorial/errors.html).

On lines 8-11,

```py
ser = serial.Serial("COM3", 115200, timeout=1.0, bytesize=serial.EIGHTBITS,
					parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
time.sleep(2.0)
```

an instance of serial's `Serial` class named `ser` is created. The object is instantiated with its port, baudrate, timeout, bytesize, parity, and stopbits data members with the string "COM3", the integer 115200, the floating point 1.0, enum serial.EIGHTBITS, enum serial.PARITY_NONE, and enum serial.STOPBITS_ONE, respectively. You can find more about `Serial` [here](https://pyserial.readthedocs.io/en/latest/pyserial_api.html). 

Afterwards, the `time` module's `sleep()` function is used to wait for 2.0 seconds.

**Note**: *I've found adding the time delay here to be helpful in resolving an issue where, when debugging a program, the serial port is able to write data to a device, e.g. an Arudino, and read the data it returns, but when running the program without debugging, the serial port does not receive any data. I believe it's because of a race condition, or that the serial port hasn't finished initialising properly before it's accessed. Keep this mind if you're having issues.*

On lines 13-22,

```py
# ser = serial.Serial()

# ser.port = "COM1"
# ser.baudrate = 115200
# ser.bytesize = serial.EIGHTBITS
# ser.parity = serial.PARITY_NONE
# ser.stopbits = serial.STOPBITS_ONE
# ser.timeout = 0.5           

# ser.open()
```

an alternative way to create a `ser` is shown. Here, the lines are commented out.

On lines 24-25,

```py
data = "Hello World!\n".encode()
print("Data: {}".format(data))
```

the `encode()` member function is used to encode the string into bytes, which is then assigned to the varaible `data`. Next, the `print()` function is used to display the contents of `data` on the console.

On lines 27-29,

```py
byts = ser.write(data)
print("Bytes written: {}".format(byts))
ser.flush()
```

`ser`'s `write()` member function is used to write the variable `data`'s content to the serial port. The number of bytes written are then assigned to the variable `byts`. Next, the `print()` function is used display the number of bytes written. Lastly, `ser`'s `flush()` member function is used to wait until all data is written. You can find more about `write()` and `flush()` [here](https://pyserial.readthedocs.io/en/latest/pyserial_api.html).

On lines 33-45,

```py
read = True

while read:

	...
```

a `while` loop is used to continously read bytes from the serial port. While the variable `read` is equal to `True`, the loop will iterate forever; stopping when `read` is equal to `False`.

On lines 35-45,

```py
if ser.inWaiting() > 0:

	c = ser.read(1)

	if c == '\r'.encode():
		continue
	elif c == '\n'.encode():
		read = False
		break

	print(c)
```

an `if` statement and `ser`'s `inWaiting()` member function are used to see if the serial port has any data to read. If `True`, the code defined in `if` statement's body is executed; else, it is ignored. Here, `ser`'s `read()` member function is used to read one byte from the serial port, which is assigned to the variable `c`. 

Next, an `if` statement is used to check whether `c` is equal to the encoded '\r' character. If `True`, then the `while` loop starts a new iteration; else, an `elif` statement is used to check whether `c` is equal to the encoded `\n` character. If `True`, then the while loops ends; else, the `print()` function is used to display the contents of `c` on the console.

One lines 47-48,

```py
ser.reset_input_buffer()
ser.reset_output_buffer()
```

`ser`'s `reset_input_buffer()` and `reset_output_buffer()` member functions are called. These clear the input and output buffer, respectively.

**Note:** *I've found that, sometimes, the serial port does not close properly, which results in the program "hanging". Searching online, it was recommended to clear the input and output buffers immediately before closing the serial port. I tried it, and it seems to work. Strictly speaking, this may not be necessary, but worth keeping in mind if it's a problem for you.*

On line 50,

```py
ser.close()
```

`ser`'s `close()` member function is used to close the serial port.

On lines 61-63,

```py
if __name__ == "__main__":

    main()
```

an `if` statement is used to check whether the program is running in the main scopre. If `True`, the code defined in the `if` statement's body is executed; else, the code defined in the `if` statement's body is ignored. Here, `main()` is called.

Now that we've looked at the sample's source code, run the program.

For it to run properly, you need to have a "COM3" serial port available on your computer. To create a serial port, plug an Arduino into your computer. It will enumerate as "USB Serial Device (COMX)", where 'X' is a number depending on the number of existing serial ports. You can check the serial ports name via your computer's Device Manager.

To have the Arduino echo the string sent to it, upload the sketch in the tutorial's serial_sketch sub-directory.

Run the binary. You should see the following printed on the console:

	Data: b'Hello World!\n'
	Bytes written: 13
	b'H'
	b'e'
	b'l'
	b'l'
	b'o'
	b' '
	b'W'
	b'o'
	b'r'
	b'l'
	b'd'
	b'!'

## Section 6: Activity 1

Now that you know how to use Python's serial module to communicate over a serial port, complete the following:

1. Write an application that uses Python's serial module to communicate with an Arduino and toggle an LED's state.

The activity_1 sub-directory is set up for you to get started. Also, on an Arduino Uno pin 13 is connected to the user-controlled LED in case you don't have an LED and resitor available.

## Section 7: Conclusion

In this tutorial, I have shown you how to communicate over a serial port using Python's serial module.

You have also written your own program that writes data to an Arduino, toggling a hardware pin's state.

I hope this tutorial has been useful.

## Credit

Dr Frazer K. Noble  
Department of Mechanical and Electrical Engineering  
School of Food and Advanced Technology  
Massey University  
New Zealand
