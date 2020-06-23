let Registro = 0
input.onButtonPressed(Button.A, function () {
    Registro += 1
    basic.showNumber(Registro)
})
input.onButtonPressed(Button.AB, function () {
    Registro = 0
    basic.showNumber(Registro)
})
input.onButtonPressed(Button.B, function () {
    Registro += -1
    basic.showNumber(Registro)
})
