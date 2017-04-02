python-ucdev
============

Python library to access the GPIO pins of the Cypress CY7C65213 USB-Serial bridge in UART mode.

A cut-down version of python-ucdev by Taisuke Yamada. Thank you Tai.
(Use Tai's original version if you need I2C or SPI functionality.)

If you want to use this code to interface to the CY7C65213 under Linux - e.g. on Raspberry Pi -
then take a look at:

https://github.com/PaulZC/python-ucdev/blob/master/Interfacing_CY7C65213_to_Raspberry_Pi.pdf

## Usage (CY7C65213)

    >>> from cy7c65213 import CyUSBSerial, CyGPIO
    >>> 
    >>> # load DLL provided by Cypress
    >>> dll = "c:/path/to/Cypress-USB-Serial/library/lib/cyusbserial.dll"
    >>> lib = CyUSBSerial(lib = dll)
    >>>
    >>> # use first device found
    >>> dev = lib.find().next()
    >>>
    >>> # access GPIO
    >>> gpio = CyGPIO(dev)
    >>> gpio.set(3, 1)
    >>> ret = gpio.get(3)
    >>>
    >>> # access each GPIO pin
    >>> pin = gpio.pin(3)
    >>> pin.set(1)
    >>> ret = pin.get()

## Note
This requires cyusbserial.dll (or libcyusbserial.so) library provided by Cypress.

## Known Bugs
The pyserial_and_gpio_test.py example works fine under Windows, but under Linux
ser.getCTS always seems to return True.

