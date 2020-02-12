import pygame as pg
from pygame.locals import *
import sys
from entities import *
from random import randint
#from main_explo import *

FPS = 60

class Game:
    clock = pg.time.Clock()
    

    def __init__(self):
      
        self.screen = pg.display.set_mode((800,600))
        pg.display.set_caption ('Spaceships')
        self.background_image = pg.image.load('resources/images/fondo.png').convert()

        self.player = Nave()

        self.font = pg.font.Font('resources/fonts/PressStart.ttf', 22)
        
        #self.player_explo = Nave_explo()
        self.asteroide = Asteroide()

        self.asteroidesGroup = pg.sprite.Group()
        self.naveGroup = pg.sprite.Group()

        self.asteroidesGroup.add(self.asteroide)
        self.naveGroup.add(self.player)
        #self.naveGroup.add(self.player_explo)


        self.asteroides_en_pantalla = 15
        self.new_asteroide = FPS*8
        self.crear_asteroid = FPS*6

 
    def crear_asteroides(self, dt):       
        self.new_asteroide += dt
        if  self.new_asteroide >= self.crear_asteroid:
            self.asteroide = Asteroide(randint(780, 840), randint(10, 550))
            self.asteroide.speed = (randint(1, 2))
            self.asteroidesGroup.add(self.asteroide)
            self.new_asteroide = 0 

    def text(self):
        self.marcador_vidas = self.font.render('Vidas:', True, (255,255,255))
        self.marcador_vidas_num = self.font.render(str(self.player.vidas), True, (255,255,255))
        self.marcador_score_num = self.font.render(str(self.asteroide.puntuacion), True, (255,255,255))


    def gameOver(self):
        if self.player.vidas == 0:
            pg.quit()
            sys.exit()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.player.go_up()

                if event.key == K_DOWN:
                    self.player.go_down()

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_UP]:
            self.player.go_up()
        if keys_pressed[K_DOWN]:
            self.player.go_down()

    def renderiza(self,dt):

        self.screen.blit( self.background_image, (0,0))
        self.asteroidesGroup.update(dt)
        self.naveGroup.update(dt)
    
        self.asteroidesGroup.draw(self.screen)
        self.naveGroup.draw(self.screen)

        self.screen.blit(self.marcador_vidas,(10, 10))
        self.screen.blit(self.marcador_vidas_num,(140, 10))
        self.screen.blit(self.marcador_score_num,(290, 10))
        

    def mainloop(self):
        while True:

            dt = self.clock.tick(FPS)
            self.handleEvents()
            self.text()
            self.gameOver()

            self.player.comprobar_colision(self.asteroidesGroup)

            cant_asteroides_creados = len(self.asteroidesGroup)
            if cant_asteroides_creados < self.asteroides_en_pantalla:
                self.crear_asteroides(dt)

            self.renderiza(dt)
            pg.display.flip()


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.mainloop()