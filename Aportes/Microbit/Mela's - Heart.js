function Heart_2 () {
    basic.showLeds(`
        . . . # .
        . . # # #
        . . # # #
        . . . # #
        . . . . #
        `)
    basic.showLeds(`
        . . # . #
        . # # # #
        . # # # #
        . . # # #
        . . . # .
        `)
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.showLeds(`
        # . # . .
        # # # # .
        # # # # .
        # # # . .
        . # . . .
        `)
    basic.showLeds(`
        . # . . .
        # # # . .
        # # # . .
        # # . . .
        # . . . .
        `)
}
input.onButtonPressed(Button.A, function () {
    music.playTone(659, music.beat(BeatFraction.Half))
    music.playTone(622, music.beat(BeatFraction.Half))
    music.playTone(659, music.beat(BeatFraction.Half))
    music.playTone(622, music.beat(BeatFraction.Half))
    music.playTone(659, music.beat(BeatFraction.Half))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(587, music.beat(BeatFraction.Half))
    music.playTone(523, music.beat(BeatFraction.Half))
    music.playTone(392, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(494, music.beat(BeatFraction.Half))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.playTone(370, music.beat(BeatFraction.Half))
    music.playTone(494, music.beat(BeatFraction.Half))
    music.playTone(523, music.beat(BeatFraction.Half))
    music.playTone(330, music.beat(BeatFraction.Half))
})
input.onButtonPressed(Button.AB, function () {
    music.stopMelody(MelodyStopOptions.All)
})
input.onButtonPressed(Button.B, function () {
    music.startMelody(music.builtInMelody(Melodies.Ode), MelodyOptions.Once)
})
function Heart_1 () {
    basic.showLeds(`
        # . . . .
        # # . . #
        # # . . #
        # . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . #
        # . . # #
        # . . # #
        . . . . #
        . . . . .
        `)
}
basic.forever(function () {
    basic.showLeds(`
        # # . # #
        # . # . #
        # . . . #
        # . . . #
        # . . . #
        `)
    basic.showLeds(`
        # . # # .
        . # . # .
        . . . # .
        . . . # .
        . . . # .
        `)
    basic.showLeds(`
        . # # . .
        # . # . .
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.showLeds(`
        # # . . #
        . # . . #
        . # . . #
        . # . . #
        . # . . #
        `)
    basic.showLeds(`
        # . . # #
        # . . # .
        # . . # #
        # . . # .
        # . . # #
        `)
    basic.showLeds(`
        . . # # #
        . . # . .
        . . # # #
        . . # . .
        . . # # #
        `)
    basic.showLeds(`
        . # # # .
        . # . . .
        . # # # .
        . # . . .
        . # # # .
        `)
    basic.showLeds(`
        # # # . .
        # . . . .
        # # # . .
        # . . . .
        # # # . .
        `)
    basic.showLeds(`
        # # . . #
        . . . . #
        # # . . #
        . . . . #
        # # . . #
        `)
    basic.showLeds(`
        # . . # .
        . . . # .
        # . . # .
        . . . # .
        # . . # #
        `)
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # # #
        `)
    basic.showLeds(`
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # # # .
        `)
    basic.showLeds(`
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        # # # . .
        `)
    basic.showLeds(`
        . . . . #
        . . . . #
        . . . . #
        . . . . #
        # # . . #
        `)
    basic.showLeds(`
        . . . # #
        . . . # .
        . . . # #
        . . . # .
        # . . # .
        `)
    basic.showLeds(`
        . . # # #
        . . # . #
        . . # # #
        . . # . #
        . . # . #
        `)
    basic.showLeds(`
        . # # # .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        `)
    basic.showLeds(`
        # # # . .
        # . # . .
        # # # . .
        # . # . .
        # . # . .
        `)
    basic.showLeds(`
        # # . . .
        . # . . .
        # # . . .
        . # . . .
        . # . . .
        `)
    basic.showLeds(`
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . . #
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . #
        . . . # #
        . . . # #
        . . . . #
        . . . . .
        `)
    Heart_2()
    for (let index = 0; index < 3; index++) {
        Heart_1()
        Heart_2()
    }
    basic.showLeds(`
        # . . . .
        # # . . .
        # # . . .
        # . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
