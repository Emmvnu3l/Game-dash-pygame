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

        ##validación de salto c10
        self.can_jump= False
        self.playing = True
    def collide_with(self, sprites):
        ## jugador, lista de sprite, 
        objects = pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]
        
    def collide_bottom(self, wall):
        return self.rect.colliderect(wall.rect_top)
        
    def skid(self, wall):
        self.pos_y = wall.rect.top
        self.vel_y = 0
        self.can_jump = True
        
    #metodo para que el player no sobrepase la plataforma
    def validation_plataform(self, platform):
        result = pygame.sprite.collide_rect(self,platform)
        if result: 
            self.pos_y = platform.rect.top
            self.vel_y = 0
            self.can_jump = True

    def jump(self):
        if self.can_jump == True:
            self.vel_y = -23
            self.can_jump = False  

    def update_pos(self):
        self.vel_y += PLAYER_GRAV   # aplicamos gravedad a la velocidad
        self.pos_y += self.vel_y  + 0.5 * PLAYER_GRAV 



             
    def update(self):
        if self.playing:
            self.update_pos()
        self.rect.bottom = self.pos_y

    def stop(self):
        self.playing = False

