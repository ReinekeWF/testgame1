import pygame
from pygame import gfxdraw as gfx
import time
import sys
import random


pygame.init()
xmax = 800
ymax = 600

fenster = pygame.display.set_mode((xmax,ymax))
FpsLock = pygame.time.Clock()

werkzeug = 0
end = (0,0)
start = (400,300)
color = (random.randrange(50,250,10),random.randrange(50,250,10),random.randrange(50,250,10))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                print(pygame.ver)
                key = pygame.ver

            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_e:
                #color = (random.randrange(50,250,10),random.randrange(50,250,10),random.randrange(50,250,10))
                pygame.draw.rect(fenster,(0,0,0),(0,0,xmax,ymax))
                pygame.display.flip()
            if event.key == pygame.K_w:
                color = (random.randrange(50,250,10),random.randrange(50,250,10),random.randrange(50,250,10))
            if event.key == pygame.K_t:
                gfx.box(fenster,(20,20,40,40),color)
                gfx.pie(fenster,80,80,30,20,340,color)

            if event.key == pygame.K_0:
                werkzeug = 0
            if event.key == pygame.K_1:
                werkzeug = 1
            if event.key == pygame.K_2:
                werkzeug = 2
            if event.key == pygame.K_3:
                werkzeug = 3

        if event.type == pygame.KEYUP:
                print("stop")
    x = 0
    for event in pygame.mouse.get_pressed():
        if x == 0 and event == 1:
            start = pygame.mouse.get_pos()
        if x == 1 and event == 1:
            end = pygame.mouse.get_pos()
        if x == 2 and event == 1:
            color = (random.randrange(50,250,10),random.randrange(50,250,10),random.randrange(50,250,10))
        x += 1

    if werkzeug == 0:
        pygame.draw.line(fenster,color,start,pygame.mouse.get_pos())
    if werkzeug == 1:
        gfx.box(fenster,(start,end),color)
    if werkzeug == 2:
        werte = start + end
        gfx.ellipse(fenster,werte[0],werte[1],werte[2],werte[3],color)
    if werkzeug == 3:
        pygame.draw.line(fenster,color,start,end)



    pygame.display.update()
    #print(pygame.mouse.get_pos())
