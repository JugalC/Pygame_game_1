import pygame
import random
import pygame.freetype

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF)  # Setting window size
pygame.display.set_caption('Ocean Adventure')  # Setting the title of the window
clock = pygame.time.Clock()  # Creating a var to regulate frame rate
count = [130, 173, 43, 87, 230]  # Variables for spears to fall at different times
moveDown = [False, False, False, False, False]  # "
music = pygame.mixer.music.load('LevelMusic.mp3')   # Music loading in

# Menu variables
bg = pygame.image.load('bg.png').convert()  # Variables loading images for background and options
PG = pygame.image.load('PG.png').convert_alpha()
PG_S = pygame.image.load('PG_S.png').convert_alpha()
HS = pygame.image.load('HS.png').convert_alpha()
HS_S = pygame.image.load('HS_S.png').convert_alpha()
Q = pygame.image.load('Q.png').convert_alpha()
Q_S = pygame.image.load('Q_S.png').convert_alpha()

menuChoice = 1

# Level Variables
score = 0

file = open('HS.txt', 'r')
HighSc = int(file.readline())
file.close()
font = pygame.font.SysFont('Berlin Sans FB', 72)
textsurface = font.render('High Score: ' + str(HighSc), False, (0, 0, 0))
losetext = font.render('Game Over', False, (0, 0, 0))
losetext2 = font.render('You scored ' + str(score) + ' points', False, (0, 0, 0))

# Loading background image
level_bg = pygame.image.load('levelbg.png').convert()
# Sprite images
charRight = [pygame.image.load('R1.png').convert_alpha(), pygame.image.load('R2.png').convert_alpha(),
             pygame.image.load('R3.png').convert_alpha(), pygame.image.load('R4.png').convert_alpha(),
             pygame.image.load('R5.png').convert_alpha(), pygame.image.load('R6.png').convert_alpha(),
             pygame.image.load('R7.png').convert_alpha(), pygame.image.load('R8.png').convert_alpha(),
             pygame.image.load('R9.png').convert_alpha()]
charLeft = [pygame.image.load('L1.png').convert_alpha(), pygame.image.load('L2.png').convert_alpha(),
            pygame.image.load('L3.png').convert_alpha(),pygame.image.load('L4.png').convert_alpha(),
            pygame.image.load('L5.png').convert_alpha(), pygame.image.load('L6.png').convert_alpha(),
            pygame.image.load('L7.png').convert_alpha(), pygame.image.load('L8.png').convert_alpha(),
            pygame.image.load('L9.png').convert_alpha()]

spearD = pygame.image.load('SpearD.png').convert_alpha()

fish1 = pygame.image.load('Fish1.png').convert_alpha()  # Fish objective
fish1 = pygame.transform.scale2x(fish1)  # Scaling fish to be correct size
fish2 = pygame.image.load('Fish2.png').convert_alpha()
fish2 = pygame.transform.scale2x(fish2)


x = 50
y = 380
width = 100
height = 40
vel = 5
left = False
right = True
spriteCount = 0

fish_x = 0
fish_y = 0
whatFish = 1

SX1 = 0
SY1 = -61
SX2 = 0
SY2 = -61
SX3 = 0
SY3 = -61
SX4 = 0
SY4 = -61
SX5 = 0
SY5 = -61

SHeight = 61
SWidth = 14
SVel = 3

gameRun = True
menuRun = True
levelRun = True

def resetgamevars():
    global count, moveDown, fish_x, fish_y, whatFish, SX1, SX2, SX3, SX4, SX5, SY1, SY2, SY3, SY4, SY5, score, x, y, \
        SVel, left, right, spriteCount
    count = [130, 173, 43, 87, 230]  # Variables for spears to fall at different times
    moveDown = [False, False, False, False, False]  # "

    x = 50
    y = 380

    left = False
    right = True
    spriteCount = 0

    fish_x = 0
    fish_y = 0
    whatFish = 1

    SX1 = 0
    SY1 = -61
    SX2 = 0
    SY2 = -61
    SX3 = 0
    SY3 = -61
    SX4 = 0
    SY4 = -61
    SX5 = 0
    SY5 = -61
    SVel = 3

    score = 0


def high_score():
    pygame.draw.rect(win, (70, 200, 250), (0, 0, 1280, 720), 0)
    win.blit(textsurface, (430, 300))
    pygame.display.update()
    pygame.time.delay(5000)


def lose_screen():
    pygame.draw.rect(win, (70, 200, 250), (0, 0, 1280, 720), 0)
    win.blit(losetext, (450, 250))
    win.blit(losetext2, (350, 310))
    pygame.display.update()
    pygame.time.delay(5000)


def randSpearDown(spear):
    global SX1, SX2, SX3, SX4, SX5

    if spear == 1:
        SX1 = random.randint(0, 220)
    if spear == 2:
        SX2 = random.randint(250, 480)
    if spear == 3:
        SX3 = random.randint(500, 700)
    if spear == 4:
        SX4 = random.randint(720, 960)
    if spear == 5:
        SX5 = random.randint(990, 1200)


def randFish():
    global whatFish, fish_x, fish_y
    whatFish = random.randint(1, 2)
    fish_x = random.randint(23, 1257)
    fish_y = random.randint(24, 696)


for i in range(1, 6):
    randSpearDown(i)

randFish()

while gameRun:

    while menuRun:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuRun = False
                gameRun = False
                levelRun = False
        win.blit(bg, (0, 0))

        if menuChoice == 1:
            win.blit(PG, (530, 320))
            win.blit(HS_S, (507, 420))
            win.blit(Q_S, (597, 520))
        if menuChoice == 2:
            win.blit(PG_S, (530, 320))
            win.blit(HS, (507, 420))
            win.blit(Q_S, (597, 520))
        if menuChoice == 3:
            win.blit(PG_S, (530, 320))
            win.blit(HS_S, (507, 420))
            win.blit(Q, (597, 520))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and menuChoice != 1:
            menuChoice -= 1
        if keys[pygame.K_DOWN] and menuChoice != 3:
            menuChoice += 1
        if keys[pygame.K_SPACE] and menuChoice == 1 or keys[pygame.K_RETURN] and menuChoice == 1:
            menuRun = False
            gameRun = True
            pygame.mixer.music.play(-1)
            resetgamevars()
        if keys[pygame.K_SPACE] and menuChoice == 2 or keys[pygame.K_RETURN] and menuChoice == 2:
            textsurface = font.render('High Score: ' + str(HighSc), False, (0, 0, 0))
            high_score()
        if keys[pygame.K_SPACE] and menuChoice == 3 or keys[pygame.K_RETURN] and menuChoice == 3:
            menuRun = False
            levelRun = False
            gameRun = False

        pygame.display.update()

    while levelRun:
        clock.tick(54)

        for i in range(1, 6):
            if count[i-1] >= 300 - (10*SVel):
                moveDown[i-1] = True
                count[i-1] = 0

                if i == 1:
                    SY1 = -61
                    randSpearDown(i)
                if i == 2:
                    SY2 = -61
                    randSpearDown(i)
                if i == 3:
                    SY3 = -61
                    randSpearDown(i)
                if i == 4:
                    SY4 = -61
                    randSpearDown(i)
                if i == 5:
                    SY5 = -61
                    randSpearDown(i)

            count[i-1] += 1

        if moveDown[0]:
            SY1 += SVel
        if moveDown[1]:
            SY2 += SVel
        if moveDown[2]:
            SY3 += SVel
        if moveDown[3]:
            SY4 += SVel
        if moveDown[4]:
            SY5 += SVel

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                levelRun = False
                gameRun = False
                menuRun = False

        win.blit(level_bg, (0, 0))

        if spriteCount + 1 >= 54:
            spriteCount = 0

        if left:
            win.blit(charLeft[spriteCount // 6], (x, y))
            spriteCount += 1
        if right:
            win.blit(charRight[spriteCount // 6], (x, y))
            spriteCount += 1

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > 0:
            x -= vel
            right = False
            left = True
        if keys[pygame.K_RIGHT] and x < 1280 - width:
            x += vel
            right = True
            left = False
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < 720 - height:
            y += vel

        if x < SX1 < x + 100 and y < SY1 < y + 40 or x < SX1 < x + 100 and y < SY1 + 61 < y + 40 or\
                x < SX1 + 14 < x + 100 and y < SY1 < y + 40 or x < SX1 + 14 < x + 100 and y < SY1 + 61 < y + 40:
            levelRun = False
            losetext2 = font.render('You scored ' + str(score) + ' points', False, (0, 0, 0))
            lose_screen()
        if x < SX2 < x + 100 and y < SY2 < y + 40 or x < SX2 < x + 100 and y < SY2 + 61 < y + 40 or\
                x < SX2 + 14 < x + 100 and y < SY2 < y + 40 or x < SX2 + 14 < x + 100 and y < SY2 + 61 < y + 40:
            levelRun = False
            losetext2 = font.render('You scored ' + str(score) + ' points', False, (0, 0, 0))
            lose_screen()
        if x < SX3 < x + 100 and y < SY3 < y + 40 or x < SX3 < x + 100 and y < SY3 + 61 < y + 40 or\
                x < SX3 + 14 < x + 100 and y < SY3 < y + 40 or x < SX3 + 14 < x + 100 and y < SY3 + 61 < y + 40:
            levelRun = False
            losetext2 = font.render('You scored ' + str(score) + ' points', False, (0, 0, 0))
            lose_screen()
        if x < SX4 < x + 100 and y < SY4 < y + 40 or x < SX4 < x + 100 and y < SY4 + 61 < y + 40 or\
                x < SX4 + 14 < x + 100 and y < SY4 < y + 40 or x < SX4 + 14 < x + 100 and y < SY4 + 61 < y + 40:
            levelRun = False
            losetext2 = font.render('You scored ' + str(score) + ' points', False, (0, 0, 0))
            lose_screen()
        if x < SX5 < x + 100 and y < SY5 < y + 40 or x < SX5 < x + 100 and y < SY5 + 61 < y + 40 or\
                x < SX5 + 14 < x + 100 and y < SY5 < y + 40 or x < SX5 + 14 < x + 100 and y < SY5 + 61 < y + 40:
            levelRun = False
            losetext2 = font.render('You scored ' + str(score) + ' points', False, (0, 0, 0))
            lose_screen()

        if x < fish_x < x + 100 and y < fish_y < y + 40 or x < fish_x < x + 100 and y < fish_y + 14 < y + 40 or\
                x < fish_x + 13 < x + 100 and y < fish_y < y + 40 or x < fish_x + 13 < x + 100 and\
                y < fish_y + 14 < y + 40:
            randFish()
            score += 1
            SVel += 1

        if whatFish == 1:
            win.blit(fish1, (fish_x, fish_y))
        if whatFish == 2:
            win.blit(fish2, (fish_x, fish_y))

        win.blit(spearD, (SX1, SY1))
        win.blit(spearD, (SX2, SY2))
        win.blit(spearD, (SX3, SY3))
        win.blit(spearD, (SX4, SY4))
        win.blit(spearD, (SX5, SY5))
        pygame.display.update()

    if score > HighSc:
        HighSc = score
        file = open('HS.txt', 'w')
        file.write(str(score))
        file.close()
    levelRun = True
    menuRun = True

pygame.mixer.music.stop()
pygame.display.quit()
pygame.quit()

