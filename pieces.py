import pygame
import os

brown = (175, 95, 0)
white = (240, 240, 240)
white = (10, 10, 10)
brown = (77, 38, 38)
tan = (121,72,57)
pygame.init()

class Pawn(pygame.sprite.Sprite):
    def __init__(self,x,y,img,gameDisplay):
        self.gameDisplay=gameDisplay
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = img
        self.image.set_colorkey(brown)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.isSelected= False
    def select(self):
        self.isSelected=True
    def unselect(self):
        self.isSelected = False
        x,y = pygame.mouse.get_pos()
        x = int(x/64) * 64
        y = int(y/64) * 64
        pos = x,y
        self.rect.topleft = pos
    def update(self):
        pos = pygame.mouse.get_pos()
        dis_width=512
        dis_height=512
        increment = dis_width/8
        i=0
        j=0
        self.gameDisplay.fill(brown)
        while j< dis_height:
            while i< dis_width:
                if (i % (increment*2)==0 and (j % (increment*2)==0)):
                    pygame.draw.rect(self.gameDisplay,tan,pygame.Rect(i,j,increment,increment))
                elif((i%(increment*2) == increment) and (j % (increment*2) == increment)):
                        pygame.draw.rect(self.gameDisplay,tan,pygame.Rect(i,j,increment,increment))
                i=i+increment
            i=0
            j=j+increment

        crashed = False
        if(self.isSelected):
            self.rect.center = pos

class Bishop(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = img
        self.image.set_colorkey(brown)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Knight(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = img
        self.image.set_colorkey(brown)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Rook(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = img
        self.image.set_colorkey(brown)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Queen(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = img
        self.image.set_colorkey(brown)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class King(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = img
        self.image.set_colorkey(brown)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
