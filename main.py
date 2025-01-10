def on_button_pressed_a():
    basic.show_icon(IconNames.SAD)
    music.play(music.string_playable("C5 B A G F E D C ", 500),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_icon(IconNames.HAPPY)
    music.play(music.string_playable("C5 C5 C5 C5 C5 C5 C5 C5 ", 500),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.MEH)
    music.play(music.string_playable("C C C C C C C C ", 500),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_icon(IconNames.SILLY)
    music.play(music.string_playable("E B C5 A B G A F ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
