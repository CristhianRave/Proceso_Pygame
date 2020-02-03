import pygame as pg
from pygame.locals import *

FPS = 60

class Nave(pg.sprite.Sprite):
    img_nave = 'nave.png'
    speed = 10

    def __init__(self, x = 0, y = 270):

        self.x = x
        self.y = y

        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('resources/images/{}'.format(self.img_nave)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h


    def go_up(self):
       self.rect.y = max(0, self.rect.y - self.speed)

    def go_down(self):
       self.rect.y = min(self.rect.y + self.speed, 600-self.w)



class Asteroide(pg.sprite.Sprite):
    speed = 10
    imgs_asteroides ='asteroide_60.png', 'asteroide_100.png', 'asteroide_200.png'
    w = 44
    h = 42


    def __init__(self, x = 0, y = 0):

        self.x = x
        self.y = y

        pg.sprite.Sprite.__init__(self)

        self.rect = Rect(self.x, self.y, self.w, self.h)

        self.imagenes = []
        for i in self.imgs_asteroides:
            imagen = pg.image.load('resources/images/{}'.format(i)).convert_alpha()
            self.imagenes.append(imagen)

       
        self.num_frames = len(self.imagenes)

        self.current_time = 0
        self.animation_time = FPS//60

    @property
    def image(self): 
        return self.imagenes[2]


    @property
    def position(self):
        return self.x, self.y
