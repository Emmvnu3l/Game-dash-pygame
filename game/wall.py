import pygame
import os
from .config import *
from .colors import *
class Wall(pygame.sprite.Sprite):

    def __init__(self , left, bottom, dir_images):
        pygame.sprite.Sprite.__init__(self)
        
        # Cargar y escalar primero
        image = pygame.image.load(os.path.join(dir_images, 'wall.png')).convert_alpha()
        self.image = pygame.transform.scale_by(image, 0.25)

        # Ahora sí, el rect tendrá el tamaño correcto
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom 

        self.vel_x = SPEED
        self.rect_top = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 1)

    def update(self):
        self.rect.left -= self.vel_x
        self.rect_top.x = self.rect.x

    def stop(self):
        self.vel_x = 0
