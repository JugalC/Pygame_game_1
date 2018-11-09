import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))  # Setting window size
pygame.display.set_caption('Ocean Adventure')

charRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
charLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.png')
level_bg = pygame.image.load('levelbg.png')

fish1 = pygame.image.load('Fish1.png')
fish1 = pygame.transform.scale2x(fish1)
fish2 = pygame.image.load('Fish2.png')
fish2 = pygame.transform.scale2x(fish2)

clock = pygame.time.Clock()

PG = pygame.image.load('PG.png')
PG_S = pygame.image.load('PG_S.png')
HS = pygame.image.load('HS.png')
HS_S = pygame.image.load('HS_S.png')
Q = pygame.image.load('Q.png')
Q_S = pygame.image.load('Q_S.png')


x = 50
y = 380
width = 100
height = 40
vel = 5
left = False
right = True
spriteCount = 0
menuChoice = 1

runGame = True

runMenu = True
while runMenu:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runMenu = False
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
    if keys[pygame.K_SPACE] and menuChoice == 3 or keys[pygame.K_RETURN] and menuChoice == 3:
        runMenu = False
        runGame = False
    if keys[pygame.K_SPACE] and menuChoice == 3 or keys[pygame.K_RETURN] and menuChoice != 3:
        runMenu = False

    pygame.display.update()


def drawLevel1():
    global spriteCount
    win.blit(level_bg, (0,0))

    if spriteCount + 1 >= 27:
        spriteCount = 0

    if left:
        win.blit(charLeft[spriteCount//3], (x, y))
        spriteCount += 1
    if right:
        win.blit(charRight[spriteCount//3], (x, y))
        spriteCount += 1

    win.blit(fish1, (1000, 346))
    pygame.display.update()


# Main loop
while runGame:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0 :
        x -= vel
        right = False
        left = True
    if keys[pygame.K_RIGHT] and x < 1280 - width :
        x += vel
        right = True
        left = False
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < 720 - height:
        y += vel

    drawLevel1()

pygame.quit()
