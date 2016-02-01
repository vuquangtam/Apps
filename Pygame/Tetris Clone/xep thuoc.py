# --coding: utf-8 --
import pygame, sys, time, random
from pygame.locals import *

#KHOI TAO CAC HANG SO

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOARDWIDTH = 10
BOARDHEIGHT = 20
BOXSIZE = 20
BOXGAP = 1
XMARGIN = int((WINDOWWIDTH - (BOXSIZE * BOARDWIDTH))/2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE)
BLANK = '.'

#KHOI TAO MAU

AQUA            =   (  0, 255, 255) 
BLACK           =   (  0,   0,   0) 
BLUE            =   (  0,   0, 255) 
CORNFLOWERBLUE  =   (100, 149, 237) 
FUCHSIA         =   (255,   0, 255) 
GRAY            =   (128, 128, 128) 
GREEN           =   (  0, 128,   0) 
LIME            =   (  0, 255,   0) 
MAROON          =   (128,   0,   0) 
NAVYBLUE        =   (  0,   0, 128) 
OLIVE           =   (128, 128,   0) 
PURPLE          =   (128,   0, 128) 
RED             =   (255,   0,   0) 
SILVER          =   (192, 192, 192) 
TEAL            =   (  0, 128, 128) 
WHITE           =   (255, 255, 255) 
YELLOW          =   (255, 255,   0)

COLOR  = (NAVYBLUE, GREEN, GRAY  )
COLOR2 = (BLUE    , LIME , SILVER)
BGCOLOR = BLACK
BORDERCOLOR = AQUA

# DU LIEU CAC KHOI HINH TRONG GAME

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

T_SHAPE = [
           ('.....',
            '..o..',
            '.ooo.',
            '.....',
            '.....'),
           ('.....',
            '..o..',
            '..oo.',
            '..o..',
            '.....'),
           ('.....',
            '.....',
            '.ooo.',
            '..o..',
            '.....'),
           ('.....',
            '..o..',
            '.oo..',
            '..o..',
            '.....')
          ] 
L_SHAPE = [
           ('.....',
            '..o..',
            '..o..',
            '..oo.',
            '.....'),
           ('.....',
            '.....',
            '.ooo.',
            '.o...',
            '.....'),
           ('.....',
            '.oo..',
            '..o..',
            '..o..',
            '.....'),
           ('.....',
            '...o.',
            '.ooo.',
            '.....',
            '.....')
          ]
J_SHAPE = [
           ('.....',
            '..o..',
            '..o..',
            '.oo..',
            '.....'),
           ('.....',
            '.o...',
            '.ooo.',
            '.....',
            '.....'),
           ('.....',
            '..oo.',
            '..o..',
            '..o..',
            '.....'),
           ('.....',
            '.....',
            '.ooo.',
            '...o.',
            '.....')
          ]
O_SHAPE = [
           ('.....',
            '.....',
            '..oo.',
            '..oo.',
            '.....')
          ]
S_SHAPE = [
           ('.....',
            '..oo.',
            '.oo..',
            '.....',
            '.....'),
           ('.....',
            '..o..',
            '..oo.',
            '...o.',
            '.....')
          ]
Z_SHAPE = [
           ('.....',
            '.oo..',
            '..oo.',
            '.....',
            '.....'),
           ('.....',
            '..o..',
            '.oo..',
            '.o...',
            '.....')
          ]
I_SHAPE = [
           ('..o..',
            '..o..',
            '..o..',
            '..o..',
            '.....'),
           ('.....',
            '.....',
            'oooo.',
            '.....',
            '.....')
          ]
DOT =     [
           ('.....',
            '.....',
            '..a..',
            '..b..',
            '.....'),
           ('.....',
            '.....',
            '..ab.',
            '.....',
            '.....'),
           ('.....',
            '.....',
            '..b..',
            '..a..',
            '.....'),
           ('.....',
            '.....',
            '..ba.',
            '.....',
            '.....')
          ]

PIECES = {'DOT ' : DOT,
         }
PIECE = {
          'I_SHAPE' : I_SHAPE,
          'O_SHAPE' : O_SHAPE,
          'Z_SHAPE' : Z_SHAPE,
          'S_SHAPE' : S_SHAPE,
          'T_SHAPE' : T_SHAPE,
          'L_SHAPE' : L_SHAPE,
          'J_SHAPE' : J_SHAPE,
         }

#CHUYEN SANG HE TOA DO PIXEL

def run():
    global windowSurface, clockFPS, BASICFONT
    pygame.init()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
    pygame.display.set_caption('Tetris')
    clockFPS = pygame.time.Clock()
    BASICFONT = pygame.font.Font('Font.TTF',25)
    pygame.mixer.music.load('music.mp3')
    score = 0
    board = getNewBoard()
    fallingPiece = None
    nextPiece = getNewPiece()
    fallTime = time.time()
    moveRight, moveLeft, moveDown = False, False, False
    moveLeftRightTime = 0

    windowSurface.fill(NAVYBLUE)
    drawText('TETRIS')
    pygame.display.update()
    time.sleep(0.5)
    pygame.event.get()
    waitForPressAKey()
    #pygame.mixer.music.play(-1,0.0)

    while True:
        if fallingPiece == None:
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            if not isValidMove(board,fallingPiece):
                drawText('Game Over')
                pygame.display.update()
                time.sleep(0.5)
                pygame.event.get()
                waitForPressAKey()

                score = 0
                board = getNewBoard()
                fallingPiece = None
                nextPiece = getNewPiece()
                fallTime = time.time()
                moveRight, moveLeft, moveDown = False, False, False
                moveLeftRightTime = 0
                pygame.mixer.music.play(-1,0.0)

        checkForQuit()
        for event in pygame.event.get():

            if event.type == KEYUP:
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_DOWN:
                    moveDown = False
                    
            if event.type == KEYDOWN:
                if event.key == K_LEFT and isValidMove(board,fallingPiece,adjX = -1):
                    fallingPiece['x'] -= 1
                    moveRight = False
                    moveLeft  = True
                    moveLeftRightTime = time.time() 
                if event.key == K_RIGHT and isValidMove(board,fallingPiece,adjX = 1):
                    fallingPiece['x'] += 1
                    moveRight = True
                    moveLeft  = False
                    moveLeftRightTime = time.time()
                if event.key == K_DOWN and isValidMove(board,fallingPiece,adjY = 1):
                    fallingPiece['y'] += 1
                    moveDown = True
                    moveLeftRightTime = time.time()
                if event.key == K_UP:
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % (len(PIECES[fallingPiece['shape']]))
                    if not isValidMove(board,fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % (len(PIECES[fallingPiece['shape']]))
                if event.key == K_SPACE:
                    for y in range(0,BOARDHEIGHT - 1):
                        if not isValidMove(board, fallingPiece, adjY = y):
                            break
                    fallingPiece['y'] += y - 1

        if(moveLeft or moveRight or moveDown) and time.time() - moveLeftRightTime > 0.3:
            if moveLeft and isValidMove(board, fallingPiece, adjX = -1):
                fallingPiece['x'] -= 1
            elif moveRight and isValidMove(board, fallingPiece, adjX = 1):
                fallingPiece['x'] += 1
            elif moveDown and isValidMove(board, fallingPiece, adjY = 1):
                fallingPiece['y'] += 1
                
        if time.time() - fallTime > 0.3:
            if not isValidMove(board,fallingPiece,adjY = 1):
                addToBoard(fallingPiece,board)
                fallingPiece = None
            else:
                fallingPiece['y'] += 1
                fallTime = time.time()

        score += checkScore(board)
        windowSurface.fill(BGCOLOR)
        drawBoard(board)
        drawScore(score)
       # drawNextPiece(nextPiece)
        if fallingPiece != None:
            drawPiece(fallingPiece)
        pygame.display.update()
        clockFPS.tick(20)
        
def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()

def waitForPressAKey():
    while True:
        checkForQuit()
        for event in pygame.event.get([KEYUP, KEYDOWN]):
            if event.type == KEYDOWN:
                continue
            return event.key
            

def getNewPiece():
    shape = random.choice(list(PIECES.keys()))
    piece = {
             'x' : int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2) - 1,
             'y' : -2,
             'shape' : shape,
             'rotation' : random.randint(0,len(PIECES[shape]) - 1),
             'colora' : random.randint(0,len(COLOR) - 1),
             'colorb' : random.randint(0,len(COLOR) - 1),
            }
    return piece
    

def getNewBoard():
    board1 = []
    board2 = []
    for x in range(BOARDWIDTH):
        col = [BLANK] * BOARDHEIGHT
        board1.append(col)
    for x in range(BOARDWIDTH):
        col = [0] * BOARDHEIGHT
        board2.append(col)
    return [board1,board2]
def addToBoard(piece,board):
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] == 'a':
                board[0][x + piece['x']][y + piece['y']] = piece['colora']
                board[1][x + piece['x']][y + piece['y']] = 2
            elif PIECES[piece['shape']][piece['rotation']][y][x] == 'b':
                board[0][x + piece['x']][y + piece['y']] = piece['colorb']
                board[1][x + piece['x']][y + piece['y']] = 2
def isValidMove(board, piece, adjX = 0, adjY = 0):
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if piece['y'] + y + adjY < 0 or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            else :
                if piece['x'] + x + adjX == -1 or piece['x'] + x + adjX == BOARDWIDTH or piece['y'] + y + adjY  >= BOARDHEIGHT -1 :
                    return False
                if board[0][piece['x'] + x + adjX][piece['y'] + y + adjY] != BLANK:
                    return False
    return True

def checkCol(board, x, y):
    if y + 2 < BOARDHEIGHT:
        if board[0][x][y] == board[0][x][y + 2]:
            num = 1
            while (board[0][x][y] == board[0][x][y + num]):
                if y + num + 1< BOARDHEIGHT:
                    num += 1
                else:
                     break
            print x, y, num
            if num >= 3:
                print x, y,'hihi'
                for i in range(num):
                    print x, y + i,'hoho'
                    board[0][x][y + i] = BLANK

def checkRow(board, x, y):
    if x + 2 < BOARDWIDTH:
        if board[0][x][y] == board[0][x + 2][y]:
            num = 1
            while (board[0][x][y] == board[0][x + num][y]):
                if x + num + 1< BOARDWIDTH:
                    num += 1
                else :
                    break
            print num
            if num >= 3:
                if board[1][x + 1][y] == 2:
                    checkDrop(board, x + 1, y)
                if board[1][x - 1][y] == 2:
                    checkDrop(board, x - 1, y)
                if board[1][x][y - 1] == 2:
                    checkDrop(board, x, y - 1)
                print x, y,'hihi'
                for i in range(num):
                    print x + i, y,'haha'
                    board[0][x + i][y] = BLANK

def checkDrop(board, x, y):
    for i in range(1, BOARDHEIGHT - y):
        if board[0][x][y + i] != BLANK:
            break
    board[0][x][y], board[0][x][y + i - 1] = board[0][x][y + i - 1], board[0][x][y]
def checkScore(board):
    addScore = 0
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[0][x][y] != BLANK:
                checkCol(board, x, y)
                checkRow(board, x, y)
    return addScore
def getPixelCoords(boxx,boxy):
    pixelx = XMARGIN + (BOXSIZE + BOXGAP) * boxx
    pixely = TOPMARGIN + (BOXSIZE + BOXGAP) * boxy 
    return pixelx, pixely

def drawBox(boxx, boxy, color, pixelx = None, pixely = None):
    if color == BLANK:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = getPixelCoords(boxx,boxy)
    pygame.draw.rect(windowSurface, COLOR[color], (pixelx, pixely, BOXSIZE, BOXSIZE))
    pygame.draw.rect(windowSurface, COLOR2[color], (pixelx, pixely, BOXSIZE - 4, BOXSIZE - 4))
    
def drawPiece(piece, pixelx = None, pixely = None):
    if pixelx == None and pixely == None:
        pixelx, pixely = getPixelCoords(piece['x'], piece['y'])
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] == 'a':
                drawBox(0, 0, piece['colora'],pixelx + x * (BOXSIZE + BOXGAP), pixely + y * (BOXSIZE + BOXGAP))
            elif PIECES[piece['shape']][piece['rotation']][y][x] == 'b':
                drawBox(0, 0, piece['colorb'],pixelx + x * (BOXSIZE + BOXGAP), pixely + y * (BOXSIZE + BOXGAP))

def drawBoard(board):
    
    borderWidth = BOARDWIDTH * BOXSIZE
    borderHeight = BOARDHEIGHT * BOXSIZE
#    pygame.draw.rect(windowSurface,WHITE,(XMARGIN - 3,TOPMARGIN - 3, borderWidth + 15, borderHeight + 3))
    pygame.draw.rect(windowSurface,BORDERCOLOR,(XMARGIN - 3,TOPMARGIN - 3, borderWidth + 15, borderHeight + 3),3)

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[0][x][y] != BLANK:
                drawBox(x, y, board[0][x][y])
                
def drawScore(score):
    scoreSurf = BASICFONT.render('Score : %d' %score, 1,WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 10)
    windowSurface.blit(scoreSurf, scoreRect)

def drawNextPiece(piece):
    pygame.draw.rect(windowSurface,TEAL,(WINDOWWIDTH - 150, 100, BOXSIZE * TEMPLATEWIDTH, BOXSIZE * TEMPLATEHEIGHT))
    pygame.draw.rect(windowSurface,OLIVE,(WINDOWWIDTH - 150, 100, BOXSIZE * TEMPLATEWIDTH, BOXSIZE * TEMPLATEHEIGHT),4)
    drawPiece(piece, WINDOWWIDTH - 150, 100)

def drawText(text):
    FONT = pygame.font.SysFont(None, 100)

    textSurf = FONT.render(text, 1, SILVER)
    textRect = textSurf.get_rect()
    textRect.centerx, textRect.centery = int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2)
    windowSurface.blit(textSurf, textRect)

    textSurf2 = FONT.render(text, 1, WHITE)
    textRect2 = textSurf.get_rect()
    textRect2.centerx, textRect2.centery = int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3
    windowSurface.blit(textSurf2, textRect2)
run()













    
