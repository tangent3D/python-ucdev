### Installation
Linux: Copy [90-cyusb.rules](cypress/linux/90-cyusb.rules) to `/etc/udev/
rules.d` and reboot to reload udev rules.
No special installation steps are required for Windows.

### Usage
Control Cypress USB-Serial GPIO3 state for active low POWER# on and off.

`gpio3 [--on] [--off] [--reset]`

### Licensing
Cypress USB-Serial library files are provided under the LGPL 2.1 license.

These files can additionally be obtained or built from the Cypress USB-Serial SDK at https://www.infineon.com/cms/en/design-support/tools/sdk/usb-controllers-sdk/usb-serial-software-development-kit/.
