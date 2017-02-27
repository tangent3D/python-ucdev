# Test the Cypress CY7C65213 GPIO Pins with simultaneous pyserial communication
# using Python 2.7 notation. Some of the following is deprecated in Python 3.0

# Before you run this test, use the Cypress USB-Serial Configuration Utility to:
#  Set UART Notification LED settings to "None" (which allows GPIO_0 and _1 to be
#   used as outputs instead of driving the Tx and Rx LEDs)
#  Configure GPIO_0 and GPIO_1 as "Drive 0" (i.e. low output as default)
#  Configure GPIO_2 as "Input" (instead of "Tristate")

# Connect GPIO_0 to GPIO_2 using a jumper wire

# Connect TXD to RXD using a jumper wire
# Connect RTS to CTS using a jumper wire
# Connect DTR to DSR using a jumper wire

from cy7c65213 import CyUSBSerial, CyGPIO
import time
import serial

# COM port name (from Device Manager)
com_port = 'COM6'

# Load DLL provided by Cypress
dll = "C:\\Program Files (x86)\\Cypress\\USB-Serial SDK\\library\\cyusbserial\\x64\\cyusbserial.dll"
lib = CyUSBSerial(lib = dll)

#dev = lib.find().next() # Use first device found
dev = lib.find(vid=0x04B4,pid=0x0003).next() # Look for a specific vendor and product id

# Access GPIO
gpio = CyGPIO(dev)

out_pin = gpio.pin(0) # GPIO Pin 0
in_pin = gpio.pin(2) # GPIO Pin 2

# Open serial port
ser = serial.Serial(com_port, 115200, timeout=0.5)

count = 0 # Initialise count

try:
    while(True): # Repeat until user presses Ctrl-C
        for x in [0,1]: # Alternate low and high (False and True)
            ser.setRTS(x) # Set the RTS pin
            ser.setDTR(x) # Set the DTR pin
            out_pin.set(x) # Set the output pin
            ser.write('%05i\n'%count) # Write count to serial port
            time.sleep(0.5) # Let the pins stabilise
            print 'CTS:',ser.getCTS() # Get CTS status
            print 'DSR:',ser.getDSR() # Get DSR status
            print 'Input pin:',in_pin.get() # Read the input pin
            print 'Received:',ser.read(100) # Try to read 100 characters forcing a timeout
            count += 1 # Increment count

except KeyboardInterrupt:
        print 'Ctrl-C received!'

finally:
    ser.close()
    print 'Bye!'
