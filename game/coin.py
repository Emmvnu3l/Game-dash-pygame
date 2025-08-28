import pygame
import os

from .colors import *
from .config import *

class Coin(pygame.sprite.Sprite):

    ## agregamos un nuevo atributo 'dir_images'
    def __init__(self, pos_x, pos_y, dir_images):

        pygame.sprite.Sprite.__init__(self)
        ## cambiamos el atributo flip por una importacion de la imagen
        image= pygame.image.load(os.path.join(dir_images, 'coin.png')).convert_alpha()
        self.image = pygame.transform.scale_by(image, 0.08)

        self.rect = self.image.get_rect()

        self.rect.x = pos_x
        self.rect.y = pos_y
        self.vel_x = SPEED

    def update(self):
        self.rect.left -= self.vel_x

    def stop(self):
        self.vel_x = 0