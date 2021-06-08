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

        for i in range(8):
            for j in range(8):
                if(self.board[i][j] != 0):
                    self.all_sprites.add(self.board[i][j])
    def checkLegalMove(self):

        if (self.endPosRow,self.endPosCol) in (self.pieceSelected.getPeacefulMoves(self.board)):
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
            if self.checkLegalMove():
                self.board[row][col]=self.pieceSelected
                self.pieceSelected.hasMoved = True
                self.pieceSelected.unselect()
                self.pieceSelected = 0
                self.isPieceSelected = False
    def returnBoard(self):
        return self.board
    def returnSprites(self):
        return self.all_sprites
