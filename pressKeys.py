import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode

with open('main.py', 'r') as f:
    output = f.read()

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(keyboard)
time.sleep(3)
keyboard.send(Keycode.POUND)
keyboard_layout.write(output.replace('\r', ''))
