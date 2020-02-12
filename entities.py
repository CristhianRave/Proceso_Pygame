import pygame as pg
from pygame.locals import *
import random
from random import choice, randint


class Nave(pg.sprite.Sprite):
    clock = pg.time.Clock()
    img_nave = 'nave.png'
    speed = 5
    FPS = 60
    vidas = 100
    
    
    def __init__(self, x = 0, y = 270):

        self.estado = 'normal'

        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.image = pg.image.load('resources/images/{}'.format(self.img_nave)).convert_alpha()
        self.disfraz_normal= pg.image.load('resources/images/{}'.format(self.img_nave)).convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h
        self.frames = []
        self.index = 0
        self.how_many = 0
        self.animation_time = self.FPS//2     
        self.current_time = 0
        
    def go_up(self):
       self.rect.y = max(0, self.rect.y - self.speed)

    def go_down(self):
       self.rect.y = min(self.rect.y + self.speed, 600-self.w)

    def loadFrames(self): 
        dt = self.clock.tick(self.FPS)
        self.w = 128
        self.h = 128
        self.sprite_sheet = pg.image.load('resources/images/bomb-sprite.png').convert_alpha()
        for fila in range(4):
            y = fila*self.h
            for columna in range (4):
                x = columna * self.w

                img_explo = pg.Surface((self.w, self.h), pg.SRCALPHA).convert_alpha()
                img_explo.blit(self.sprite_sheet, (0, 0), (x, y, self.w, self.h))
                self.frames.append(img_explo)
        self.how_many = len(self.frames)
        self.image = self.frames[self.index]
    

    def comprobar_colision(self,group):
        colisiones = pg.sprite.spritecollide(self,group,True)
        num_candidatos = len(colisiones)
        if num_candidatos > 0:
            self.estado = 'explo'
            self.vidas -= 1         
            print('Quedan', self.vidas, 'vidas')
            return num_candidatos
    

    def update(self,dt):

        if self.estado == 'normal':
            self.image = pg.image.load('resources/images/{}'.format(self.img_nave)).convert_alpha()

        elif self.estado == 'explo':
            self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32)
            self.image = self.loadFrames()
            self.current_time += dt
            if self.current_time > self.animation_time:
                self.current_time = 0
                self.index += 1
                if self.index >= self.how_many:
                    self.index = 0
                self.image = self.frames [self.index]
                




class Asteroide(pg.sprite.Sprite):    
    
    imgs_asteroides =('asteroide_60.png', 'asteroide_200.png', 'satelite.png', 'saturno.png', 'astronauta.png')

    def __init__(self, x = randint(780, 800), y = randint(10,550), w = 0, h = 0, speed = 1, puntuacion = 0):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed  
        self.puntuacion = puntuacion

        
        self.asteroids = []     
        for img in self.imgs_asteroides:
            self.image = pg.image.load('resources/images/{}'.format(img)).convert_alpha()
            self.asteroids.append(self.image)
        self.image = (random.choice(self.asteroids))

        self.rect = self.image.get_rect()   
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h    
       

    def suma_score(self):
        self.puntuacion += 10



    def update(self, dt):
        self.rect.x -= self.speed
        if self.rect.x <= -170:  
                        
            self.kill() 
            del self

        
        