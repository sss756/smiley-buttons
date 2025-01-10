input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Sad)
    music.play(music.stringPlayable("C5 B A G F E D C ", 500), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Happy)
    music.play(music.stringPlayable("C5 C5 C5 C5 C5 C5 C5 C5 ", 500), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Meh)
    music.play(music.stringPlayable("C C C C C C C C ", 500), music.PlaybackMode.UntilDone)
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Silly)
    music.play(music.stringPlayable("E B C5 A B G A F ", 120), music.PlaybackMode.UntilDone)
})
