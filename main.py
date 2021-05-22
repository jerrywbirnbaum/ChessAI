import pygame
import random
import os
import numpy as np
from pieces import *

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
    gameDisplay.fill(brown)

    #init sprites
    all_sprites = pygame.sprite.Group()
    pawna7=Pawn(0,64,blackPawnImg)
    pawnb7=Pawn(64,64,blackPawnImg)
    pawnc7=Pawn(128,64,blackPawnImg)
    pawnd7=Pawn(192,64,blackPawnImg)
    pawne7=Pawn(256,64,blackPawnImg)
    pawnf7=Pawn(320,64,blackPawnImg)
    pawng7=Pawn(384,64,blackPawnImg)
    pawnh7=Pawn(448,64,blackPawnImg)

    pawna2=Pawn(0,384,whitePawnImg)
    pawnb2=Pawn(64,384,whitePawnImg)
    pawnc2=Pawn(128,384,whitePawnImg)
    pawnd2=Pawn(192,384,whitePawnImg)
    pawne2=Pawn(256,384,whitePawnImg)
    pawnf2=Pawn(320,384,whitePawnImg)
    pawng2=Pawn(384,384,whitePawnImg)
    pawnh2=Pawn(448,384,whitePawnImg)

    bishopc8=Bishop(128,0,blackBishopImg)
    bishopf8=Bishop(320,0,blackBishopImg)
    bishopc1=Bishop(128,448,whiteBishopImg)
    bishopf1=Bishop(320,448,whiteBishopImg)

    knightb8=Knight(64,0,blackKnightImg)
    knightg8=Knight(384,0,blackKnightImg)
    knightb1=Knight(64,448,whiteKnightImg)
    knightg1=Knight(384,448,whiteKnightImg)

    rooka8=Rook(0,0,blackRookImg)
    rookh8=Rook(448,0,blackRookImg)
    rooka1=Rook(0,448,whiteRookImg)
    rookh1=Rook(448,448,whiteRookImg)

    blackqueen=Queen(192,0,blackQueenImg)
    whitequeen=Queen(192,448,whiteQueenImg)
    blackking=King(256,0,blackKingImg)
    whiteking=King(256,448,whiteKingImg)


    all_sprites.add(pawna7,pawnb7,pawnc7,pawnd7,pawne7,pawnf7,pawng7,pawnh7)
    all_sprites.add(pawna2,pawnb2,pawnc2,pawnd2,pawne2,pawnf2,pawng2,pawnh2)
    all_sprites.add(bishopc8,bishopf8,bishopc1,bishopf1)
    all_sprites.add(knightb1,knightb8,knightg1,knightg8,rooka1,rooka8,rookh1,rookh8,blackqueen,whitequeen,blackking,whiteking)

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
        pygame.display.update()
        pawne2.select()
        all_sprites.update()
        all_sprites.draw(gameDisplay)
        clock.tick(60)
    pygame.quit()
    quit()

ChessGame()
