import time
import pygame
import sys, os
from pygame import gfxdraw as gfx

#import testinput
#from pygame.locals import *

pygame.init()
height = 480
width = 800
height1 = 1080
width1 = 1920

Fenster = pygame.display.set_mode((width, height),pygame.NOFRAME)#,pygame.FULLSCREEN)
INFONT = pygame.font.Font('C:\Windows\Fonts\comic.ttf',13)
#INFONT = pygame.font.Font('http://reineke.wf/index/font/verdana.ttf',11)

white = (200,200,200)
black = (0,0,0)
dayColor = (200,150,0)
nightColor = (0,50,200)

def background():
    pos = 0
    for backcolor in range(150,0,-2):
        gfx.box(Fenster,(0,pos,800,height/15),(backcolor+100,backcolor+100,backcolor+100))
        pos += height/15
    gfx.line(Fenster ,int(width/2),0,int(width/2),height,(200,0,0))

from weather import Weather, Unit

#time.sleep(5)
weather = Weather(unit=Unit.CELSIUS)

location = weather.lookup_by_location('schluechtern')
forecasts = location.forecast
current = location.condition

#print(current.date)
#print('Temperature: ' + current.temp + '    ' + current.text)
#print()

a = 5
x = 402

background()

text = INFONT.render(current.date,True,black)
Fenster.blit(text,(width / 2 + 5 ,5))

for forecast in forecasts:
    text = INFONT.render(str(forecast.date),True,black)
    Fenster.blit(text,(10, a))
    a += 15

    inhalt = 'Day: ' +forecast.high + ' Night: ' + forecast.low + '    ' + forecast.text
    text = INFONT.render(inhalt,True,black)
    Fenster.blit(text,(10, a))
    a += 32

    x +=40
    gfx.box(Fenster,(x - 40,400, 38, -1 * (10 * int(forecast.high))),dayColor)# Tag
    gfx.box(Fenster,(x - 40,400, 38, (10 * int(forecast.low) * -1 )),nightColor)#
    text = INFONT.render(forecast.high,True,black)
    Fenster.blit(text,(x-25, 300))
    text = INFONT.render(forecast.low,True,black)
    Fenster.blit(text,(x-25, 460))

    #print(forecast.date)
    #print('Day: ' +forecast.high + ' Night: ' + forecast.low + '    ' + forecast.text)
    #print()
gfx.line(Fenster,400,400,800-4,400,(200,0,0))
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
