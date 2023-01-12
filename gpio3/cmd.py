from cy7c65213.device import CyUSBSerial, CyGPIO
import platform
import time

def main(argv=None):
    # Point to the DLL provided by Cypress
    if (platform.system() == "Windows"):
        dll = "C:\\Program Files (x86)\\Cypress\\USB-Serial SDK\\library\\cyusbserial\\x64\\cyusbserial.dll"
    else:
        dll = "/usr/local/lib/libcyusbserial.so"

    # Load the DLL
    lib = CyUSBSerial(lib=dll)

    # Look for a specific vendor and product id
    dev = next(lib.find(vid = 0x04B4,pid = 0x0003))

    gpio = CyGPIO(dev)

    # Set GPIO3 high
    gpio.pin(3).set(1)

if __name__ == "__main__":
    main()