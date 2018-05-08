# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
from GameClasses import Char
from ObjectClass import Object
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
pygame.display.set_caption("My Game")

spriteList = pygame.sprite.Group ()

player = Char (RED, 20, 30, 100)
player.rect.x = screenW/2
player.rect.y = screenH/2

spriteList.add (player)

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

        keys = pygame.key.get_pressed ()
        if keys [pygame.K_LEFT] :
            player.moveLeft (5)
        if keys [pygame.K_RIGHT] :
            player.moveRight (5)
        if keys [pygame.K_UP] :
            player.moveUp (5)
        if keys [pygame.K_DOWN] :
            player.moveDown (5)

    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    spriteList.draw (screen)
    

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
