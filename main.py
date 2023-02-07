def on_button_pressed_a():
    global start
    start = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

SEC = 0

start = 0
basic.show_number(SEC)
minute = 0

def on_forever():
    global SEC
    if start==1:
        basic.pause(1000)
        SEC = SEC + 1
        if SEC==60:
            minute=minute+1
            SEC=0
basic.forever(on_forever)
def on_button_pressed_b():
    global start
    start=0
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_mereu():
    # basic.show_number(SEC)
    basic.show_string(str(minute)+":"+str(SEC))
basic.forever(on_mereu)
def on_button_pressed_ab():
    global SEC,start,minute
    start=0
    SEC=0
    minute=0
input.on_button_pressed(Button.AB, on_button_pressed_ab)
