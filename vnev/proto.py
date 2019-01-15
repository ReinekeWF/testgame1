import time
import pygame
import sys
from pygame import gfxdraw as gfx
import random

#test änderrung

hight = 480
widht = 800
moveX = 0
pygame.init()
pygame.font.init()


fontComicSans18 = pygame.font.Font('fonts/ComicSans.ttf', 28)
fontEthopool18 = pygame.font.Font('fonts/ethopool.ttf', 28)

pygame.display.set_icon(pygame.image.load('grafiken/Base pack/Tiles/boxExplosive.png'))

fenser = pygame.display.set_caption("Proto")
fenser = pygame.display.set_mode((widht, hight), pygame.NOFRAME)

farbe = [0,0,0]
backgroundfarbe = [150,150,150]
f = 0

def background(farbe):
    pos = 0
    reduzierung = 0
    for color in range(150,0,-5):
        pos += hight/150*5
        gfx.box(fenser,(0,pos - 17,widht,pos),(farbe[0] + 100 - reduzierung, farbe[1] + 100 - reduzierung, farbe[2] + 100 - reduzierung))
        reduzierung += 5

def speed(geschwindigkeit):
    if geschwindigkeit <-1:
        pygame.draw.rect(fenser, (200, 0, 50), (widht-20, hight, 20, geschwindigkeit*10))
        #gfx.pie(fenser,int(widht/2),int(hight/2),80,0,int(geschwindigkeit-180),(200,0,0))
    else:
        geschwindigkeit = geschwindigkeit * -1
        pygame.draw.rect(fenser, (200, 0, 50), (widht-20, hight, 20, geschwindigkeit*10))
        #gfx.pie(fenser,int(widht/2),int(hight/2),80,0,int(geschwindigkeit-180),(200,0,0))


def zeit():
    zeitNeu = time.asctime()
    textObjekt = pygame.font.Font.render(fontEthopool18,zeitNeu,False,farbe)
    return textObjekt


x = 0
y = 440
yUp = 0
jump = 0
rand = 0

richtung = ["+","+","+"]
while True:

    if rand == 0:
        rand = random.randrange(60,2000)
        jump += 1
        yUp -= random.randrange(5,253,10)
    rand -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_DOWN:
                for colorpos in range(3):
                    farbe[colorpos] = random.randrange(50,250)
            if event.key == pygame.K_b:
                for colorpos in range(3):
                    backgroundfarbe[colorpos] = random.randrange(50,150)
            if event.key == pygame.K_UP and jump <= 1:
                jump += 1
                yUp -= 25
                print("jump")
            if event.key == pygame.K_RIGHT:
                moveX = 15
            if event.key == pygame.K_LEFT:
                moveX = -15
            if event.key == pygame.K_1:
                fenser = pygame.display.set_mode((widht,hight),0)
                pygame.display.set_icon(pygame.image.load('grafiken/Base pack/Tiles/boxExplosive.png'))
            if event.key == pygame.K_2:
                fenser = pygame.display.set_mode((widht,hight),pygame.NOFRAME)
            if event.key == pygame.K_3:
                fenser = pygame.display.set_mode((widht,hight),pygame.FULLSCREEN)

    #print(jump)

    FpsLock = pygame.time.Clock()
    #farbe = int(f * (250/500))
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
    x = x + moveX
    if x < 0:
        x = 0
        moveX = 0
    if x > 430:
        x = 430
        moveX = 0
    if moveX < 0:
        moveX = moveX/1.05
    if moveX > 0:
        moveX = moveX/1.05
    if moveX == 1 or moveX == -1:
        moveX = 0
    if yUp < 0:
        yUp = yUp/1.05
    if int(yUp) == -1:
        yUp = yUp * -1
    if yUp >= 1:
        yUp = yUp * 1.05
    if y >= 440 and yUp >= 1:
        yUp = yUp * -1 / 2
    if yUp > 50:
        yUp = 50
    if yUp < -30:
        yUp = -30
    if (yUp >= -1 and yUp <= 0) or (yUp <= 1 and yUp >=0):
        jump = 0
        y = 440
        yUp = 0
    #print(yUp)

    #gfx.box(fenser,((0,0),(800,480)),(150,150,150))
    background(backgroundfarbe)
    speed(yUp)
    fenser.blit(zeit(),(x,y))
    FpsLock.tick(60)
    pygame.display.update()


    '''
    widerstand = 0.01 #ohm
    einteilung = reverenz / 1024

    spannung1 = messwert1 * einteilung
    spannung2 = messwert2 * einteilung
    
    strom = (spannung1 - spannung2) / widerstand
    '''
