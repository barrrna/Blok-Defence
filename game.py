#Barna Alimu
import gamebox
import random
camera = gamebox.Camera(800,600)

#images
p = gamebox.from_image(400, 300, 'player_image.png')
p.scale_by(0.09)
back = gamebox.from_image(500, 100, 'backgroud.png')
back.scale_by(0.9)
mouse = gamebox.from_color(999, 999, "light green", 10, 10)
explosion_images = gamebox.load_sprite_sheet('sprite.png', 2, 5)
current_frame = 9
bomb = gamebox.from_image(999,999, explosion_images[0])
bomb.scale_by(.5)
#initial values
rocks = []
coins = []
timer = 0
p_score = 0
gameOver = False
difficulty = 1

def create_rocks():
    # randomly generates rocks from 6 sides
    ran = random.randint(1,6)
    if ran == 1:
        TL = gamebox.from_image(0, 0, 'space_rock.png')
        TL.speedx = 3 * difficulty
        TL.speedy = 2 * difficulty
        TL.scale_by(.13)
        rocks.append(TL)
    if ran == 2:
        TR = gamebox.from_image(800, 0, 'space_rock.png')
        TR.speedx = -3 * difficulty
        TR.speedy = 2 * difficulty
        TR.scale_by(.13)
        rocks.append(TR)
    if ran == 3:
        BL = gamebox.from_image(0, 600, 'space_rock.png')
        BL.speedx = 3 * difficulty
        BL.speedy = -2 * difficulty
        BL.scale_by(.13)
        rocks.append(BL)
    if ran == 4:
        BR = gamebox.from_image(800, 600, 'space_rock.png')
        BR.speedx = -3 * difficulty
        BR.speedy = -2 * difficulty
        BR.scale_by(.13)
        rocks.append(BR)
    if ran == 5 or ran == 6:
        RM = gamebox.from_image(0, 300, 'space_rock.png')
        RM.speedx = 3 * difficulty
        RM.speedy = 0
        RM.scale_by(.13)
        rocks.append(RM)
    if ran == 6 or ran == 5:
        LM = gamebox.from_image(800, 300, 'space_rock.png')
        LM.speedx = -3 * difficulty
        LM.speedy = 0
        LM.scale_by(.13)
        rocks.append(LM)
    ran_2 = random.randint(1, 12)
    if ran_2 == 7:
        coin = gamebox.from_image(random.randint(0,800), random.randint(0,600), 'coin.png')
        coin.scale_by(.07)
        coins.append(coin)

def create_explosion():
    global current_frame
    current_frame += 1
    if(current_frame < 8):
        bomb.image = explosion_images[int(current_frame)]

def tick(keys):
    global timer
    global gameOver
    global current_frame
    global difficulty
    global p_score
    camera.draw(back)
    timer += 1
    p.rotate(-1)

    #generagtes rock every second
    if timer % 30 == 0:
        create_rocks()

    if camera.mouseclick:
        mouse.center = camera.mouse

    #draws the rocks and removes rocks once mouse clicks
    for rock in rocks:
        rock.rotate(-1)
        rock.move_speed()
        if rock.touches(mouse):
            bomb.x = rock.x
            bomb.y = rock.y
            current_frame = 0
            rocks.remove(rock)
            p_score += 100
        if rock.touches(p):
            gameOver = True

    for coin in coins:
        if coin.touches(mouse):
            coins.remove(coin)
            p_score += 200
    # moves cursor off screen
    mouse.center = (999,999)

    #draw list
    for rock in rocks:
        camera.draw(rock)
    for coin in coins:
        camera.draw(coin)

    #multiple levels
    if p_score == 1000:
        difficulty = 2
        camera.draw(gamebox.from_text(400, 200, "NEXT LEVEL!", 100, "White", bold=True))
    if p_score == 2000:
        difficulty = 3
        camera.draw(gamebox.from_text(400, 200, "NEXT LEVEL!", 100, "White", bold=True))
    if p_score == 3000:
        camera.draw(gamebox.from_text(400, 200, "NEXT LEVEL!", 100, "White", bold=True))
        difficulty = 3.5
    if p_score == 4000:
        camera.draw(gamebox.from_text(400, 200, "NEXT LEVEL!", 100, "White", bold=True))
        difficulty = 4

    #draw function
    camera.draw(p)
    camera.draw(mouse)
    create_explosion()
    camera.draw(bomb)
    camera.draw(gamebox.from_text(80, 570, "score: " + str(p_score), 30, "orange", bold=False))
    camera.display()

    if gameOver:
        camera.clear("gray")
        camera.draw(gamebox.from_text(400, 200, "Game Over!", 100, "Black", bold=True))
        camera.draw(gamebox.from_text(400, 500, "score: " + str(p_score), 60, "white", bold=False))
        gamebox.pause()
    camera.display()
gamebox.timer_loop(30, tick)