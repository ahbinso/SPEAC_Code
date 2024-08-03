# Set_Up

1. Download CircuitPython from this link: "https://circuitpython.org/board/adafruit_qtpy_rp2040/". (Currently using V 9.1.1)
2. Plug in the QT Py RP2040 -- it should show up as RP1/RP2.
3. Drag and drop the .uf2 file from step 1 into the RP1/RP2 external drive. The drive should now appear as CIRCUITPY.
4. Go to "https://circuitpython.org/libraries" and scroll to Bundles. Under Bundles, download 'Bundle for Version 9.X'.
5. Unzip & extract the bundle. From there, locate the following files/folders and copy them to the 'lib' folder in your CIRCUITPY drive:
       - adafruit_bus_device
       - adafruit_circuitplayground
       - adafruit_mpr121.mpy
       - adafruit_pixelbyf.mpy
       - adafruit_waveform
6. Download all .wav files from this repository and move them into your CIRCUITPY drive.
8. Copy the contents of'code.py' file onto the 'code.py' file on the CIRCUITPY.

 # Troubleshooting_Code

1. Open terminal in your code editor.
2. Type in "ls /dev/tty.*" and press enter.
3. A USB or USB Modem will appear in the address. (ex. usbmodem11201)
4. Type in "screen /dev/tty.[USB NAME] 115200" and press enter.
5. You have entered screen mode and will be able to see all terminal outputs now. Good luck!
