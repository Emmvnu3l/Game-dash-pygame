import pygame
import sys


from .config import* ## importación de las configuraciónes
from .colors import* ## importación de colores
from .platform import Platform
from .player import Player
from .wall import Wall

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        
        self.running = True

    def start(self):
        self.new()    
    
    def new(self):
        self.generate_elements()
        self.run()
    
    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top- 200)
        self.wall = Wall(500, self.platform.rect.top)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        self.sprites.add(self.wall)

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()
    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.jump()
                            
    def draw(self):
        self.surface.fill(LIGHT_BLUE) 
        self.sprites.draw(self.surface) ##Pintar la superficie
    def update(self):
        pygame.display.flip() ## flip actualiza todo la superficie
        self.sprites.update() ## todos los elementos de las listas ejecutaran su metodo update
        self.player.validation_plataform(self.platform)
    def stop(self):
        pass

