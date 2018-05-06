import pygame

GREEN = (0, 255, 0)

#This class represents a car. Derives from the "Sprite" class in pygame
class Char (pygame.sprite.Sprite) :

        def __init__ (self, c, w, h, health) :
                #Call the parent class (Sprite) constructor
                super ().__init__()

                #Put in the color (c), x, y, width (w) and height (h) of car
                #Set background color to transparent
                self.image = pygame.Surface ([w, h])
                self.image.fill (GREEN)
                self.image.set_colorkey (GREEN)

                self.width = w
                self.height = h
                self.color = c
                self.health = health

                #Draw car (rectangle)
                pygame.draw.rect (self.image, c, [0, 0, w, h])

                #This loads a image of car
                #self.image = pygame.image.load ("car.png").convert_alpha()

                #Get rectangle object that has dimensions of image
                self.rect = self.image.get_rect ()
        
        def moveRight (self, pixels) :
               self.rect.x += pixels

        def moveLeft (self, pixels) :
                self.rect.x -= pixels
                
        def moveUp (self, pixels) :
                self.rect.y -= pixels

        def moveDown (self, pixels) :
                self.rect.y += pixels

                

                
