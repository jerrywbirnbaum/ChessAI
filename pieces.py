import pygame
import os

brown = (175, 95, 0)
white = (240, 240, 240)
white = (10, 10, 10)
brown = (77, 38, 38)
tan = (121,72,57)
pygame.init()

class Piece(pygame.sprite.Sprite):
    def __init__(self,x,y,img,gameDisplay):
        self.row = int(y/64)
        self.col = int(x/64)
        if(self.row < 4):
            self.isBlack=True
        else:
            self.isBlack=False
        self.gameDisplay=gameDisplay
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = img
        #self.image.set_colorkey(brown)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.isSelected= False
        self.hasMoved=False
    def select(self):
        self.isSelected=True
    def unselect(self):
        self.isSelected = False
        x,y = pygame.mouse.get_pos()
        x = int(x/64) * 64
        y = int(y/64) * 64
        pos = x,y
        self.row = int(y/64)
        self.col = int(x/64)
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
    def getPeacefulMoves(self,board):
        legalMoves = []
        return legalMoves
    def getCaptureMoves(self,board):
        captureMoves=[]
        return captureMoves


class Pawn(Piece):
    def __init__(self,x,y,img,gameDisplay):
        super().__init__(x,y,img,gameDisplay)
    def print(self):
        print("imma pawn")
    def getPeacefulMoves(self,board):
        legalMoves = []
        if self.isBlack:
            if board[self.row+1][self.col]==0:
                legalMoves.append((self.row+1,self.col))
            if self.hasMoved == False and board[self.row+2][self.col] == 0 and board[self.row+1][self.col]==0:
                legalMoves.append((self.row+2,self.col))
        else:
            if board[self.row-1][self.col]==0:
                legalMoves.append((self.row-1,self.col))
            if self.hasMoved == False and board[self.row-2][self.col] == 0 and board[self.row-1][self.col]==0:
                legalMoves.append((self.row-2,self.col))
        return legalMoves

    def getCaptureMoves(self,board):
        captureMoves=[]
        if self.isBlack:
            if (self.row+1 <8) and (self.col-1>=0) and board[self.row+1][self.col-1] != 0:
                captureMoves.append((self.row+1,self.col-1))
            if (self.row+1 <8) and (self.col+1 <8) and board[self.row+1][self.col+1] != 0:
                captureMoves.append((self.row+1,self.col+1))
        else:
            if (self.row-1  >= 0) and (self.col-1>=0) and board[self.row-1][self.col-1] != 0:
                captureMoves.append((self.row-1,self.col-1))
            if (self.row-1 >= 0) and (self.col+1 <8) and board[self.row-1][self.col+1] != 0:
                captureMoves.append((self.row-1,self.col+1))
        return captureMoves

class Bishop(Piece):
    def __init__(self,x,y,img,gameDisplay):
        super().__init__(x,y,img,gameDisplay)
    def getPeacefulMoves(self,board):
        legalMoves = []
        for i in range(8):
            if (self.row+i < 8 and self.col+i<8) and board[self.row+i][self.col+i] == 0:
                legalMoves.append((self.row+i,self.col+i))
            else:
                break
        for i in range(8):
            if (self.row-i >= 0 and self.col+i<8) and board[self.row-i][self.col+i] == 0:
                legalMoves.append((self.row-i,self.col+i))
            else:
                break
        for i in range(8):
            if (self.row+i < 8 and self.col-i >=0) and board[self.row+i][self.col-i] == 0:
                legalMoves.append((self.row+i,self.col-i))
            else:
                break
        for i in range(8):
            if (self.row-i >=0 and self.col-i>=0) and board[self.row-i][self.col-i] == 0:
                legalMoves.append((self.row-i,self.col-i))
            else:
                break
        return legalMoves
    def getCaptureMoves(self,board):
        captureMoves=[]
        for i in range(8):
            if (self.row+i < 8 and self.col+i<8):
                if(board[self.row+i][self.col+i] != 0) and board[self.row+i][self.col+i].isBlack != self.isBlack:
                    captureMoves.append((self.row+i,self.col+i))
                    break
            else:
                break
        for i in range(8):
            if (self.row-i >= 0 and self.col+i<8):
                if(board[self.row-i][self.col+i] != 0) and board[self.row-i][self.col+i].isBlack != self.isBlack:
                    captureMoves.append((self.row-i,self.col+i))
                    break
            else:
                break
        for i in range(8):
            if (self.row+i < 8 and self.col-i >=0):
                if board[self.row+i][self.col-i] != 0 and board[self.row+i][self.col-i].isBlack != self.isBlack:
                    captureMoves.append((self.row+i,self.col-i))
                    break
            else:
                break
        for i in range(8):
            if (self.row-i >=0 and self.col-i>=0):
                if board[self.row-i][self.col-i] != 0 and board[self.row-i][self.col-i].isBlack != self.isBlack:
                    captureMoves.append((self.row-i,self.col-i))
                    break
            else:
                break
        return captureMoves


class Knight(Piece):
    def __init__(self,x,y,img,gameDisplay):
        super().__init__(x,y,img,gameDisplay)
    def getPeacefulMoves(self,board):
        legalMoves = []
        knightMovesCol = [-2,-2,-1,-1,1,1,2,2]
        knightMovesRow = [-1,1,-2,2,-2,2,-1,1]
        for i in range(8):
            if(self.row+knightMovesRow[i]<8 and self.row+knightMovesRow[i]>=0) and (self.col+knightMovesCol[i]<8 and self.col+knightMovesCol[i]>=0) and board[self.row+knightMovesRow[i]][self.col+knightMovesCol[i]] == 0:
                legalMoves.append((self.row+knightMovesRow[i],self.col+knightMovesCol[i]))
        return legalMoves
    def getCaptureMoves(self,board):
        captureMoves = []
        knightMovesCol = [-2,-2,-1,-1,1,1,2,2]
        knightMovesRow = [-1,1,-2,2,-2,2,-1,1]
        for i in range(8):
            if(self.row+knightMovesRow[i]<8 and self.row+knightMovesRow[i]>=0) and (self.col+knightMovesCol[i]<8 and self.col+knightMovesCol[i]>=0) and board[self.row+knightMovesRow[i]][self.col+knightMovesCol[i]] != 0 and board[self.row+knightMovesRow[i]][self.col+knightMovesCol[i]].isBlack != self.isBlack:
                captureMoves.append((self.row+knightMovesRow[i],self.col+knightMovesCol[i]))
        return captureMoves

class Rook(Piece):
    def __init__(self,x,y,img,gameDisplay):
        super().__init__(x,y,img,gameDisplay)

    def getPeacefulMoves(self,board):
        legalMoves = []
        for i in range(8):
            if (self.row+i < 8) and board[self.row+i][self.col] == 0:
                legalMoves.append((self.row+i,self.col))
            else:
                break
        for i in range(8):
            if (self.row-i >= 0) and board[self.row-i][self.col] == 0:
                legalMoves.append((self.row-i,self.col))
            else:
                break
        for i in range(8):
            if (self.col+i <8) and board[self.row][self.col+i] == 0:
                legalMoves.append((self.row,self.col+i))
            else:
                break
        for i in range(8):
            if (self.col-i>=0) and board[self.row][self.col-i] == 0:
                legalMoves.append((self.row,self.col-i))
            else:
                break
        return legalMoves

    def getCaptureMoves(self,board):
        captureMoves = []
        for i in range(8):
            if (self.row+i < 8) and (board[self.row+i][self.col] != 0) and (board[self.row+i][self.col].isBlack != self.isBlack):
                captureMoves.append((self.row+i,self.col))
                break
        for i in range(8):
            if (self.row-i >= 0) and board[self.row-i][self.col] != 0 and board[self.row-i][self.col].isBlack != self.isBlack:
                captureMoves.append((self.row-i,self.col))
                break
        for i in range(8):
            if (self.col+i <8) and board[self.row][self.col+i] != 0 and board[self.row][self.col+i].isBlack != self.isBlack:
                captureMoves.append((self.row,self.col+i))
                break
        for i in range(8):
            if (self.col-i>=0) and board[self.row][self.col-i] != 0 and board[self.row][self.col-i].isBlack != self.isBlack :
                captureMoves.append((self.row,self.col-i))
                break
        return captureMoves

class Queen(Piece):
    def __init__(self,x,y,img,gameDisplay):
        super().__init__(x,y,img,gameDisplay)
    def getPeacefulMoves(self,board):
        legalMoves = []
        for i in range(8):
            if (self.row+i < 8) and board[self.row+i][self.col] == 0:
                legalMoves.append((self.row+i,self.col))
            else:
                break
        for i in range(8):
            if (self.row-i >= 0) and board[self.row-i][self.col] == 0:
                legalMoves.append((self.row-i,self.col))
            else:
                break
        for i in range(8):
            if (self.col+i <8) and board[self.row][self.col+i] == 0:
                legalMoves.append((self.row,self.col+i))
            else:
                break
        for i in range(8):
            if (self.col-i>=0) and board[self.row][self.col-i] == 0:
                legalMoves.append((self.row,self.col-i))
            else:
                break
        for i in range(8):
            if (self.row+i < 8 and self.col+i<8) and board[self.row+i][self.col+i] == 0:
                legalMoves.append((self.row+i,self.col+i))
            else:
                break
        for i in range(8):
            if (self.row-i >= 0 and self.col+i<8) and board[self.row-i][self.col+i] == 0:
                legalMoves.append((self.row-i,self.col+i))
            else:
                break
        for i in range(8):
            if (self.row+i < 8 and self.col-i >=0) and board[self.row+i][self.col-i] == 0:
                legalMoves.append((self.row+i,self.col-i))
            else:
                break
        for i in range(8):
            if (self.row-i >=0 and self.col-i>=0) and board[self.row-i][self.col-i] == 0:
                legalMoves.append((self.row-i,self.col-i))
            else:
                break
        return legalMoves
    def getCaptureMoves(self,board):
        captureMoves = []
        for i in range(8):
            if (self.row+i < 8) and (board[self.row+i][self.col] != 0) and (board[self.row+i][self.col].isBlack != self.isBlack):
                captureMoves.append((self.row+i,self.col))
                break
        for i in range(8):
            if (self.row-i >= 0) and board[self.row-i][self.col] != 0 and board[self.row-i][self.col].isBlack != self.isBlack:
                captureMoves.append((self.row-i,self.col))
                break
        for i in range(8):
            if (self.col+i <8) and board[self.row][self.col+i] != 0 and board[self.row][self.col+i].isBlack != self.isBlack:
                captureMoves.append((self.row,self.col+i))
                break
        for i in range(8):
            if (self.col-i>=0) and board[self.row][self.col-i] != 0 and board[self.row][self.col-i].isBlack != self.isBlack :
                captureMoves.append((self.row,self.col-i))
                break
        for i in range(8):
            if (self.row+i < 8 and self.col+i<8):
                if(board[self.row+i][self.col+i] != 0) and board[self.row+i][self.col+i].isBlack != self.isBlack:
                    captureMoves.append((self.row+i,self.col+i))
                    break
            else:
                break
        for i in range(8):
            if (self.row-i >= 0 and self.col+i<8):
                if(board[self.row-i][self.col+i] != 0) and board[self.row-i][self.col+i].isBlack != self.isBlack:
                    captureMoves.append((self.row-i,self.col+i))
                    break
            else:
                break
        for i in range(8):
            if (self.row+i < 8 and self.col-i >=0):
                if board[self.row+i][self.col-i] != 0 and board[self.row+i][self.col-i].isBlack != self.isBlack:
                    captureMoves.append((self.row+i,self.col-i))
                    break
            else:
                break
        for i in range(8):
            if (self.row-i >=0 and self.col-i>=0):
                if board[self.row-i][self.col-i] != 0 and board[self.row-i][self.col-i].isBlack != self.isBlack:
                    captureMoves.append((self.row-i,self.col-i))
                    break
            else:
                break
        return captureMoves


class King(Piece):
    def __init__(self,x,y,img,gameDisplay):
        super().__init__(x,y,img,gameDisplay)
    def getPeacefulMoves(self,board):
        legalMoves=[]
        if(self.row+1 < 8) and board[self.row+1][self.col] == 0:
            legalMoves.append((self.row+1,self.col))
        if(self.col+1 < 8) and board[self.row][self.col+1] == 0:
            legalMoves.append((self.row,self.col+1))
        if(self.row-1 >=0) and board[self.row-1][self.col] == 0:
            legalMoves.append((self.row-1,self.col))
        if(self.col-1 >=0) and board[self.row][self.col-1] == 0:
            legalMoves.append((self.row,self.col-1))
        if(self.row+1 < 8)and (self.col+1 <8) and board[self.row+1][self.col+1] == 0:
            legalMoves.append((self.row+1,self.col+1))
        if(self.row+1 < 8)and (self.col-1 >= 0) and board[self.row+1][self.col-1] == 0:
            legalMoves.append((self.row+1,self.col-1))
        if(self.row-1 >= 0)and (self.col+1 <8) and board[self.row-1][self.col+1] == 0:
            legalMoves.append((self.row-1,self.col+1))
        if(self.row-1 >=0)and (self.col-1 >= 0) and board[self.row-1][self.col-1] == 0:
            legalMoves.append((self.row-1,self.col-1))
        return legalMoves
    def getCaptureMoves(self,board):
        captureMoves=[]
        if(self.row+1 < 8) and (board[self.row+1][self.col] != 0) and (board[self.row+1][self.col].isBlack != self.isBlack):
            captureMoves.append((self.row+1,self.col))
        if(self.col+1 < 8) and (board[self.row][self.col+1] != 0) and (board[self.row][self.col+1].isBlack != self.isBlack):
            captureMoves.append((self.row,self.col+1))
        if(self.row-1 >=0) and board[self.row-1][self.col] != 0 and board[self.row-1][self.col].isBlack != self.isBlack:
            captureMoves.append((self.row-1,self.col))
        if(self.col-1 >=0) and board[self.row][self.col-1] != 0 and board[self.row][self.col-1].isBlack != self.isBlack:
            captureMoves.append((self.row,self.col-1))
        if(self.row+1 < 8)and (self.col+1 <8) and board[self.row+1][self.col+1] != 0 and board[self.row+1][self.col+1].isBlack != self.isBlack:
            captureMoves.append((self.row+1,self.col+1))
        if(self.row+1 < 8)and (self.col-1 >= 0) and board[self.row+1][self.col-1] != 0 and board[self.row+1][self.col-1].isBlack != self.isBlack:
            captureMoves.append((self.row+1,self.col-1))
        if(self.row-1 >= 0)and (self.col+1 <8) and board[self.row-1][self.col+1] != 0 and board[self.row-1][self.col+1].isBlack != self.isBlack:
            captureMoves.append((self.row-1,self.col+1))
        if(self.row-1 >=0)and (self.col-1 >= 0) and board[self.row-1][self.col-1] != 0 and board[self.row-1][self.col-1].isBlack != self.isBlack:
            captureMoves.append((self.row-1,self.col-1))
        return captureMoves
