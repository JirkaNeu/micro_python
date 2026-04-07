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

def feed_watchdog(timer):
    wdt.feed()
    print("nom nom")
    #--> try the wdt
    graphics.set_pen(graphics.create_pen(150, 0, 0))
    graphics.rectangle(3, 9, 4, 4)
    stellar.update(graphics)
    time.sleep(6)
    #--> try the wdt


wdt = machine.WDT(timeout=5000)

graphics.set_pen(graphics.create_pen(100, 80, 10))
graphics.rectangle(3, 9, 4, 4)
stellar.update(graphics)
time.sleep(.6)
clr_scr()
time.sleep(1)


timer = machine.Timer()
timer.init(period=3000, mode=machine.Timer.PERIODIC, callback=feed_watchdog)


while True:
    graphics.set_pen(graphics.create_pen(0, 150, 0))
    graphics.rectangle(3, 9, 4, 4)
    stellar.update(graphics)
    time.sleep(0.7)
    clr_scr()
    time.sleep(0.6)


    



