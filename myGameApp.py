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
YELLOW = (255,255,0)
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
        self.rect.centerx = WIDTH/2 #places image in the centre
        self.rect.bottom = HEIGHT-10 #puts it 10px from the bottom of the screen
        #needs to move side to side so we need speed
        self.speedx = 0
    def update(self):
        #we will keep the default speed of the object to 0 and only alter it with a key press
        #this way we avoid coding for what heppens when the key is released
        if self.rect.left > WIDTH:
            self.rect.right = 0
        #returned a list of key that are down (pressed)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -5
        if keystate[pg.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx #move at the speed set by controls

        #constrain the object within the width of the screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
        #spawns new bullet at centerx of player
        #y will spawn at the top i.e. bottom of the bullet at the top of the player
        bullet = Bullet(self.rect.centerx,self.rect.top)
        #add bullet to all sprites group so that its updated
        all_sprites.add(bullet)
        #add bullet to the bullete sprite group
        bullets.add(bullet) 

class Mob(pg.sprite.Sprite):
    #enemy mobile object which inhereits from spirte
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        #makes enemy spawn randomly at top of screen and start dropping down
        self.rect.x = random.randrange(0, WIDTH - self.rect.width) #appears within limits of the x of the screen
        self.rect.y = random.randrange(-100,-40) # this is off the screen
        self.speedy = random.randrange(1,8)
    def update(self):
        #move downwards
        self.rect.y += self.speedy
        #gets rid of enemy when they get to bottom of screen
        if self.rect.top > HEIGHT +10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40) # this is off the screen
            self.speedy = random.randrange(1,8)

class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        #x and y and respawn positions are based on player's position
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10,20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        #set respawn position of bullete to right infront of player
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    
    def update(self):
        #rect (bullet) move upwards at the speed
        self.rect.y += self.speedy
        #deletes it if it move off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


#initialise coomon pygame objects
pg.init()
pg.mixer.init()

#create window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

#create a sprite group
all_sprites = pg.sprite.Group()
mobs = pg.sprite.Group() #creating another group aids during collision detection
bullets = pg.sprite.Group() #bullets sprite group
#instantiate the player object and add it to sprite group
player = Player()
#spawns mobs
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

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
        #check event for keydown to shoot
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot()
    #update
    all_sprites.update()

    #checks of a bullet hits a mob
        #have to consider a group of bullets and group of mobs
        #using a pygame.sprite.groupcollide() method helps to collide two groups togther
        #setting the last 2 parameters will delete the bullet and the mob which collide with each other
        #notice that this will kill the mobs so there needs to be a way of respawnig them if they get killed
    hits = pg.sprite.groupcollide(mobs,bullets,True,True)
    #check to see if a mob hits the player
    hits = pg.sprite.spritecollide(player,mobs,False) #parameters are objects to check against and group againt
                                                    #FALSE indicates whethere hit items in group should be deleted or not

    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    if hits:
        running = False

    #draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #after drawing anything use flip to display image
    pg.display.flip()

#terminates the game window and closes everything up    
pg.quit()