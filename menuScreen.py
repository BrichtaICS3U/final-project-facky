# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
from ButtonClass import Button
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
textSurfaceTitle = fontTitle.render('Demon Staff', True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (SCREENWIDTH/2, SCREENHEIGHT/6)   # place the centre of the text

def my_next_function():
    """A function that advances to the next level"""
    global level
    level += 1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level = 1

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def my_settings_function():
    """A function that retreats to the previous level"""
    global level
    level += 2

def my_sound_function():
    """A function that retreats to the previous level"""
    global level
    level += 1

def my_sound_on_function():
    """A function that retreats to the previous level"""
    global level
    level += 0

def my_sound_off_function():
    """A function that retreats to the previous level"""
    global level
    level += 0

def my_music_function():
    """A function that retreats to the previous level"""
    global level
    level += 2

def my_music_on_function():
    """A function that retreats to the previous level"""
    global level
    level += 0
    pygame.mixer.music.play(-1)

def my_music_off_function():
    """A function that retreats to the previous level"""
    global level
    level += 0
    pygame.mixer.music.pause()
    
def my_confirm_function():
    """A function that retreats to the previous level"""
    global level
    level = 3
    
def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

    elif level == 3:
        for button in level3_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

    elif level == 4:
        for button in level4_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

    elif level == 5:
        for button in level5_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

level = 1
carryOn = True

#create button objects
button_01 = Button("Play", (SCREENWIDTH/2, SCREENHEIGHT/3), my_next_function) #level 1
button_02 = Button("Back", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_previous_function) #level 3
button_03 = Button("Quit", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_quit_function, bg=(50, 200, 20)) #level 1
button_04 = Button("Settings", (SCREENWIDTH/2, SCREENHEIGHT/2), my_settings_function, bg=(255, 0, 0)) #level 1
button_05 = Button("Sound", (SCREENWIDTH/2, SCREENHEIGHT/2), my_sound_function, bg=(255, 0, 0)) #level 3
button_06 = Button("Sound On", (SCREENWIDTH/2, SCREENHEIGHT/3), my_sound_on_function, bg=(255, 0, 0)) #level 4
button_07 = Button("Sound Off", (SCREENWIDTH/2, SCREENHEIGHT/2), my_sound_off_function, bg=(255, 0, 0)) #level 4
button_08 = Button("Music", (SCREENWIDTH/2, SCREENHEIGHT/3), my_music_function, bg=(255, 0, 0)) #level 3
button_09 = Button("Music On", (SCREENWIDTH/2, SCREENHEIGHT/3), my_music_on_function, bg=(255, 0, 0)) #level 5
button_10 = Button("Music Off", (SCREENWIDTH/2, SCREENHEIGHT/2), my_music_off_function, bg=(255, 0, 0)) #level 5
button_11 = Button("Confirm", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_confirm_function, bg=(255, 0, 0)) #level 4 and 5

#arrange button groups depending on level
level1_buttons = [button_01, button_03, button_04]
level2_buttons = [button_02, button_03]
level3_buttons = [button_02, button_05, button_08]
level4_buttons = [button_06, button_07, button_11]
level5_buttons = [button_09, button_10, button_11]

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown(level)

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
            button.draw()

    # Text
    screen.blit(textSurfaceTitle, textRectTitle)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()


