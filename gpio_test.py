# Test the Cypress CY7C65213 GPIO Pins

# Before you run this test, use the Cypress USB-Serial Configuration Utility (under Windows) to:
#  Set UART RX Notification LED to "None"
#  Set UART TX Notification LED to "None"
#  Set UART RX or TX Notification LED to "GPIO_0"
#  Configure GPIO_1 as "Drive 0" (i.e. low output as default)
#  Configure GPIO_2 as "Input" (instead of "Tristate")

# Connect GPIO_1 to GPIO_2 using a jumper wire

from cy7c65213 import CyUSBSerial, CyGPIO
import time

# Point to the DLL provided by Cypress
# Windows
dll = "C:\\Program Files (x86)\\Cypress\\USB-Serial SDK\\library\\cyusbserial\\x64\\cyusbserial.dll"
# Linux (e.g. Raspberry Pi)
#dll = "/usr/local/lib/libcyusbserial.so"

# Load the DLL
lib = CyUSBSerial(lib = dll)

#dev = lib.find().next() # Use first device found
dev = lib.find(vid=0x04B4,pid=0x0003).next() # Look for a specific vendor and product id

# Access GPIO
gpio = CyGPIO(dev)

out_pin = gpio.pin(1) # GPIO Pin 1
in_pin = gpio.pin(2) # GPIO Pin 2

try:
    while(True): # Repeat until user presses Ctrl-C
        out_pin.set(1) # Set the output pin high
        print 'Input pin:',in_pin.get() # Read the input pin
        time.sleep(1) # Sleep
        out_pin.set(0) # Set the output pin low
        print 'Input pin:',in_pin.get() # Read the input pin
        time.sleep(1) # Sleep

except KeyboardInterrupt:
        print 'Ctrl-C received!'

finally:
    print 'Bye!'
