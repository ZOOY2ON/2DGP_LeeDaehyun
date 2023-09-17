from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0

while (x < 800):
    #Game Rendering
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    #---

    #Game Logic
    x = x + 2
    #---
    
    delay(0.01)
    
close_canvas()

#깜박거린다
