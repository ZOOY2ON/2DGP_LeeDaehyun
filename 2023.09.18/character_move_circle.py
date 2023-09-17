from pico2d import *
import math

open_canvas()

# 이미지 로딩
grass = load_image('grass.png')
character = load_image('character.png')

# 초기 위치 및 상태 변수 설정
center_x, center_y = 400, 300  # 원의 중심 좌표
radius = 200  # 원의 반지름
angle = 271  # 시작 각도

move = True

while move:
    
    # 원의 중심에서 각도에 따라 이동
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    
    # 캐릭터 그리기
    clear_canvas()  # 이전 프레임 지우기
    character.draw(x, y)
    grass.draw(400, 30)
    update_canvas()
    #print(x, y)
    delay(0.01)
    
    angle += 1  # 각도를 1도씩 증가

    if y == 100 :
        move = False

close_canvas()
