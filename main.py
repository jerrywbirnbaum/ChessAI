import pygame
import random
import os
import numpy as np
from pieces import *
from chessBoard import *

def ChessGame():
    dis_width = 512
    dis_height = 512

    white = (240, 240, 240)
    white = (10, 10, 10)
    brown = (77, 38, 38)
    tan = (121,72,57)

    #init pygame
    pygame.init()
    gameDisplay = pygame.display.set_mode((dis_width,dis_height))
    pygame.display.set_caption("Chess")
    clock=pygame.time.Clock()
    gameFolder = os.path.dirname(__file__)
    imgFolder = os.path.join(gameFolder,'img')
    gameDisplay.fill(brown)

    #sprite images
    blackPawnImg=pygame.image.load(os.path.join(imgFolder,'blackpawn.png'))
    whitePawnImg = pygame.image.load((os.path.join(imgFolder,'whitepawn.png')))
    blackBishopImg=pygame.image.load(os.path.join(imgFolder,'blackbishop.png'))
    whiteBishopImg = pygame.image.load((os.path.join(imgFolder,'whitebishop.png')))
    blackKnightImg=pygame.image.load(os.path.join(imgFolder,'blackknight.png'))
    whiteKnightImg = pygame.image.load((os.path.join(imgFolder,'whiteknight.png')))
    blackRookImg=pygame.image.load(os.path.join(imgFolder,'blackrook.png'))
    whiteRookImg = pygame.image.load((os.path.join(imgFolder,'whiterook.png')))
    blackQueenImg=pygame.image.load(os.path.join(imgFolder,'blackqueen.png'))
    whiteQueenImg = pygame.image.load((os.path.join(imgFolder,'whitequeen.png')))
    blackKingImg=pygame.image.load(os.path.join(imgFolder,'blackking.png'))
    whiteKingImg = pygame.image.load((os.path.join(imgFolder,'whiteking.png')))


    #init sprites
    all_sprites = pygame.sprite.Group()
    board= ChessBoard(gameDisplay)

    all_sprites = board.returnSprites()


    #Draw chess board
    increment = dis_width/8
    i=0
    j=0
    while j< dis_height:
        while i< dis_width:
            if (i % (increment*2)==0 and (j % (increment*2)==0)):
                pygame.draw.rect(gameDisplay,tan,pygame.Rect(i,j,increment,increment))
            elif((i%(increment*2) == increment) and (j % (increment*2) == increment)):
                    pygame.draw.rect(gameDisplay,tan,pygame.Rect(i,j,increment,increment))
            i=i+increment
        i=0
        j=j+increment

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                print(event)
            if event.type == pygame.MOUSEBUTTONUP:
                board.mouseClick(pygame.mouse.get_pos())
        pygame.display.update()
        all_sprites.update()
        all_sprites.draw(gameDisplay)
        clock.tick(60)
    pygame.quit()
    quit()

ChessGame()
