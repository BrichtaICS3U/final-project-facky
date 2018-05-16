# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
import math

from GameClasses import Player
from GameClasses import StaffAOE
from GameClasses import Staff
from GameClasses import Enemy

pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (174, 20, 188)

# Open a new window
# The window is defined as (width, height), measured in pixels

screenW = 1440
screenH = 785

size = (screenW, screenH)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Demon Staff")

# Create lists
spriteList = pygame.sprite.Group ()
ennemiList = pygame.sprite.Group ()
objectList = pygame.sprite.Group ()

# Create the objects
player = Player (GREEN, 50, 50, 100)
player.rect.center = (screenW//2, screenH//2)

badBoi = Enemy (RED, 0, 0, 10, 4)
badBoi.rect.x = 900
badBoi.rect.y = screenH/2

staff = Staff (PURPLE, 0, 0)
staff.rect.x = screenW/3
staff.rect.y = screenH/2

staffAOE = StaffAOE (PURPLE, 400, 400, 400//2)
staffAOE.rect.x = staff.rect.x-170
staffAOE.rect.y = staff.rect.y-160

# Put objects into lists
spriteList.add (player)
spriteList.add (badBoi)
spriteList.add (staff)
spriteList.add (staffAOE)

ennemiList.add (badBoi)

objectList.add (staff)
objectList.add (staffAOE)

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # - Arrow controls
    keys = pygame.key.get_pressed ()
    if keys [pygame.K_a] :
        player.moveLeft (5)
    if keys [pygame.K_d] :
        player.moveRight (5)
    if keys [pygame.K_w] :
        player.moveUp (5)
    if keys [pygame.K_s] :
        player.moveDown (5)

    # --- Game logic goes here
    spriteList.update ()

    # List to know what to check for collision between enemy(ies) and player
    collisionList = pygame.sprite.spritecollide (player, ennemiList , False, pygame.sprite.collide_mask)

    # - Blessing zone to allow player to use magic,
    # Code based off: https://stackoverflow.com/questions/34054248/pygame-circle-and-its-associated-rect-for-collision-detection

    #  Find pos of player and AOE
    x1 = player.rect.x
    y1 = player.rect.y
    x2, y2 = staffAOE.rect.center

    # Find the distance between 
    distance = math.hypot (x1 - x2, y1 - y2)

    # Check if inside AOE
##    if distance < staffAOE.radius :
##        print ("blessed")
    
    # - Does dmg when player toches enemy
    for bad in collisionList :
        player.health -= 1

    # - Ends game when player runs out of health
    if player.health <= 0 :
        carryOn = False
        print("GAME OVER!!!")

    #print (pygame.mouse.get_pressed())

    for enemy in ennemiList :
        enemy.moveToPlayer (player)

    # --- Draw code goes here

    # - Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    spriteList.draw (screen)

    # - Health Bar 
    pygame.draw.rect (screen, BLACK, [5, 5, 210, 60], 10)
    pygame.draw.rect (screen, GREEN, [10, 10, player.health * 2, 50])
    
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
