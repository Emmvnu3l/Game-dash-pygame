import pygame


from .colors import *
from .config import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((HEIGHT_PLAYER,WIDTH_PLAYER))
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
