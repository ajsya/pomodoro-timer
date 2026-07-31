def on_button_pressed_a():
    global index3
    basic.show_string("Starting 25 Min Focus Session")
    for index in range(25):
        if canceled == False:
            basic.show_number(25 - index)
            basic.pause(60000)
        else:
            break
    index3 = 25
    while acknowledged == False:
        doAnimation()
    basic.show_string("Starting 5 Min Break")
    for index2 in range(5):
        basic.show_number(5 - index2)
        basic.pause(60000)
    basic.show_number(0)
    basic.pause(5000)
    showPomodoro()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global canceled
    canceled = True
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def showPomodoro():
    basic.show_leds("""
        . . . . .
        . # # # .
        # # # # #
        # # # # #
        . # # # .
        """)

def on_button_pressed_b():
    global acknowledged
    if index32 == 25:
        acknowledged = True
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global acknowledged
    if index32 == 25:
        acknowledged = True
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

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

index32 = 0
acknowledged = False
index3 = 0
canceled = False
doAnimation()
showPomodoro()

def on_forever():
    pass
basic.forever(on_forever)
