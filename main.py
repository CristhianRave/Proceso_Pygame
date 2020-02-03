import pygame as pg
from pygame.locals import *
import sys
from entities import *
from random import randint

FPS = 60


class Game:
    clock = pg.time.Clock()


    def __init__(self):
        self.screen = pg.display.set_mode((800,600))
        pg.display.set_caption ('Spaceships')

        self.background_image = pg.image.load('resources/images/fondo.png').convert()
        self.player = Nave()
        self.asteroides = Asteroide()

        self.allSprites = pg.sprite.Group()

        self.allSprites.add(self.player)
        self.allSprites.add(self.asteroides)

        self.asteroide = []
        for i in range(10):
            ast = Asteroide(randint(0, 750), randint(0, 550))
            self.asteroide.append(ast)     

    def gameOver(self):
        pg.quit()
        sys.exit()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.gameOver()

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


    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS)

            self.handleEvents()

            self.screen.blit( self.background_image, (0,0))
            
            for i in self.asteroide:
                self.screen.blit(i.image, i.position)


            self.allSprites.update(dt)
            self.allSprites.draw(self.screen)
            

            pg.display.flip()




if __name__ == '__main__':
    pg.init()
    game = Game()
    game.mainloop()




