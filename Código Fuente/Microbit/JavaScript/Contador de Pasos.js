input.onGesture(Gesture.Shake, function () {
    Pasos += 1
    basic.showNumber(Pasos)
})
input.onButtonPressed(Button.AB, function () {
    Pasos = 0
    basic.showNumber(Pasos)
})
let Pasos = 0
Pasos = 0
basic.showNumber(Pasos)
