import os
import board
import time
import terminalio
import displayio
import busio
from adafruit_display_text import label
import adafruit_st7789

print("==============================")
print(os.uname())
print("Hello Raspberry Pi Pico/CircuitPython ST7789 SPI IPS Display")
print(adafruit_st7789.__name__ + " version: " + adafruit_st7789.__version__)
print()

# Release any resources currently in use for the displays
displayio.release_displays()

tft_cs = board.GP17
tft_dc = board.GP16
#tft_res = board.GP23
spi_mosi = board.GP19
spi_clk = board.GP18

spi = busio.SPI(spi_clk, MOSI=spi_mosi)

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs
)

#display = adafruit_st7789.ST7789(display_bus,
#                    width=135, height=240,
#                    rowstart=40, colstart=53)
#display.rotation = 270

# Create the ST7789 display:
display = adafruit_st7789.ST7789(
    display_bus,
    width=240,
    height=240,
    rowstart=80,
    colstart=0,
    rotation=180,
)

group = displayio.Group()
display.show(group)

bitmap = displayio.Bitmap(240, 240, 135)

palette = displayio.Palette(240)
for p in range(240):
    palette[p] = (0x010000*p) + (0x0100*p) + p

for y in range(240):
    for x in range(240):
        bitmap[x,y] = y
        
tileGrid = displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0)
group.append(tileGrid)

time.sleep(3.0)

while True:
    for p in range(240):
        palette[p] = p
    time.sleep(3.0)

    for p in range(240):
        palette[p] = 0x0100 * p
    time.sleep(3.0)

    for p in range(240):
        palette[p] = 0x010000 * p
    time.sleep(3.0)