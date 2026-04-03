import time
import network
import ntptime
import machine

from stellar import StellarUnicorn
from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN as DISPLAY
# create stellar object and graphics surface for drawing
stellar = StellarUnicorn()
graphics = PicoGraphics(DISPLAY)


try:
    from WIFI_CONFIG import SSID, PSK
except ImportError:
    print("Create WIFI_CONFIG.py with your WiFi credentials")



WIDTH = 16  # StellarUnicorn.WIDTH
HEIGHT = 16  # StellarUnicorn.HEIGHT

rtc = machine.RTC()

#DAYS = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
DAYS = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

# Enable the Wireless
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#------------------------------------------------->

def network_connect(ssid, psk):
    # Number of attempts to make before timeout
    max_wait = 5
    
    # Sets the Wireless LED pulsing and attempts to connect to your local network.
    print("connecting... (try: " + str(6-max_wait) +")")
    #wlan.config(pm=0xa11140)  # Turn WiFi power saving off for some slow APs
    wlan.connect(ssid, psk)
    
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(2)
    
    # Handle connection error. Switches the Warn LED on.
    if wlan.status() != 3:
        print("Unable to connect. Attempting connection again")


# Function to sync the Pico RTC using NTP
def sync_time():
    try:
        network_connect(SSID, PSK)
    except NameError:
        print("Create WIFI_CONFIG.py with your WiFi credentials")

    if wlan.status() < 0 or wlan.status() >= 3:
        try:
            ntptime.settime()
            draw()
        except OSError:
            print("Unable to sync with NTP server. Check network and try again.")


def init():
    global time_start
    time_start = time.time()
    print("script starts")
    #print(time_start)
    sync_time()


def draw():
    while True:
        # Pens
        RED = graphics.create_pen(120, 0, 0)
        WHITE = graphics.create_pen(255, 255, 255)
        black = graphics.create_pen(0, 0, 0)
        other = graphics.create_pen(55, 155, 155)

        current_t = rtc.datetime()

        #graphics.set_pen(WHITE)
        graphics.set_pen(RED)
        graphics.clear()

        # Measures the length of the text to help us with centring later.
        day_length = graphics.measure_text(DAYS[current_t[3]], 1)
        date_length = graphics.measure_text(str(current_t[2]), 1)

        graphics.set_font("bitmap6")
        #graphics.set_pen(RED) # upper red rect
        graphics.set_pen(black) # upper red rect
        graphics.rectangle(0, 0, WIDTH, 7)
        #graphics.set_pen(WHITE) # uper letters
        graphics.set_pen(other) # uper letters
        graphics.text(DAYS[current_t[3]], (WIDTH // 2) - (day_length // 2), 0, 16, 1)

        graphics.set_pen(black) # upper red rect
        graphics.rectangle(0, 8, WIDTH, 8)
        #graphics.set_pen(RED)
        graphics.set_pen(other)
        graphics.set_font("bitmap6")
        graphics.text(str(current_t[2]), (WIDTH // 2) - (date_length // 2) + 1, 8, 16, 1)

        graphics.set_pen(graphics.create_pen(0, 0, 0))
        
        #--> slow down infinity
        time.sleep(.8)
        time_now = time.time()
        time_gone = time_start - time_now
        print(time_gone)
        if time_gone <= 7175:
            wlan.active(False)  # deactivate interface
            print("shutting down wlan-modul")
            time.sleep(3)
            machine.reset()
        stellar.update(graphics)

print("wait a second...")
time.sleep(1.5)
init()


