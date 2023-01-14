#!/usr/bin/env python3

from cy7c65213.device import CyUSBSerial, CyGPIO
import argparse
import platform
import sys
import time

def set(pin, state):
    try:
        gpio.set(pin, state)
    except:
        print('Could not set GPIO value.')
        exit()

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Control Cypress USB-Serial GPIO3 state."
    )
    parser.add_argument("--on", action='store_true', help="Set GPIO3 power on")
    parser.add_argument("--off", action='store_true', help="Set GPIO3 power off")
    parser.add_argument("--reset", action='store_true', help="Reset GPIO3 power")

    args = parser.parse_args(argv)

    if len(sys.argv) != 2:
        parser.print_help()
        parser.exit()

    # Point to the DLL provided by Cypress
    if (platform.system() == "Windows"):
        dll = "C:\\Program Files (x86)\\Cypress\\USB-Serial SDK\\library\\cyusbserial\\x64\\cyusbserial.dll"
    if (platform.system() == "Linux"):
        dll = "/usr/local/lib/libcyusbserial.so"

    # Load the DLL
    try:
        lib = CyUSBSerial(lib=dll)
    except:
        print('Could not load USB-Serial library.')
        exit()

    # Look for a specific vendor and product id
    try:
        dev = next(lib.find(vid = 0x04B4,pid = 0x0003))
    except:
        print('Could not detect USB-Seral device.')
        exit()

    global gpio
    gpio = CyGPIO(dev)

    if args.on:
        set(3, 0)
    if args.off:
        set(3, 1)
    if args.reset:
        set(3, 1)
        time.sleep(0.1)
        set(3, 0)

if __name__ == "__main__":
    main()
