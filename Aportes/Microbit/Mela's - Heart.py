def Heart_2():
    basic.show_leds("""
        . . . # .
        . . # # #
        . . # # #
        . . . # #
        . . . . #
        """)
    basic.show_leds("""
        . . # . #
        . # # # #
        . # # # #
        . . # # #
        . . . # .
        """)
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.show_leds("""
        # . # . .
        # # # # .
        # # # # .
        # # # . .
        . # . . .
        """)
    basic.show_leds("""
        . # . . .
        # # # . .
        # # # . .
        # # . . .
        # . . . .
        """)

def on_button_pressed_a():
    music.play_tone(659, music.beat(BeatFraction.HALF))
    music.play_tone(622, music.beat(BeatFraction.HALF))
    music.play_tone(659, music.beat(BeatFraction.HALF))
    music.play_tone(622, music.beat(BeatFraction.HALF))
    music.play_tone(659, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(587, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.stop_melody(MelodyStopOptions.ALL)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.start_melody(music.built_in_melody(Melodies.ODE), MelodyOptions.ONCE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def Heart_1():
    basic.show_leds("""
        # . . . .
        # # . . #
        # # . . #
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . #
        # . . # #
        # . . # #
        . . . . #
        . . . . .
        """)

def on_forever():
    basic.show_leds("""
        # # . # #
        # . # . #
        # . . . #
        # . . . #
        # . . . #
        """)
    basic.show_leds("""
        # . # # .
        . # . # .
        . . . # .
        . . . # .
        . . . # .
        """)
    basic.show_leds("""
        . # # . .
        # . # . .
        . . # . .
        . . # . .
        . . # . .
        """)
    basic.show_leds("""
        # # . . #
        . # . . #
        . # . . #
        . # . . #
        . # . . #
        """)
    basic.show_leds("""
        # . . # #
        # . . # .
        # . . # #
        # . . # .
        # . . # #
        """)
    basic.show_leds("""
        . . # # #
        . . # . .
        . . # # #
        . . # . .
        . . # # #
        """)
    basic.show_leds("""
        . # # # .
        . # . . .
        . # # # .
        . # . . .
        . # # # .
        """)
    basic.show_leds("""
        # # # . .
        # . . . .
        # # # . .
        # . . . .
        # # # . .
        """)
    basic.show_leds("""
        # # . . #
        . . . . #
        # # . . #
        . . . . #
        # # . . #
        """)
    basic.show_leds("""
        # . . # .
        . . . # .
        # . . # .
        . . . # .
        # . . # #
        """)
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # # #
        """)
    basic.show_leds("""
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # # # .
        """)
    basic.show_leds("""
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        # # # . .
        """)
    basic.show_leds("""
        . . . . #
        . . . . #
        . . . . #
        . . . . #
        # # . . #
        """)
    basic.show_leds("""
        . . . # #
        . . . # .
        . . . # #
        . . . # .
        # . . # .
        """)
    basic.show_leds("""
        . . # # #
        . . # . #
        . . # # #
        . . # . #
        . . # . #
        """)
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        # # # . .
        # . # . .
        # # # . .
        # . # . .
        # . # . .
        """)
    basic.show_leds("""
        # # . . .
        . # . . .
        # # . . .
        . # . . .
        . # . . .
        """)
    basic.show_leds("""
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . #
        . . . # #
        . . . # #
        . . . . #
        . . . . .
        """)
    Heart_2()
    for index in range(3):
        Heart_1()
        Heart_2()
    basic.show_leds("""
        # . . . .
        # # . . .
        # # . . .
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
basic.forever(on_forever)
