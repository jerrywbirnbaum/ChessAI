import pygame
import random
import numpy as np

def ChessGame():
    dis_width = 512
    dis_height = 512

    white = (240, 240, 240)
    black = (10, 10, 10)
    brown = (175, 95, 0)
    tan = (50,50,0)

    pygame.init()
    gameDisplay = pygame.display.set_mode((dis_width,dis_height))
    pygame.display.set_caption("Chess")
    clock=pygame.time.Clock()

    #Draw chess board
    increment = dis_width/8
    i=0
    j=0
    while j< dis_height:
        while i< dis_width:
            if (i % (increment*2)==0 and (j % (increment*2)==0)):
                pygame.draw.rect(gameDisplay,white,pygame.Rect(i,j,increment,increment))
            elif((i%(increment*2) == increment) and (j % (increment*2) == increment)):
                    pygame.draw.rect(gameDisplay,white,pygame.Rect(i,j,increment,increment))
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
        clock.tick(60)
    pygame.quit()
    quit()

ChessGame()
