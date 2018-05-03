# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
from ButtonClass import Button
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
BLUE = (0, 0, 200)
BRIGHT_BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)


# Open a new window
# The window is defined as (width, height), measured in pixels
SCREENWIDTH = 1440
SCREENHEIGHT = 785
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Button")

# --- Text elements

# Define text for title of game
fontTitle = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceTitle = fontTitle.render('My Awesome Game!', True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (SCREENWIDTH/2, SCREENHEIGHT/3)   # place the centre of the text
textRectTitle.center = (SCREENWIDTH/2, SCREENHEIGHT/3) # place the centre of the text

# Button's font
font = pygame.font.Font ('Comic Sans MS.ttf', 24)

# Play button Text
textFacePlay = font.render ("Play", True, WHITE)
textRectPlay = textFacePlay.get_rect()
textRectPlay.center = (SCREENWIDTH/3, SCREENHEIGHT/2 + 25)

# Options button Text
textFaceOptions = font.render ("Options", True, WHITE)
textRectOptions = textFaceOptions.get_rect()
textRectOptions.center = (SCREENWIDTH*2/3, SCREENHEIGHT/2 + 25)

# Quit button Text
textFaceQuit = font.render ("Quit", True, WHITE)
textRectQuit = textFaceQuit.get_rect()
textRectQuit.center = (SCREENWIDTH/2, SCREENHEIGHT * 2/3 + 25)

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

    # Get mouse location
    mouse = pygame.mouse.get_pos()
    #print(mouse) # Uncomment to see mouse position in shell

    # Check if mouse is pressed
    click = pygame.mouse.get_pressed()
    #print(click) # Uncomment to see mouse buttons clicked in shell
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue shapes to be drawn
    
    # Buttons
    # Play button
##    if SCREENWIDTH/3-50 < mouse[0] < SCREENWIDTH/3+50 and SCREENHEIGHT/2 < mouse[1] < SCREENHEIGHT/2 + 50 and click[0] == 1:
##        pygame.draw.rect(screen, ORANGE, (SCREENWIDTH/3-50, SCREENHEIGHT/2, 100, 50))
##        print('Les go')
##    elif SCREENWIDTH/3-50 < mouse[0] < SCREENWIDTH/3+50 and SCREENHEIGHT/2 < mouse[1] < SCREENHEIGHT/2 + 50:
##        pygame.draw.rect(screen, BRIGHT_GREEN, (SCREENWIDTH/3-50, SCREENHEIGHT/2, 100, 50))
##    else:
##        pygame.draw.rect(screen, GREEN, (SCREENWIDTH/3-50, SCREENHEIGHT/2, 100, 50))
##
##     # Options button
##    if SCREENWIDTH * 2/3 - 50 < mouse[0] < SCREENWIDTH * 2/3 + 50 and SCREENHEIGHT/2 < mouse[1] < SCREENHEIGHT/2 + 50 and click [0] == 1 :
##        pygame.draw.rect(screen, ORANGE, (SCREENWIDTH*2/3-50, SCREENHEIGHT/2, 100, 50))
##        print ("Options")
##    elif SCREENWIDTH * 2/3 - 50 < mouse[0] < SCREENWIDTH * 2/3 + 50 and  SCREENHEIGHT/2 < mouse[1] < SCREENHEIGHT/2 + 50 :
##        pygame.draw.rect (screen, BRIGHT_BLUE, (SCREENWIDTH * 2/3 - 50, SCREENHEIGHT/2, 100, 50))
##    else :
##       pygame.draw.rect (screen, BLUE, (SCREENWIDTH * 2/3 - 50, SCREENHEIGHT/2, 100, 50))
##
##    # Quit button
##    if SCREENWIDTH/2 - 50 < mouse[0] < SCREENWIDTH/2 + 50 and SCREENHEIGHT * 2/3 < mouse[1] < SCREENHEIGHT * 2/3 +50 and click[0] == 1 :
##        pygame.draw.rect (screen, ORANGE, (SCREENWIDTH/2 - 50, SCREENHEIGHT * 2/3, 100, 50))
##        print ("Quit")
##    elif SCREENWIDTH/2 - 50 < mouse[0] < SCREENWIDTH/2 + 50  and SCREENHEIGHT * 2/3 < mouse[1] < SCREENHEIGHT * 2/3 +50 :
##       pygame.draw.rect (screen, BRIGHT_RED, (SCREENWIDTH/2 - 50, SCREENHEIGHT * 2/3, 100, 50))
##    else :
##       pygame.draw.rect (screen, RED, (SCREENWIDTH/2 - 50, SCREENHEIGHT * 2/3, 100, 50))

    if Button.level == 1:
        for Button.button in Button.level1_buttons:
            Button.button.draw()
            
    if Button.level == 2:
        for Button.button in Button.level2_buttons:
            Button.button.draw()

    if Button.level == 3:
        for Button.button in Button.level3_buttons:
            Button.button.draw()

    if Button.level == 4:
        for Button.button in Button.level4_buttons:
            Button.button.draw()

    if Button.level == 5:
        for Button.button in Button.level5_buttons:
            Button.button.draw()

    # Text
    screen.blit(textSurfaceTitle, textRectTitle)
    screen.blit(textFacePlay, textRectPlay)
    screen.blit(textFaceOptions, textRectOptions)
    screen.blit(textFaceQuit, textRectQuit)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()


