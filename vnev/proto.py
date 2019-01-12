import time
import pygame
import sys
from pygame import gfxdraw as gfx

#test änderrung

hight = 480
widht = 800

windowed = False # notused

if windowed == False:
    window = pygame.FULLSCREEN
else:
    window = 0
pygame.init()
pygame.font.init()


fontComicSans18 = pygame.font.Font('fonts/ComicSans.ttf',28)

pygame.display.set_icon(pygame.image.load('grafiken/Base pack/Tiles/boxExplosive.png'))

fenser = pygame.display.set_caption("Proto")
fenser = pygame.display.set_mode((widht,hight),pygame.NOFRAME)

farbe = 0
f = 0

def zeit():
    zeitNeu = time.asctime()
    textObjekt = pygame.font.Font.render(fontComicSans18,zeitNeu,False,(farbe,farbe,farbe))
    return textObjekt
x = 0
y = 440
bounce = 0
yUp = 0
jump = 0

richtung = ["+","+","+"]
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP and jump <= 1:
                jump += 1
                yUp = -15
                print("jump")
            if event.key == pygame.K_1:
                fenser = pygame.display.set_mode((widht,hight),0)
                pygame.display.set_icon(pygame.image.load('grafiken/Base pack/Tiles/boxExplosive.png'))
            if event.key == pygame.K_2:
                fenser = pygame.display.set_mode((widht,hight),pygame.NOFRAME)
            if event.key == pygame.K_3:
                fenser = pygame.display.set_mode((widht,hight),pygame.FULLSCREEN)

    #print(jump)

    FpsLock = pygame.time.Clock()
    farbe = int(f * (250/500))
    '''
    if x >= 455:
        richtung[0] = "-"
    if x <= 0:
        richtung[0] = "+"
    if y >= 450:
        richtung[1] = "-"
    if y <= 0:
        richtung[1] = "+"

    if richtung[0] == "+":
        x += 2.7
    if richtung[0] == "-":
        x -= 2.3
    if richtung[1] == "+":
        y += 2.4
    if richtung[1] == "-":
        y -= 2.9
    
    if f >= 500:
        richtung[2] = "-"
    if f <= 0:
        richtung[2] = "+"

    if richtung[2] == "+":
        f += 1.7
    if richtung[2] == "-":
        f -= 1.7
    '''
    y = y + yUp
    if yUp < 0:
        yUp = yUp/1.05
    if int(yUp) == -1:
        yUp = yUp * -1
    if yUp >= 1:
        yUp = yUp * 1.05
    if y >= 440 and yUp >= 1 and bounce <= 3:
        bounce += 1
        yUp = yUp * -1 / 2
    if bounce == 4:
        jump = 0
        bounce = 0
        y = 440
        yUp = 0
    #print(yUp)

    gfx.box(fenser,((0,0),(800,480)),(100,100,100))
    fenser.blit(zeit(),(x,y))
    FpsLock.tick(60)
    pygame.display.update()

