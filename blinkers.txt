import time
import machine
import random


def clr_scr():
    graph.set_pen(graph.create_pen(0, 0, 0))
    graph.rectangle(0, 0, 16, 16)
    su.update(graph)
    return None

def explosion():
    time.sleep(.1)
    wa = 5
    wb = 6
    white = (250, 250, 250)
    blue = (10, 10, 155)
    col = blue
    
    for i in range(5):
        graph.set_pen(graph.create_pen(col[0], col[1], col[2]))
        graph.rectangle(wa, wa, wb, wb)
        su.update(graph)
        time.sleep(.08)
        clr_scr()
        wa += 1
        wb -= 2

    fac = 16
    for i in range(16):
        fac -= 1
        col = white
        graph.set_pen(graph.create_pen(int((col[0] * (fac-6)) / 52), int((col[1] * (fac-6)) / 52), int((col[2] * (fac-6)) / 52)))
        graph.rectangle(0, 0, 16, 16)
        if i < 1:
            graph.set_pen(graph.create_pen(160, 160, 160))
            graph.rectangle(0, 0, 16, 16)
        col = blue
        graph.set_pen(graph.create_pen(col[0], col[1], col[2]))
        graph.circle(7, 7, i)
        graph.set_pen(graph.create_pen(int((col[0] * i) / 52), int((col[1] * i) / 52), int((col[2] * i) / 52)))
        graph.circle(7, 7, i-1)
        col = white
        graph.set_pen(graph.create_pen(int((col[0] * fac) / 52), int((col[1] * fac) / 52), int((col[2] * fac) / 52)))
        graph.circle(7, 7, i-2)
        su.update(graph)
        time.sleep(.1)
    return None

def center_blink():
    clr_scr()
    blue = (10, 10, 155)
    white = (250, 250, 250)
    col = blue
    
    for i in range(0, 3):
        #print(i)
        graph.set_pen(graph.create_pen(col[0], col[1], col[2]))
        graph.rectangle(6, 6, 4, 4)
        su.update(graph)
        time.sleep(.6)
        graph.set_pen(graph.create_pen(0, 0, 0))
        graph.rectangle(6, 6, 4, 4)
        su.update(graph)
        time.sleep(.5)
    return None

def diffuse_blink_explosion():
    blue = (10, 10, 155)
    white = (250, 250, 250)
    col = blue
    
    for i in range(80):
        #print(i)
        r1 = 6
        r2 = 9
        x1 = random.randint(r1, r2)
        x2 = random.randint(r1, r2)
        x3 = random.randint(r1, r2)
        x4 = random.randint(r1, r2)
        y1 = random.randint(r1, r2)
        y2 = random.randint(r1, r2)
        y3 = random.randint(r1, r2)
        y4 = random.randint(r1, r2)
        graph.set_pen(graph.create_pen(col[0], col[1], col[2]))
        graph.pixel(x1, y1)
        graph.pixel(x2, y2)
        graph.pixel(x3, y3)
        graph.pixel(x4, y4)
        su.update(graph)
        time.sleep(.05)
        graph.set_pen(graph.create_pen(0, 0, 0))
        graph.pixel(x1, y1)
        graph.pixel(x2, y2)
        graph.pixel(x3, y3)
        graph.pixel(x4, y4)
        su.update(graph)
    #---> explosion
    time.sleep(.1)
    wa = 5
    wb = 6
    white = (250, 250, 250)
    blue = (10, 10, 155)
    col = blue
    
    for i in range(5):
        graph.set_pen(graph.create_pen(col[0], col[1], col[2]))
        graph.rectangle(wa, wa, wb, wb)
        su.update(graph)
        time.sleep(.08)
        clr_scr()
        wa += 1
        wb -= 2

    fac = 16
    for i in range(16):
        fac -= 1
        col = white
        graph.set_pen(graph.create_pen(int((col[0] * (fac-6)) / 52), int((col[1] * (fac-6)) / 52), int((col[2] * (fac-6)) / 52)))
        graph.rectangle(0, 0, 16, 16)
        if i < 1:
            graph.set_pen(graph.create_pen(160, 160, 160))
            graph.rectangle(0, 0, 16, 16)
        col = blue
        graph.set_pen(graph.create_pen(col[0], col[1], col[2]))
        graph.circle(7, 7, i)
        graph.set_pen(graph.create_pen(int((col[0] * i) / 52), int((col[1] * i) / 52), int((col[2] * i) / 52)))
        graph.circle(7, 7, i-1)
        col = white
        graph.set_pen(graph.create_pen(int((col[0] * fac) / 52), int((col[1] * fac) / 52), int((col[2] * fac) / 52)))
        graph.circle(7, 7, i-2)
        su.update(graph)
        time.sleep(.1)
    return None

def terminal_blink():
    blue = (10, 10, 155)
    green = (0, 210, 10)
    white = (250, 250, 250)
    col = green
    
    xtb = 1
    ytb = 11
    xxtra = 0
    
    for i in range(14):
        print(i)
        graph.set_pen(graph.create_pen(col[0], col[1], col[2]))
        if i == 7:
            for i in range(3):
                graph.set_pen(graph.create_pen(0, 0, 0))
                graph.rectangle(xtb+xxtra+3, ytb-1, 10, 4)
                graph.set_pen(graph.create_pen(col[0], col[1], col[2]))
                graph.pixel(xtb+xxtra+3, ytb+2)
                graph.rectangle(xtb+xxtra+5, ytb+2, 2, 1)
                su.update(graph)
                time.sleep(.25)
                xxtra = xxtra+2
        #--> indicator
        graph.pixel(xtb, ytb)
        graph.pixel(xtb+1, ytb+1)
        graph.pixel(xtb, ytb+2)
        #--> clear cursor
        graph.set_pen(graph.create_pen(0, 0, 0))
        graph.rectangle(xtb+xxtra+3, ytb-1, 10, 4)
        #--> cursor
        graph.set_pen(graph.create_pen(col[0], col[1], col[2]))
        graph.rectangle(xtb+xxtra+3, ytb+2, 2, 1)
        su.update(graph)
        time.sleep(.5)
        #--> clear cursor
        graph.set_pen(graph.create_pen(0, 0, 0))
        graph.rectangle(xtb+xxtra+3, ytb-1, 10, 4)
        #--> cursor
        graph.set_pen(graph.create_pen(col[0], col[1], col[2]))
        graph.rectangle(xtb+xxtra + 3, ytb-1, 2, 4)
        su.update(graph)
        time.sleep(.5)
    graph.set_pen(graph.create_pen(0, 0, 0))
    graph.rectangle(0, 0, 16, 16)
    su.update(graph)
    time.sleep(2)
    return None


from stellar import StellarUnicorn
from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN as DISPLAY

su = StellarUnicorn()
graph = PicoGraphics(DISPLAY)

time.sleep(1)


#------------------------------------------------->

explosion()
terminal_blink()
center_blink()
diffuse_blink_explosion()

#------------------------------------------------->

print("EOF")




