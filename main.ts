/** 
pomodoro-timer
author: ajsya
purpose: a pomodoro-timer for the BBC micro:bit
usage:
    - button a to start 25 min timer
    - button b or shake to acknowledge when focus timer is off and start 5 min break timer
    - button a + b to cancel timer

 */
//  # input functions
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    doFocusTimer()
    if (canceled == false) {
        //  do animation until timer is acknowledged
        while (acknowledged == false) {
            doAnimation()
        }
        //  do 5 min break timer
        doBreakTimer()
    }
    
    //  reset pomodoro timer
    showPomodoro()
    canceled = false
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    canceled = true
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    cancelTimer()
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    cancelTimer()
})
//  # process functions
function doFocusTimer() {
    
    for (let index = 0; index < 25; index++) {
        if (canceled == false) {
            basic.showNumber(25 - index)
            basic.pause(60000)
        } else {
            break
        }
        
    }
    timerDone = true
}

function doBreakTimer() {
    for (let index2 = 0; index2 < 5; index2++) {
        basic.showNumber(5 - index2)
        basic.pause(60000)
    }
    basic.showNumber(0)
    basic.pause(5000)
}

function cancelTimer() {
    
    if (timerDone == true) {
        acknowledged = true
    }
    
}

//  # display functions
function doAnimation() {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.pause(18)
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    basic.pause(18)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.pause(18)
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    basic.pause(18)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.pause(18)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(18)
}

function showPomodoro() {
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        # # # # #
        . # # # .
        `)
}

//  started on boot
// # set variables to be used globally
let canceled = false
let acknowledged = false
let timerDone = false
let index32 = 0
// # do intro animation
doAnimation()
showPomodoro()
