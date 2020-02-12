import pygame as pg
from pygame.locals import *
from random import randint

class Nave_explo(pg.sprite.Sprite):
    img_nave = 'bomb-sprite.png'
    speed = 5
    FPS = 60
    vidas = 10
    estado = 'Explo'

    def __init__(self, x = 0, y = 250, w = 128, h = 128):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32)
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
        self.loadFrames()
        

    def loadFrames(self):
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

    def update(self,dt):
        
        self.current_time += dt
        if self.current_time > self.animation_time:
            self.current_time = 0
            self.index += 1
            if self.index >= self.how_many:
                self.index = 0
            self.image = self.frames [self.index]
            
    