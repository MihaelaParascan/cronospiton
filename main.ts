input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    start = 1
})
let SEC = 0
let start = 0
basic.showNumber(SEC)
let minute = 0
basic.forever(function on_forever() {
    let minute: number;
    
    if (start == 1) {
        basic.pause(1000)
        SEC = SEC + 1
        if (SEC == 60) {
            minute = minute + 1
            SEC = 0
        }
        
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    start = 0
})
basic.forever(function on_mereu() {
    //  basic.show_number(SEC)
    basic.showString("" + minute + ":" + ("" + SEC))
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    start = 0
    SEC = 0
    minute = 0
})
