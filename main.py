"""
pomodoro-timer
author: ajsya
purpose: a pomodoro-timer for the BBC micro:bit
usage:
    - button a to start 25 min timer
    - button b or shake to acknowledge when focus timer is off and start 5 min break timer
    - button a + b to cancel timer
"""

# # input functions

def on_button_pressed_a():
    global canceled
    
    doFocusTimer()

    if canceled == False:
        # do animation until timer is acknowledged
        while acknowledged == False:
            doAnimation()
        
        # do 5 min break timer
        doBreakTimer()
    
    # reset pomodoro timer
    showPomodoro()
    canceled = False
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global canceled
    canceled = True
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    cancelTimer()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    cancelTimer()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# # process functions
def doFocusTimer():
    global timerDone
    for index in range(25):
        if canceled == False:
            basic.show_number(25 - index)
            basic.pause(60000)
        else:
            break
    timerDone = True

def doBreakTimer():
    for index2 in range(5):
        basic.show_number(5 - index2)
        basic.pause(60000)
    basic.show_number(0)
    basic.pause(5000)

def cancelTimer():
    global acknowledged
    if timerDone == True:
        acknowledged = True

# # display functions
def doAnimation():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.pause(18)
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
    basic.pause(18)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.pause(18)
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
    basic.pause(18)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.pause(18)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(18)

def showPomodoro():
    basic.show_leds("""
        . . . . .
        . # # # .
        # # # # #
        # # # # #
        . # # # .
        """)

# started on boot

## set variables to be used globally
canceled = False
acknowledged = False
timerDone = False
index32 = 0

## do intro animation
doAnimation()
showPomodoro()