input.onButtonPressed(Button.A, function () {
    for (let index = 0; index <= 24; index++) {
        if (canceled == false) {
            basic.showNumber(25 - index)
            basic.pause(60000)
        } else {
            break;
        }
    }
    if (canceled == false) {
        while (acknowledged == false) {
            doAnimation()
        }
        basic.showString("Starting 5 Min Break")
        for (let index2 = 0; index2 <= 4; index2++) {
            basic.showNumber(5 - index2)
            basic.pause(60000)
        }
        basic.showNumber(0)
        basic.pause(5000)
    }
    showPomodoro()
    canceled = false
})
input.onButtonPressed(Button.AB, function () {
    canceled = true
})
function showPomodoro () {
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        # # # # #
        . # # # .
        `)
}
input.onButtonPressed(Button.B, function () {
    if (index32 == 25) {
        acknowledged = true
    }
})
input.onGesture(Gesture.Shake, function () {
    if (index32 == 25) {
        acknowledged = true
    }
})
function doAnimation () {
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
let index32 = 0
let acknowledged = false
let canceled = false
doAnimation()
showPomodoro()
basic.forever(function () {
	
})
