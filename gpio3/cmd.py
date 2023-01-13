from cy7c65213.device import CyUSBSerial, CyGPIO
import platform
import time

def main(argv=None):
    # Point to the DLL provided by Cypress
    if (platform.system() == "Windows"):
        dll = "C:\\Program Files (x86)\\Cypress\\USB-Serial SDK\\library\\cyusbserial\\x64\\cyusbserial.dll"
    if (platform.system() == "Linux"):
        dll = "/usr/local/lib/libcyusbserial.so"

    # Load the DLL
    try:
        lib = CyUSBSerial(lib=dll)
        print('lib: ', lib)
    except:
        print('Could not load USB-Serial library.')
        exit()

    # Look for a specific vendor and product id
    try:
        dev = next(lib.find(vid = 0x04B4,pid = 0x0003))
        print('dev: ', dev)
    except:
        print('Could not find USB-Seral device.')
        exit()

    gpio = CyGPIO(dev)
    print('gpio: ', gpio)

    # Set GPIO3 high
    try:
        gpio.pin(3).set(1)
    except:
        print('Could not set GPIO value.')
        exit()

if __name__ == "__main__":
    main()
