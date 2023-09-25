from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 50
y = 90

frame = 0

while(True):

    while(x < 750):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame*100, 100, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.05)
        get_events()

    frame = 0

    while(y < 550):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame*100, 300, 100, 100, 750, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.05)
        get_events()

    frame = 0

    while(x > 50):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame*100, 0, 100, 100, x, 550)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.05)
        get_events()

    frame = 0

    while(y > 90):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame*100, 200, 100, 100, 50, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.05)
        get_events()

close_canvas()