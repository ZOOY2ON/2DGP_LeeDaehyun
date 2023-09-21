#Drill02 캐릭터 사각 운동과 원 운동
# 사각형 운동과 원 운동을 번갈아 가면서 무한 반복함

from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def rander_frame(x,y):
    clear_canvas_now()
    grass.draw_now()
    character.draw_now(x,y)
    delay(0.01)
    print(x,y)

from pico2d import *
import math

open_canvas()

glass = load_image('grass.png')
character = load_image('character.png')

def render_frame(x,y):
    clear_canvas_now()
    glass.draw_now(400,30)
    character.draw_now(x, y)
    delay(0.01)
    
def move_circle(): 
    
    #일단 그림을 그리자
    cx, cy, r = 800 // 2, 600 // 2, 200
    
    for degree in range(0,360,5):
        x = cx + r * math.cos(math.radians(degree))
        y = cy + r * math.sin(math.radians(degree))
        render_frame(x,y)

def move_rectangle():
    for x in range(50,750+1,10): #하단 좌->우
        render_frame(x,90)

    for y in range(90, 510+1, 10): # 우측 하->상
        render_frame(750,y)
        
    for x in range(750,50-1,-10): #상단 우->좌
        render_frame(x,510)
        
    for y in range(510, 90-1, -10): # 좌측 상->하
        render_frame(50,y)
        
while True:
    #move_circle()
    move_rectangle()
    break
    
close_canvas()
