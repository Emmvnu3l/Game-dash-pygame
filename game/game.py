import pygame
import sys
import random
import os

from .config import* ## importación de las configuraciónes
from .colors import* ## importación de colores
from .platform import Platform
from .player import Player
from .wall import Wall
from .coin import Coin

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True

        ## creacion de ruta de sonidos
        self.dir = os.path.dirname(__file__)
        self.dir_sounds = os.path.join(self.dir, 'sources','sounds')

        self.font = pygame.font.match_font(FONT)

    def start(self):
        self.new()    
    
    def new(self):
        self.score = 0
        self.level = 0
        self.generate_elements()
        self.run()
    
    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top- 200)

        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        self.generate_walls()
    
    def generate_walls(self):
        last_position = WIDTH + 100 ##variable que otorga rango entre un obstaculo y otro
        if not len(self.walls)>0:
            for w in range (0,MAX_WALLS):
                left = random.randrange(last_position + 200, last_position + 400)
                wall = Wall(left, self.platform.rect.top)
                last_position = wall.rect.right

                self.sprites.add(wall)
                self.walls.add(wall)

            self.level += 1
            self.generate_coins()

    def generate_coins(self):
        last_position = WIDTH + 100
        for c in range (0, MAX_COINS):
            pos_x = random.randrange(last_position + 180, last_position + 300)
            coin = Coin(pos_x, 150)
            last_position = coin.rect.right

            self.sprites.add(coin)
            self.coins.add(coin)


    def run(self):
        while self.running:
            self.events()
            self.draw()
            
            self.update()
            self.clock.tick(FPS)
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
        self.draw_text()
        self.sprites.draw(self.surface) ##Pintar la superficie
    def update(self):
        if self.playing:
            pygame.display.flip() ## flip actualiza todo la superficie
            wall = self.player.collide_with(self.walls)
            if wall:
                if self.player.collide_bottom(wall):
                    self.player.skid(wall)
                else:    
                    self.stop()

            coin = self.player.collide_with(self.coins)
            if coin:
                self.score +=1
                coin.kill()
                sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'coin.mp3'))
                sound.play()
                print(self.score)
            self.sprites.update() ## todos los elementos de las listas ejecutaran su metodo update
            self.player.validation_plataform(self.platform)
            self.update_elements(self.walls)
            self.update_elements(self.coins)
            self.generate_walls()
            ## Metodo para limpiar elementos
    def update_elements(self, elements):
        for element in elements:
            if not element.rect.right > 0:
                element.kill()

    def stop(self):
        sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'lose.mp3'))
        sound.play()
        self.player.stop() 
        self.stop_element(self.walls)
        self.playing = False

    def stop_element(self, elements):
        for element in elements:
            element.stop()

    def score_format(self):
        return 'Score: {}'.format(self.score)
    
    def level_format(self):
        return 'Level: {}'.format(self.level)
    
    def draw_text(self):
        self.display_text(self.score_format(), 36, WHITE, WIDTH // 2, TEXT_POSTY)
        self.display_text(self.level_format(), 36, WHITE, 150, TEXT_POSTY)


    def display_text(self, text, size, color, pos_x, pos_y):
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)

        self.surface.blit(text, rect)
