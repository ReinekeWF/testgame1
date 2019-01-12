import sys
import pygame
import random

#constants representing colors
BLACK = (0  , 0  , 0  )
BROWN = (153, 76 , 0  )
GREEN = (0  , 255, 0  )
BLUE  = (0  , 0  , 255)
WHITE = (255, 255, 255)
RED   = (255, 0  , 0  )
GRAY  = (128, 128, 128)

#cloud position
cloudx = -200
cloudy = 0

#constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
ROCK = 5
DIAMOND = 6


CLOUD = 9999

#A dictionary linking resources to colors
colors = {
            DIRT : BROWN,
            GRASS : GREEN,
            WATER : BLUE,
            COAL : BLACK,
            LAVA : RED,
            ROCK : GRAY
}

#A dictionary linking resources to textures
textures = {
            DIRT : pygame.image.load('grafiken/dirt.png'),
            GRASS : pygame.image.load('grafiken/grass.png'),
            WATER : pygame.image.load('grafiken/water.png'),
            COAL : pygame.image.load('grafiken/coal.png'),
            LAVA : pygame.image.load('grafiken/lava.png'),
            ROCK : pygame.image.load('grafiken/rock.png'),
            DIAMOND : pygame.image.load('grafiken/diamond.png'),
            CLOUD : pygame.image.load('grafiken/cloude.png')
}

inventory = {
            DIRT    : 0,
            GRASS   : 0,
            WATER   : 0,
            COAL    : 0,
            ROCK    : 0,
            LAVA    : 0,
            DIAMOND : 0
}


#useful game dimensions
TILESIZE    = 32
MAPWIDTH    = 30
MAPHEIGHT  = 20

#the player image
PLAYER = pygame.image.load("grafiken/player.png")
#the position of the player [x,y]
playerPos = [0,0]

#a list of resources
resources = [DIRT,GRASS,WATER,LAVA,ROCK,COAL,DIAMOND]


#this is a map
'''
tilemap = [
            [GRASS,COAL,DIRT,ROCK,LAVA],
            [WATER,LAVA,LAVA,WATER,GRASS],
            [COAL,GRASS,ROCK,LAVA,WATER],
            [DIRT,GRASS,ROCK,ROCK,COAL],
            [GRASS,WATER,DIRT,ROCK,DIRT]
        ]
'''
#use list comrehension to create our tilemap
tilemap = [[DIRT for w in range(MAPWIDTH)]for h in range(MAPHEIGHT)]

#pygame.mixer.pre_init(22050,-16,4,2048)
pygame.mixer.init()

#pygame.mixer.music.load('sound/Dark Descent.mp3')
pygame.mixer.music.load('sound/song18_new.ogg')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(20)
sound = pygame.mixer.Sound("sound/sound.wav")

#set up the display
pygame.init()
pygame.display.set_caption('Game 1')
pygame.display.set_icon(pygame.image.load('grafiken/rock.png'))
GAMESCREEN = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE+62))

#add a font for our inventory
INVFONT = pygame.font.Font('fonts/ComicSans.ttf',18)

#loop through  each row
for rw in range(MAPHEIGHT):
    #loop through each colum in that row
    for cl in range(MAPWIDTH):
        #pick a random nummber
        randoNumber = random.randint(0,20)
        if randoNumber == 0:
            tile = DIAMOND
        elif randoNumber == 1 or randoNumber == 2:
            tile = COAL
        elif randoNumber >= 3 and randoNumber <= 5:
            tile = WATER
        elif randoNumber >= 6 and randoNumber <= 11:
            tile = GRASS
        elif randoNumber >=12 and randoNumber <= 14:
            tile = ROCK
        elif randoNumber >=15 and randoNumber <= 16:
            tile = LAVA
        else:
            tile = DIRT
        tilemap[rw][cl] = tile
while True:
    FpsLock = pygame.time.Clock()
    #spieler eingaben
    #print('X: ', playerX, 'Y: ', playerY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:

            if (event.key == pygame.K_w or event.key == pygame.K_UP) and playerPos[1] > 0 :
                print("up")
                playerPos[1] -= 1
            if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and playerPos[1] < MAPHEIGHT -1:
                print("down")
                playerPos[1] += 1
            if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and playerPos[0] > 0:
                print("left")
                playerPos[0] -= 1
            if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and playerPos[0] < MAPWIDTH -1:
                print("right")
                playerPos[0] += 1
            if event.key == pygame.K_p:
                sound.play()
            if event.key == pygame.K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] += 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT
                print(inventory)
            if event.key == pygame.K_F1:
                print(pygame.ver)
            #placing dirt
            if event.key == pygame.K_1:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[DIRT] > 0:
                    inventory[DIRT] -=1
                    tilemap[playerPos[1]][playerPos[0]] = DIRT
                    inventory[currentTile] += 1


            if event.key == pygame.K_q:
                exit()
        if event.type == pygame.KEYUP:
                print("stop")
        #print('x: ',playerPos[0],'y: ',playerPos[1])
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            #pygame.draw.rect(GAMESCREEN,colors[tilemap[row][column]],(column * TILESIZE,row * TILESIZE, TILESIZE, TILESIZE))
            GAMESCREEN.blit(textures[tilemap[row][column]],(column * TILESIZE,row * TILESIZE, TILESIZE, TILESIZE))
    #display the player at the correct position
    GAMESCREEN.blit(PLAYER,(playerPos[0] * TILESIZE,playerPos[1] * TILESIZE))
    #'''
    GAMESCREEN.blit(textures[CLOUD].convert_alpha(),(cloudx,cloudy))

    cloudx += 1
    if cloudx > MAPWIDTH*TILESIZE:
        cloudy = random.randint(0,MAPHEIGHT*TILESIZE-64)
        cloudx = -200
    #'''


    #display the inventory, starting 10 pixels in
    placePosition = 10
    for item in resources:
        #add image
        GAMESCREEN.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+15))
        placePosition += 42
    #add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventory[item]),True,WHITE,BLACK)
        GAMESCREEN.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 50

    pygame.display.update()
    FpsLock.tick(25)
