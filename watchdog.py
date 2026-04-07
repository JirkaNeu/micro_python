import machine
import time
import random
import sys

time.sleep(.5)

from stellar import StellarUnicorn
from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN as DISPLAY

stellar = StellarUnicorn()
graphics = PicoGraphics(DISPLAY)

def clr_scr():
    graphics.set_pen(graphics.create_pen(0, 0, 0))
    graphics.rectangle(0, 0, 16, 16)
    stellar.update(graphics)
    return None


wdt = machine.WDT(timeout=5000)  # 5000 milliseconds = 5 seconds


graphics.set_pen(graphics.create_pen(150, 50, 0))
graphics.rectangle(3, 9, 4, 4)
stellar.update(graphics)
time.sleep(.6)
clr_scr()


def feed_watchdog(timer = 3000):
    wdt.feed()
    print("Watchdog fed")


#timer = machine.Timer()
#timer.init(period=3000, mode=machine.Timer.PERIODIC, callback=feed_watchdog)

# Main loop
while True:
    graphics.set_pen(graphics.create_pen(0, 150, 0))
    graphics.rectangle(3, 9, 4, 4)
    stellar.update(graphics)
    time.sleep(0.6)
    clr_scr()
    time.sleep(0.6)
    feed_watchdog()
    #--> try the wdt
    graphics.set_pen(graphics.create_pen(150, 0, 0))
    graphics.rectangle(3, 9, 4, 4)
    stellar.update(graphics)
    time.sleep(6)
    



