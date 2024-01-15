#imports

import pygame as pg
import random

#parameters
WIDTH,HEIGHT,FPS = (800,600,30)

#define colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#a sprite will be an object which inherits from the built in sprite class
class Player(pg.sprite.Sprite):
    #sprite for the player

#initialise coomon pygame objects
pg.init()
pg.mixer.init()

#create window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

#create a sprite group
all_sprites = pg.sprite.Group()
#Game loop
running = True
while running:
    #keep the game running at the right speed
    clock.tick(FPS)
    #process input (events)
    #this closes the game when the user quits
    #pygame keeps track of all events in event loop
    for event in pg.event.get():
        #checks event for closing the window/game
        if event.type == pg.QUIT:
            running = False
    #update
    all_sprites.update()
    #draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #after drawing anything use flip to display image
    pg.display.flip()

#terminates the game window and closes everything up    
pg.quit()