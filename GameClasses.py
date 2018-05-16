import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (174, 20, 188)

#This class represents the player. Derives from the "Sprite" class in pygame
# Code based off of http://www.101computing.net/creating-sprites-using-pygame/
class Player (pygame.sprite.Sprite) :

        def __init__ (self, color, width, height, health) :
                #Call the parent class (Sprite) constructor
                super ().__init__()

                #Put in the color (c), x, y, width (w) and height (h) of car
                #Set background color to transparent
                self.image = pygame.Surface ([width, height])
                self.image.fill (WHITE)
                self.image.set_colorkey (WHITE)

                self.width = width
                self.height = height
                self.color = color
                self.health = health

                #Draw player (rectangle)
                pygame.draw.rect (self.image, color, [0, 0, width, height])

                #This loads a image of player
                #self.image = pygame.image.load ("car.png").convert_alpha()

                #Get rectangle object that has dimensions of image
                self.rect = self.image.get_rect ()

        # Changes position of char
        def moveRight (self, pixels) :
               self.rect.x += pixels

        def moveLeft (self, pixels) :
                self.rect.x -= pixels
                
        def moveUp (self, pixels) :
                self.rect.y -= pixels

        def moveDown (self, pixels) :
                self.rect.y += pixels

# class to create enemies
class Enemy (pygame.sprite.Sprite) :

        def __init__ (self, color, width, height, health) :
                #Call the parent class (Sprite) constructor
                super ().__init__()
                
                # mask code from: http://www.101computing.net/pygame-how-tos/
                self.image = pygame.image.load ("DemonStaff-Crawler.png").convert_alpha()
                self.mask = pygame.mask.from_surface (self.image)

                 #Put in the color (c), x, y, width (w) and height (h) of car
                #Set background color to transparent
                self.width = width
                self.height = height
                self.color = color
                self.health = health

                #Draw car (rectangle)
                pygame.draw.rect (self.image, color, [0, 0, width, height])

                #This loads a image of car
                #self.image = pygame.image.load ("car.png").convert_alpha()

                #Get rectangle object that has dimensions of image
                self.rect = self.image.get_rect ()

# class of the enchanting zone from staff
class StaffAOE (pygame.sprite.Sprite) :

        def __init__ (self, color, width, height, radius):

                super ().__init__()

                self.image = pygame.Surface ([width, height])
                self.image.set_colorkey (BLACK)
                self.width = width
                self.height = height
                self.color = color
                self.radius = radius

                # Looks like a circle
                pygame.draw.ellipse (self.image, color, [0, 0, width, height], 10)
                self.rect = self.image.get_rect ()

                
# class for the staff itself
class Staff (pygame.sprite.Sprite):

    def __init__ (self, color, width, height):
        super().__init__()

        # uses custom sprite image made by Farhan
        self.image = pygame.image.load ("DemonStaff-Staff.png").convert_alpha()
        self.image.set_colorkey (WHITE)

        self.width = width
        self.height = height
        self.color = color

        pygame.draw.rect (self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect ()

# class for projectile 
class Fireball (pygame.sprite.Sprite) :

        def __init__ (self, color, width, height) :
                super (). __init__ ()
                
                self.width = width
                self.height = height
                self.color = color

                pygame.draw.rect (self.image, color, [0, 0, width, height])

                self.rect = self.image.get_rect ()

##        def shoot (self, pixels) :
##                mousePos = pygame.mouse.get_pos()
##                mouseClick = pygame.mouse.get_pressed ()
##                
##                if mouseClick ==
                
                
