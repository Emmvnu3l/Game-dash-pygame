import pygame


from .colors import*
from .config import*

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

    #metodo para que el player no sobrepase la plataforma
    def validation_plataform(self, platform):
        result = pygame.sprite.collide_rect(self,platform)
        if result: 
            self.pos_y = platform.rect.top
            self.vel_y = 0

    def jump(self):
        self.vel_y = -23  

    def update_pos(self):
        self.vel_y += PLAYER_GRAV   # aplicamos gravedad a la velocidad
        self.pos_y += self.vel_y   



             
    def update(self):
        self.update_pos()
        self.rect.bottom = self.pos_y