# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
from ButtonClassWorkingVersion import Button
pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('DemonStaff_TitleTheme.mp3')
pygame.mixer.music.play(-1) #-1 means loops for ever, 0 means play just once)

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
pygame.display.set_caption("Game")

# --- Text elements

# Define text for title of game
fontTitle = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceTitle = fontTitle.render('My Awesome Game!', True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (SCREENWIDTH/2, SCREENHEIGHT/6)   # place the centre of the text

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
    
    if level == 1:
        for button in level1_buttons:
            button.draw()
            
    elif level == 2:
        for button in level2_buttons:
            button.draw()

    elif level == 3:
        for button in level3_buttons:
            button.draw()

    elif level == 4:
        for button in level4_buttons:
            button.draw()

    elif level == 5:
        for button in level5_buttons:
            Bbutton.draw()

    # Text
    screen.blit(textSurfaceTitle, textRectTitle)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()


