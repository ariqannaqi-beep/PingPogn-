from pygame import *

window_Width = 600
window_Height = 400
window = display.set_mode((window_Width, window_Height))
display.set_caption("Ping pogn!")

#connditions
Run = True

GameTime = time.Clock()
while Run:
    for e in event.get():
        if e.type == QUIT:
            Run = False

    window.fill((0, 0, 0))
    display.update()
    GameTime.tick(60)
