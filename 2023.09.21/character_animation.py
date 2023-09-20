from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# 초기 위치 및 상태 변수 설정
x, y = 50, 90
move = True
way = ['Right', 'Up', 'Left', 'Down']
image_bottom = {'Right': 100, 'Up': 300, 'Left': 0, 'Down': 200}
frame = 0

# 이동 경로 정의: 오른쪽, 위, 왼쪽, 아래 순서로 움직임
waypoints = [(750, 90), (750, 550), (50, 550), (50, 90)]

i = 0  # 방향 리스트의 인덱스 변수
T_or_F = True

while T_or_F:

    movepoint = (x, y)

    #print(x,y)
    print(movepoint)
    print(waypoints[i])

    if movepoint != waypoints[i]:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, image_bottom[way[i]], 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        if x >= 800:
            T_or_F = False
        else :
            if way[i] == 'Right':
                x += 5
            elif way[i] == 'Up':
                y += 5
            elif way[i] == 'Left':
                x -= 5
            elif way[i] == 'Down':
                y -= 5
            else:
                print('Error')
        delay(0.05)
    elif movepoint == waypoints[i]:
        print("===========change=================")
        i = (i + 1) % 4  # 다음 방향으로 이동

close_canvas()