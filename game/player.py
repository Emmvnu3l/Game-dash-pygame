import pygame


from .colors import *
from .config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((HEIGHT_PLAYER,WIDTH_PLAYER))
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
        self.pos_y = self.rect.bottom
        self.vel_y = 0
    def update_pos(self):
        self.vel_y += PLAYER_GRAV   # aplicamos gravedad a la velocidad
        self.pos_y += self.vel_y   
        if self.pos_y >= HEIGHT - 40:  
            self.pos_y = HEIGHT - 40
            self.vel_y = 0
             
    def update(self):
        self.update_pos()
        self.rect.bottom = self.pos_y