# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()

# Define some colours
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREENWIDTH = 1440
SCREENHEIGHT = 785
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

class Button():
    """This is a class for a generic button.
    
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(150, 75), font_name="Segoe Print", font_size=40):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GRAY  # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()

def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')

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

def my_music_off_function():
    """A function that retreats to the previous level"""
    global level
    level += 0
    
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
clock = pygame.time.Clock()

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
#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)

    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Draw buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()
    elif level == 2:
        for button in level2_buttons:
            button.draw()
    elif level == 3:
        for button in level3_buttons:
            button.draw()

    if level == 4:
        for button in level4_buttons:
            button.draw()

    if level == 5:
        for button in level5_buttons:
            button.draw()

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()



