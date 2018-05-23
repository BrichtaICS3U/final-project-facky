import pygame, math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (174, 20, 188)

#This class represents the player. Derives from the "Sprite" class in pygame
# Code based off of http://www.101computing.net/creating-sprites-using-pygame/

class Char (pygame.sprite.Sprite) :

        def __init__ (self, color, width, height, health) :

                super (). __init__ ()

                # Put in the color (c), x, y, width (w) and height (h) of car
                # Set background color to transparent
                self.image = pygame.Surface ([width, height])
                self.image.fill (WHITE)
                self.image.set_colorkey (WHITE)

                self.width = width
                self.height = height
                self.color = color
                self.health = health

# Used to create the player character
class Player (Char) :

        def __init__ (self, color, width, height, health) :
                super (). __init__ (color, width, height, health)

                #Draw player (rectangle)
                pygame.draw.rect (self.image, color, [0, 0, width, height])

                # Get rectangle object that has dimensions of image
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


# Class to create enemies
class Enemy (Char) :

        def __init__ (self, color, width, height, health, speed) :
                # Call the parent class (Sprite) constructor
                super ().__init__(color, width, height, health)

                # Put in the color (c), x, y, width (w) and height (h) of car
                # Set background color to transparent
                self.speed = speed

                # This loads a image of sprite
                # Mask code from: http://www.101computing.net/pygame-how-tos/
                self.image = pygame.image.load ("DemonStaff-Crawler.png").convert_alpha()
                self.mask = pygame.mask.from_surface (self.image)

                # Get rectangle object that has dimensions of image
                self.rect = self.image.get_rect ()

        # Makes enemy move toward player
        # Code from: https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame
        def moveToPlayer (self, player) :

                dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
                
                dist = math.hypot (dx, dy)

                dx, dy = dx / dist, dy/ dist

                self.rect.x -= dx * self.speed
                self.rect.y -= dy * self.speed
                
# Object super class
class Object (pygame.sprite.Sprite) :
        
        def __init__ (self, color, width, height) :

                super (). __init__ ()

                self.image = pygame.Surface ([width, height])
                self.image.fill (BLACK)
                self.image.set_colorkey (BLACK)

                self.color = color
                self.width = width
                self.height = height
                

# Class of the enchanting zone from staff
class StaffAOE (Object) :

        def __init__ (self, color, width, height, radius):

                super ().__init__(color, width, height)

                self.radius = radius

                # Looks like a circle
                pygame.draw.ellipse (self.image, color, [0, 0, width, height], 10)
                self.rect = self.image.get_rect ()

        def moveWithStaff (self, item) :

                self.rect.x = item.rect.x - 170
                self.rect.y = item.rect.y - 160
                
# Class for the staff itself
class Staff (Object):

    def __init__ (self, color, width, height):
        super().__init__(color, width, height)

        # uses custom sprite image made by Farhan
        self.image = pygame.image.load ("DemonStaff-Staff.png").convert_alpha()

        self.rect = self.image.get_rect ()

    def moveWithPlayer (self, player) :

                self.rect.x = player.rect.x
                self.rect.y = player.rect.y
            
# Super class for projectiles
# Based from : http://programarcadegames.com/python_examples/en/bullets_aimed.py
class Projectile (pygame.sprite.Sprite) :

        # Set the arguments

        def __init__ (self, xStart, yStart, xDest, yDest) :

                super (). __init__ ()

                # Makes a rectangle
                self.image = pygame.Surface ([20, 15])
                self.image.fill (RED)
                
                self.rect = self.image.get_rect ()

                # Set the pos of projectile
                self.rect.x = xStart
                self.rect.y = yStart

                # New variables to save values as floats instead of integers
                self.floating_xPoint = xStart
                self.floating_yPoint = yStart

                # Calculation the angle in radians between the start points
                # and end points. This is the angle the projectile will travel.
                xDiff = xDest - xStart
                yDiff = yDest - yStart
                angle = math.atan2(yDiff, xDiff)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                velocity = 5
                self.xChange = math.cos(angle) * velocity
                self.yChange = math.sin(angle) * velocity


        def update (self) :
                """ Moves the projectile"""
                
                # The floating point x and y hold our more accurate location.
                self.floating_xPoint += self.xChange
                self.floating_yPoint += self.yChange
                
                # The rect.x and rect.y are converted to integers.
                self.rect.x = int(self.floating_xPoint)
                self.rect.y = int(self.floating_yPoint)

# The fireball sprite
class FireBall (Projectile) :

        def __init__ (self, xStart, yStart, xDest, yDest) :

                super().__init__ (xStart, yStart, xDest, yDest)

                # Changes default into fireball sprite
                self.image = pygame.image.load ("Demon Staff - Fireball Frame 1.png").convert_alpha()
                self.mask = pygame.mask.from_surface (self.image)
