from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

#grass = load_image('grass.png')
character = load_image('animation_sheet4.png')


def handle_events():
    global running, dir,dir_y
    global idle

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            idle = False
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key ==SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

            elif event.key == SDLK_UP:
                dir_y +=1
            elif event.key == SDLK_DOWN:
                dir_y -=1

        elif event.type == SDL_KEYUP:
            idle = True
        #idle이 true이면 idle 모션을 넣어준다.
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            # fill
            if event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1




running = True
idle = True
x = 1280 / 2
y = 1024 / 2
frame = 0
dir = 0
dir_y = 0
# fill here

# running 중일때


while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2) #왜 2로 나누지? 왜 나누는데 커지지

    if(idle == True):
        character.clip_draw(120,130,120,130,x,y)
    else:
        character.clip_draw(frame*120,130,120,130,x,y)

    update_canvas()
    handle_events()
    frame = (frame+1)%8

    #이동
    if (80 <= x <= 1200 and 100 <= y <= 970):
        x += dir * 5
        y += dir_y * 5
    else:
        if(x<80):
            x= 80 +10
        elif(x >1200):
            x =1200-10 # 오른 벽

        if(y <100):
            y = 100+10 #밑
        elif(y >970):
            y = 970-10 #위
    delay(0.05)





close_canvas()

