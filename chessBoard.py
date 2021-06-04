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
        self.board=[[0]*8]*8
        self.board[1][0]= Pawn(0,64,blackPawnImg,self.gameDisplay)
        self.isPieceSelected = False

        for i in range(8):
            for j in range(8):
                if(self.board[i][j] != 0):
                    self.all_sprites.add(self.board[i][j])
    def checkLegalMove(self):
        PawnInstance= Pawn(0,0,blackPawnImg,self.gameDisplay)
        if type(PawnInstance)==type(self.pieceSelected):
            if(self.startPosRow-self.endPosRow)== -1 and self.startPosCol==self.endPosCol:
                return True
            elif(self.endPosRow-self.startPosRow) == 2 and self.pieceSelected.hasMoved == False:
                return True
            else:
                return False
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
                pygame.draw.circle(self.gameDisplay,(0,0,0),pos,20)
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
