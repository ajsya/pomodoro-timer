"""
pomodoro-timer
author: ajsya
purpose: a pomodoro-timer for the BBC micro:bit
usage:
    - button a to start 25 min timer
    - button b to cancel timer prematurely
    - button b or shake to acknowledge when focus timer is off and start 5 min break timer
"""

from microbit import *

# display functions

def doAnimation():
    PAUSE_DELAY = 250 # pause delay between images in ms
    
    display.show(Image('00000:'
                       '00000:'
                       '00900:'
                       '00000:'
                       '00000:'))
    sleep(PAUSE_DELAY)
    display.show(Image('00000:'
                       '09990:'
                       '09990:'
                       '09990:'
                       '00000:'))
    sleep(PAUSE_DELAY)
    display.show(Image('99999:'
                       '99999:'
                       '99999:'
                       '99999:'
                       '99999:'))
    sleep(PAUSE_DELAY)
    display.show(Image('00000:'
                       '09990:'
                       '09990:'
                       '09990:'
                       '00000:'))
    sleep(PAUSE_DELAY)
    display.show(Image('00000:'
                       '00000:'
                       '00900:'
                       '00000:'
                       '00000:'))
    sleep(PAUSE_DELAY)
    display.clear()
    sleep(PAUSE_DELAY)

def showPomodoro():
    display.show(Image('00000:'
                       '09990:'
                       '99999:'
                       '99999:'
                       '09990:'))

# process functions

def doFocusTimer():
    display.clear()

    global cancel

    for y in range(5):
            if cancel == True:
                break
            for x in range(5):
                if cancel == True:
                    break
                i = 0
                while i < 60:
                    if button_b.was_pressed():
                        cancel = True
                        break
                    display.set_pixel(x,y,9)
                    sleep(500)
                    display.set_pixel(x,y,0)
                    sleep(500)
                    i = i + 1
                display.set_pixel(x,y,9)
            
def doBreakTimer():
    for index2 in range(5):
        display.show(5 - index2)
        sleep(1000)
    display.show(0)
    sleep(5000)

# started on boot

## set variables to be used globally
cancel = False

## do intro animation
doAnimation()
showPomodoro()

while True:
    if button_a.was_pressed():
        doFocusTimer()

        if cancel == False:
            while button_b.was_pressed() == False:
                doAnimation()
            
            doBreakTimer()
        
        # reset pomodoro timer
        cancel = False
        showPomodoro()
