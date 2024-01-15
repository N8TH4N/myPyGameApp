#imports

import pygame as pg
import random

#parameters
WIDTH,HEIGHT,FPS = (480,600,60)
#60 fps makes it fast and smooth
#define colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#a sprite will be an object which inherits from the built in sprite class
class Player(pg.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        #contrustor
        pg.sprite.Sprite.__init__(self)
        #gives you a surface to draw on
        self.image = pg.Surface((50,40))
        self.image.fill(GREEN)
        #useful for moving, size, position and collision
        self.rect = self.image.get_rect() #looks at the image and gets its rect
        self.rect.center = (WIDTH/2,HEIGHT/2) #places image in the centre
        self.rect.bottom = HEIGHT-10 #puts it 10px from the bottom of the screen
        #needs to move side to side so we need speed
        self.speedx = 0
    def update(self):
        #move the sprite at a speed set by controls
        self.rect.x += self.speedx
        #to ensure it does not run off screen
        if self.rect.left > WIDTH:
            self.rect.right = 0

#initialise coomon pygame objects
pg.init()
pg.mixer.init()

#create window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

#create a sprite group
all_sprites = pg.sprite.Group()
#instantiate the player object and add it to sprite group
player = Player()
all_sprites.add(player)

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