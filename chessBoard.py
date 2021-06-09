from pieces import *

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

class ChessBoard ():
    def __init__(self,gameDisplay):
        self.gameDisplay=gameDisplay
        self.all_sprites = pygame.sprite.Group()
        self.board=[[0 for i in range(8)]for j in range(8)]

        #init pieces
        self.board[1][0]=Pawn(0,64,blackPawnImg,self.gameDisplay)
        self.board[1][1]=Pawn(64,64,blackPawnImg,self.gameDisplay)
        self.board[1][2]=Pawn(128,64,blackPawnImg,self.gameDisplay)
        self.board[1][3]=Pawn(192,64,blackPawnImg,self.gameDisplay)
        self.board[1][4]=Pawn(256,64,blackPawnImg,self.gameDisplay)
        self.board[1][5]=Pawn(320,64,blackPawnImg,self.gameDisplay)
        self.board[1][6]=Pawn(384,64,blackPawnImg,self.gameDisplay)
        self.board[1][7]=Pawn(448,64,blackPawnImg,self.gameDisplay)

        self.board[6][0]=Pawn(0,384,whitePawnImg,self.gameDisplay)
        self.board[6][1]=Pawn(64,384,whitePawnImg,self.gameDisplay)
        self.board[6][2]=Pawn(128,384,whitePawnImg,self.gameDisplay)
        self.board[6][3]=Pawn(192,384,whitePawnImg,self.gameDisplay)
        self.board[6][4]=Pawn(256,384,whitePawnImg,self.gameDisplay)
        self.board[6][5]=Pawn(320,384,whitePawnImg,self.gameDisplay)
        self.board[6][6]=Pawn(384,384,whitePawnImg,self.gameDisplay)
        self.board[6][7]=Pawn(448,384,whitePawnImg,self.gameDisplay)

        self.board[0][2]=Bishop(128,0,blackBishopImg,self.gameDisplay)
        self.board[0][5]=Bishop(320,0,blackBishopImg,self.gameDisplay)
        self.board[7][2]=Bishop(128,448,whiteBishopImg,self.gameDisplay)
        self.board[7][5]=Bishop(320,448,whiteBishopImg,self.gameDisplay)

        self.board[0][1]=Knight(64,0,blackKnightImg,self.gameDisplay)
        self.board[0][6]=Knight(384,0,blackKnightImg,self.gameDisplay)
        self.board[7][1]=Knight(64,448,whiteKnightImg,self.gameDisplay)
        self.board[7][6]=Knight(384,448,whiteKnightImg,self.gameDisplay)

        self.board[0][0]=Rook(0,0,blackRookImg,self.gameDisplay)
        self.board[0][7]=Rook(448,0,blackRookImg,self.gameDisplay)
        self.board[7][0]=Rook(0,448,whiteRookImg,self.gameDisplay)
        self.board[7][7]=Rook(448,448,whiteRookImg,self.gameDisplay)

        self.board[0][3]=Queen(192,0,blackQueenImg,self.gameDisplay)
        self.board[7][3]=Queen(192,448,whiteQueenImg,self.gameDisplay)
        self.board[0][4]=King(256,0,blackKingImg,self.gameDisplay)
        self.board[7][4]=King(256,448,whiteKingImg,self.gameDisplay)
        self.isPieceSelected = False
        self.pieceCaptured=False

        self.tempBoard=self.board

        for i in range(8):
            for j in range(8):
                if(self.board[i][j] != 0):
                    self.all_sprites.add(self.board[i][j])
    def checkLegalMove(self):
        if (self.endPosRow,self.endPosCol) in (self.pieceSelected.getPeacefulMoves(self.board)):
            return True
        return False
    def checkCapture(self):
        if (self.endPosRow,self.endPosCol) in (self.pieceSelected.getCaptureMoves(self.board)):
            self.pieceCaptured=True
            self.whichPieceCaptured=self.board[self.endPosRow][self.endPosCol]
            #self.board[self.endPosRow][self.endPosCol].kill()
            #self.tempBoard[self.endPosRow][self.endPosCol] = self.pieceSelected
            return True
        return False
    def mouseClick(self,pos):
        if not self.isPieceSelected:
            x,y = pos
            col = int(x/64)
            row = int(y/64)
            self.startPosRow = row
            self.startPosCol = col
            if self.board[row][col] != 0:
                self.board[row][col].select()
                self.pieceSelected=self.board[row][col]
                self.board[row][col] = 0
                self.isPieceSelected = True
        else:
            x,y = pos
            col = int(x/64)
            row = int(y/64)
            self.endPosRow =row
            self.endPosCol = col
            while(True):
                if self.checkLegalMove():
                    self.tempBoard[row][col]=self.pieceSelected
                elif self.checkCapture():
                    self.tempBoard[row][col]=self.pieceSelected
                if not self.whiteKingInCheck(self.tempBoard):
                    if self.pieceCaptured:
                        self.whichPieceCaptured.kill()
                    self.board=self.tempBoard
                    self.pieceSelected.hasMoved = True
                    self.pieceSelected.unselect()
                    self.pieceSelected = 0
                    self.isPieceSelected = False
                    break
                else:
                    self.tempBoard=self.board
    def returnBoard(self):
        return self.board
    def returnSprites(self):
        return self.all_sprites

    def whiteKingInCheck(self,board):
        KingInstance=King(0,0,whiteKingImg,0)
        PawnInstance = Pawn(0,0,whitePawnImg,0)
        KnightInstance = Knight(0,0,whitePawnImg,0)
        BishopInstance = Bishop(0,0,whitePawnImg,0)
        QueenInstance = Queen(0,0,whitePawnImg,0)
        RookInstance = Rook(0,0,whitePawnImg,0)

        #locate white king
        for i in range(8):
            for j in range(8):
                if type(board[i][j]) == type(KingInstance) and not board[i][j].isBlack:
                    kingRow=i
                    kingCol=j
                    break
        #check pawn checks
        if(kingRow-1 >= 0) and (kingCol-1 >= 0) and type(board[kingRow-1][kingCol-1]) == type(PawnInstance) and board[kingRow-1][kingCol-1].isBlack:
            return True
        elif (kingRow-1 >= 0) and (kingCol+1 < 8) and type(board[kingRow-1][kingCol+1]) == type(PawnInstance) and board[kingRow-1][kingCol+1].isBlack:
            return True
        #check knight checks
        knightMovesCol = [-2,-2,-1,-1,1,1,2,2]
        knightMovesRow = [-1,1,-2,2,-2,2,-1,1]
        for i in range(8):
            if(kingRow+knightMovesRow[i]<8 and kingRow+knightMovesRow[i]>=0) and (kingCol+knightMovesCol[i]<8 and kingCol+knightMovesCol[i]>=0) and type(board[kingRow+knightMovesRow[i]][kingCol+knightMovesCol[i]]) == type(KnightInstance) and board[kingRow+knightMovesRow[i]][kingCol+knightMovesCol[i]].isBlack:
                return True
        #check diagonal checks
        for i in range(1,8):
            if (kingRow+i < 8 and kingCol+i<8) and board[kingRow+i][kingCol+i] != 0:
                if not board[kingRow+i][kingCol+i].isBlack:
                    break
                elif (type(board[kingRow+i][kingCol+i])==type(BishopInstance) or type(board[kingRow+i][kingCol+i])==type(QueenInstance)):
                    return True
                else:
                    break
        for i in range(1,8):
            if (kingRow-i >= 0 and kingCol+i<8) and board[kingRow-i][kingCol+i] != 0:
                if not board[kingRow-i][kingCol+i].isBlack:
                    break
                elif (type(board[kingRow-i][kingCol+i])==type(BishopInstance) or type(board[kingRow-i][kingCol+i])==type(QueenInstance)):
                    return True
                else:
                    break
        for i in range(1,8):
            if (kingRow+i < 8 and kingCol-i >= 0) and board[kingRow+i][kingCol-i] != 0:
                if not board[kingRow+i][kingCol-i].isBlack:
                    break
                elif (type(board[kingRow+i][kingCol-i])==type(BishopInstance) or type(board[kingRow+i][kingCol-i])==type(QueenInstance)):
                    return True
                else:
                    break
        for i in range(1,8):
            if (kingRow-i >= 0 and kingCol-i >= 0) and board[kingRow-i][kingCol-i] != 0:
                if not board[kingRow-i][kingCol-i].isBlack:
                    break
                elif (type(board[kingRow-i][kingCol-i])==type(BishopInstance) or type(board[kingRow-i][kingCol-i])==type(QueenInstance)):
                    return True
                else:
                    break
        #check file checks
        for i in range(1,8):
            if (kingRow+i < 8) and board[kingRow+i][kingCol] != 0:
                if not board[kingRow+i][kingCol].isBlack:
                    break
                elif (type(board[kingRow+i][kingCol])==type(RookInstance) or type(board[kingRow+i][kingCol])==type(QueenInstance)):
                    return True
                else:
                    break
        for i in range(1,8):
            if (kingCol+i < 8) and board[kingRow][kingCol+i] != 0:
                if not board[kingRow][kingCol+i].isBlack:
                    break
                elif (type(board[kingRow][kingCol+i])==type(RookInstance) or type(board[kingRow][kingCol+i])==type(QueenInstance)):
                    return True
                else:
                    break
        for i in range(1,8):
            if (kingRow-i >= 0) and board[kingRow-i][kingCol] != 0:
                if not board[kingRow-i][kingCol].isBlack:
                    break
                elif (type(board[kingRow-i][kingCol])==type(RookInstance) or type(board[kingRow-i][kingCol])==type(QueenInstance)):
                    return True
                else:
                    break
        for i in range(1,8):
            if (kingCol-i >= 0) and board[kingRow][kingCol-i] != 0:
                if not board[kingRow][kingCol-i].isBlack:
                    break
                elif (type(board[kingRow][kingCol-i])==type(RookInstance) or type(board[kingRow][kingCol-i])==type(QueenInstance)):
                    return True
                else:
                    break
        return False
