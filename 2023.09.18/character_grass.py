from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

delay(5)

close_canvas()

# 파일이 저장된 폴더를 Working Directory로 인식함.
