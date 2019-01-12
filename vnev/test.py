import pygame
import time
import sys


pygame.init()
pygame.font.init()

def keys():
    key = ""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:

            if (event.key == pygame.K_w or event.key == pygame.K_UP):
                print("up")
                key = "Up"
            if (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                print("down")
                key = "Down"
            if (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                print("left")
                key = "Left"
            if (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                print("right")
                key = "Right"
            if event.key == pygame.K_p:
                print("p")
                key = "p"
                #sound.play()
            if event.key == pygame.K_SPACE:
                print("space")
                key = "space"

            if event.key == pygame.K_F1:
                print(pygame.ver)
                key = pygame.ver

            if event.key == pygame.K_q:
                exit()
        if event.type == pygame.KEYUP:
                print("stop")
    return key

font = pygame.font.Font('fonts/ComicSans.ttf',18)
FENSTER = pygame.display.set_caption("Platformer 001")
pygame.display.set_icon(pygame.image.load('grafiken/Base pack/Player/p3_stand.png'))
FENSTER = pygame.display.set_mode((800,600))

#while True:
    #FpsLock = pygame.time.Clock()
    #textObj = font.render(keys(),True,(255,255,255),(0,0,0))
    #FENSTER.blit(textObj,(20,20))
    #pygame.display.update()
    #FpsLock.tick(25)
