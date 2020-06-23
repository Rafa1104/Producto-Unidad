def on_gesture_shake():
    global Pasos
    Pasos += 1
    basic.show_number(Pasos)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global Pasos
    Pasos = 0
    basic.show_number(Pasos)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

Pasos = 0
Pasos = 0
basic.show_number(Pasos)
