import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Object (pygame.sprite.Sprite) :
    def __init__ (self, color, width, height):
        super ().__init__()

        self.image = pygame.Surface ([w, h])
        self.image.fill = (WHITE)
        self.image.set_colorkey (WHITE)

        self.width = width
        self.height = height
        self.color = color

        pygame.draw.rect (self.image, color, [0, 0, w, h])

        self.rect = self.image.get_rect ()
        
