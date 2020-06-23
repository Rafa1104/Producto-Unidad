Registro = 0

def on_button_pressed_a():
    global Registro
    Registro += 1
    basic.show_number(Registro)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Registro
    Registro = 0
    basic.show_number(Registro)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Registro
    Registro += -1
    basic.show_number(Registro)
input.on_button_pressed(Button.B, on_button_pressed_b)
