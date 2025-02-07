from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
             if event.key == SDLK_RIGHT:
                 dir_x += 1
             elif event.key == SDLK_LEFT:
                 dir_x -= 1
             elif event.key == SDLK_UP:
                 dir_y += 1
             elif event.key == SDLK_DOWN:
                 dir_y -= 1
             elif event.key == SDLK_ESCAPE:
                 running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                 dir_x -= 1
            elif event.key == SDLK_LEFT:
                 dir_x += 1
            elif event.key == SDLK_UP:
                 dir_y -= 1
            elif event.key == SDLK_DOWN:
                 dir_y += 1

running = True
x = 800 // 2
y = 600 // 2
frame = 0
dir_x = 0
dir_y = 0
while running:
    clear_canvas()
    ground.draw(400, 300, 800, 600)
    character.clip_draw(frame * 256, 320, 230, 300, x, y, 100, 100)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    x += dir_x * 5
    y += dir_y * 5

    if x < 0:
        x = 0
    elif x > 800:
        x = 800

    if y < 0:
        y = 0
    elif y > 600:
        y = 600

    delay(0.05)

close_canvas()
