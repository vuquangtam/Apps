# --coding: utf-8 --
import pygame, sys, time, random
from pygame.locals import *

#KHOI TAO CAC HANG SO

WINDOWWIDTH = 853
WINDOWHEIGHT = 480
BOXSIZE = 20
BOXGAP = 1
BOARDWIDTH = 10
BOARDHEIGHT = 20
COOPBOARDWIDTH = 12
COOPBOARDHEIGHT = 20
COOPXMARGIN = int((WINDOWWIDTH - COOPBOARDWIDTH * BOXSIZE)/2)
XMARGIN = 50
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE)
BOARDGAP = WINDOWWIDTH - (BOARDWIDTH * BOXSIZE + XMARGIN) * 2
LRFEQ = 0.15
DOWNDELAY = 0.3
BLANK = '.'


#KHOI TAO MAU
 
BLUE            =   ( 20,  20, 255)
GREEN           =   ( 20, 255,  20) 
CORNFLOWERBLUE  =   (100, 149, 237) 
RED             =   (255,  20,  20)
YELLOW          =   (255, 255,  20)
GRAY            =   (128, 128,  20)
PINK            =   (255, 168, 255)

LIGHTBLUE       =   (  0,   0, 235)
LIGHTGREEN      =   (  0, 235,   0) 
LIGHTCORNBLUE   =   ( 80, 129, 217)
LIGHTRED        =   (235,   0,   0)
LIGHTYELLOW     =   (235, 235,   0)
LIGHTGRAY       =   (108, 108,   0)
LIGHTPINK       =   (235, 148, 235)

PURPLE          =   (148,  20, 148) 
LIGHTPURPLE     =   (128,   0, 128)  
WHITE           =   (255, 255, 255)
LIGHTWHITE      =   (215, 215, 215)
FUCHSIA         =   (255,  20, 255)
LIGHTFUCHSIA    =   (235,   0, 235)
GRAY            =   (128, 128, 128) 
LIGHTGRAY       =   (108, 108, 108) 
SILVER          =   (192, 192, 192) 
LIGHTSILVER     =   (172, 172, 172) 
MAROON          =   (128,  20,  20)
LIGHTMAROON     =   (128,   0,   0)

BLUEBG          =   ( 50,  50, 255)
AQUA            =   (  0, 255, 255) 
BLACK           =   (  0,   0,   0)
OLIVE           =   (128, 128,   0)
TEAL            =   (  0, 128, 128)
YELLOW          =   (255, 255,   0)

COLOR   = [BLUE     , GREEN     , CORNFLOWERBLUE, RED     , YELLOW     , GRAY     , PINK     ]
COLOR2  = [LIGHTBLUE, LIGHTGREEN, LIGHTCORNBLUE , LIGHTRED, LIGHTYELLOW, LIGHTGRAY, LIGHTPINK]
LEVELCOLOR  = [PURPLE     , GRAY     , WHITE     , MAROON     , SILVER     , FUCHSIA     ]
LEVELCOLOR2 = [LIGHTPURPLE, LIGHTGRAY, LIGHTWHITE, LIGHTMAROON, LIGHTSILVER, LIGHTFUCHSIA]
BGCOLOR = [BLUEBG, OLIVE, LIGHTGRAY, TEAL]

BOARDBGCOLOR = BLACK
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

PIECES = {
          'I_SHAPE' : I_SHAPE,
          'O_SHAPE' : O_SHAPE,
          'Z_SHAPE' : Z_SHAPE,
          'S_SHAPE' : S_SHAPE,
          'T_SHAPE' : T_SHAPE,
          'L_SHAPE' : L_SHAPE,
          'J_SHAPE' : J_SHAPE,
         }

#CHUYEN SANG HE TOA DO PIXEL


def main():
    global windowSurface, clockFPS, BASICFONT, MUSIC
    pygame.init()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Tetris')
    clockFPS = pygame.time.Clock()
    BASICFONT = pygame.font.Font('Font.TTF',25)
    MUSIC = 'MUSIC : ON'
    
    game()
#    coopMode()
#    pauseMenu()
    
def onePlayerMode():
    score = 0
    board = getNewBoard()
    logoBoard = getNewLogoBoard()
    fallingPiece = None
    nextPiece = getNewPiece()
    fallTime = time.time()
    moveRight, moveLeft, moveDown = False, False, False
    moveLeftRightTime, moveDownTime = 0, 0

    pygame.mixer.music.load('Tetris - Kalinka.mid')
    if MUSIC == 'MUSIC : ON':
        pygame.mixer.music.play(-1,0.0)
    
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
                logoBoard = getNewLogoBoard()
                fallingPiece = None
                nextPiece = getNewPiece()
                fallTime = time.time()
                moveRight, moveLeft, moveDown = False, False, False
                moveLeftRightTime, moveDownTime = 0, 0
                if MUSIC == 'MUSIC : ON':
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
                if event.key == K_ESCAPE:
                    pauseMenu()
                    
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
                    moveDownTime = time.time()
                if event.key == K_UP:
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % (len(PIECES[fallingPiece['shape']]))
                    if not isValidMove(board,fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % (len(PIECES[fallingPiece['shape']]))
                if event.key == K_SPACE:
                    for y in range(0,BOARDHEIGHT - 1):
                        if not isValidMove(board, fallingPiece, adjY = y):
                            break
                    fallingPiece['y'] += y - 1

        if(moveLeft or moveRight) and time.time() - moveLeftRightTime > LRFEQ:
            if moveLeft and isValidMove(board, fallingPiece, adjX = -1):
                fallingPiece['x'] -= 1
            elif moveRight and isValidMove(board, fallingPiece, adjX = 1):
                fallingPiece['x'] += 1
            moveLeftRightTime = time.time()

        if moveDown and time.time() - moveDownTime > DOWNDELAY and isValidMove(board, fallingPiece, adjY = 1):
            fallingPiece['y'] += 1

        level,speed = generateLevelAndSpeed(score)
        
        if time.time() - fallTime > speed:
            if not isValidMove(board,fallingPiece,adjY = 1):
                addToBoard(fallingPiece,board)
                logoBoard[fallingPiece['shape']] += 1
                fallingPiece = None
            else:
                fallingPiece['y'] += 1
                fallTime = time.time()

        score += checkCompleteLine(board)

        drawBG(0)
        drawLogoBoard(logoBoard)
        drawBoard(board, level % len(LEVELCOLOR))
        drawScoreAndLevel(score,level)
        
        drawNextPiece(nextPiece, 1)
        if fallingPiece != None:
            drawPiece(fallingPiece)
        pygame.display.update()
        clockFPS.tick(20)
        
def twoPlayerMode():
    score, score2 = 0, 0
    board, board2 = getNewBoard(), getNewBoard()
    fallingPiece, fallingPiece2 = None, None
    nextPiece, nextPiece2 = getNewPiece(), getNewPiece()
    fallTime, fallTime2 = time.time(), time.time()
    moveRight, moveLeft, moveDown = False, False, False
    moveRight2, moveLeft2, moveDown2 = False, False, False
    moveLeftRightTime, moveDownTime, moveLeftRightTime2, moveDownTime2 = 0, 0, 0, 0 

    pygame.mixer.music.load('Tetris - Loginska.mid')
    if MUSIC == 'MUSIC : ON':
        pygame.mixer.music.play(-1,0.0)

    while True:
        if fallingPiece == None:
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            if not isValidMove(board,fallingPiece):
                drawText('PLAYER 2 WIN')
                pygame.display.update()
                time.sleep(0.5)
                pygame.event.get()
                waitForPressAKey()

                score, score2 = 0, 0
                board, board2 = getNewBoard(), getNewBoard()
                fallingPiece, fallingPiece2 = None, None
                nextPiece, nextPiece2 = getNewPiece(), getNewPiece()
                fallTime, fallTime2 = time.time(), time.time()
                moveRight, moveLeft, moveDown = False, False, False
                moveRight2, moveLeft2, moveDown2 = False, False, False
                moveLeftRightTime, moveDownTime, moveLeftRightTime2, moveDownTime2 = 0, 0, 0, 0 
                if MUSIC == 'MUSIC : ON':
                    pygame.mixer.music.play(-1,0.0)

        if fallingPiece2 == None:
            fallingPiece2 = nextPiece2
            nextPiece2 = getNewPiece()
            if not isValidMove(board2,fallingPiece2):
                drawText('PLAYER 1 WIN')
                pygame.display.update()
                time.sleep(0.5)
                pygame.event.get()
                waitForPressAKey()

                score, score2 = 0, 0
                board, board2 = getNewBoard(), getNewBoard()
                fallingPiece, fallingPiece2 = None, None
                nextPiece, nextPiece2 = getNewPiece(), getNewPiece()
                fallTime, fallTime2 = time.time(), time.time()
                moveRight, moveLeft, moveDown = False, False, False
                moveRight2, moveLeft2, moveDown2 = False, False, False
                moveLeftRightTime, moveDownTime, moveLeftRightTime2, moveDownTime2 = 0, 0, 0, 0 
                if MUSIC == 'MUSIC : ON':
                    pygame.mixer.music.play(-1,0.0)

        checkForQuit()
        for event in pygame.event.get():

            if event.type == KEYUP:
                if event.key == K_a:
                    moveLeft = False
                if event.key == K_d:
                    moveRight = False
                if event.key == K_s:
                    moveDown = False

                if event.key == K_LEFT:
                    moveLeft2 = False
                if event.key == K_RIGHT:
                    moveRight2 = False
                if event.key == K_DOWN:
                    moveDown2 = False

                if event.key == K_ESCAPE:
                    pauseMenu()
                                        
            if event.type == KEYDOWN:
                if event.key == K_a and isValidMove(board,fallingPiece,adjX = -1):
                    fallingPiece['x'] -= 1
                    moveRight = False
                    moveLeft  = True
                    moveLeftRightTime = time.time() 
                if event.key == K_d and isValidMove(board,fallingPiece,adjX = 1):
                    fallingPiece['x'] += 1
                    moveRight = True
                    moveLeft  = False
                    moveLeftRightTime = time.time()
                if event.key == K_s and isValidMove(board,fallingPiece,adjY = 1):
                    fallingPiece['y'] += 1
                    moveDown = True
                    moveDownTime = time.time()
                if event.key == K_w:
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % (len(PIECES[fallingPiece['shape']]))
                    if not isValidMove(board,fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % (len(PIECES[fallingPiece['shape']]))
                if event.key == K_SPACE:
                    for y in range(0,BOARDHEIGHT - 1):
                        if not isValidMove(board, fallingPiece, adjY = y):
                            break
                    fallingPiece['y'] += y - 1


                if event.key == K_LEFT and isValidMove(board2,fallingPiece2,adjX = -1):
                    fallingPiece2['x'] -= 1
                    moveRight2 = False
                    moveLeft2  = True
                    moveLeftRightTime2 = time.time() 
                if event.key == K_RIGHT and isValidMove(board2,fallingPiece2,adjX = 1):
                    fallingPiece2['x'] += 1
                    moveRight2 = True
                    moveLeft2  = False
                    moveLeftRightTime2 = time.time()
                if event.key == K_DOWN and isValidMove(board2,fallingPiece2,adjY = 1):
                    fallingPiece2['y'] += 1
                    moveDown2 = True
                    moveDownTime2 = time.time()
                if event.key == K_UP:
                    fallingPiece2['rotation'] = (fallingPiece2['rotation'] + 1) % (len(PIECES[fallingPiece2['shape']]))
                    if not isValidMove(board2,fallingPiece2):
                        fallingPiece2['rotation'] = (fallingPiece2['rotation'] - 1) % (len(PIECES[fallingPiece2['shape']]))
                if event.key == K_RETURN:
                    for y in range(0,BOARDHEIGHT - 1):
                        if not isValidMove(board2, fallingPiece2, adjY = y):
                            break
                    fallingPiece2['y'] += y - 1

        if(moveLeft or moveRight) and time.time() - moveLeftRightTime > LRFEQ:
            if moveLeft and isValidMove(board, fallingPiece, adjX = -1):
                fallingPiece['x'] -= 1
            elif moveRight and isValidMove(board, fallingPiece, adjX = 1):
                fallingPiece['x'] += 1
            moveLeftRightTime = time.time()

        if moveDown and time.time() - moveDownTime > DOWNDELAY and isValidMove(board, fallingPiece, adjY = 1):
            fallingPiece['y'] += 1

        if(moveLeft2 or moveRight2) and time.time() - moveLeftRightTime2 > LRFEQ:
            if moveLeft2 and isValidMove(board2, fallingPiece2, adjX = -1):
                fallingPiece2['x'] -= 1
            elif moveRight2 and isValidMove(board2, fallingPiece2, adjX = 1):
                fallingPiece2['x'] += 1
            moveLeftRightTime2 = time.time()

        if moveDown2 and time.time() - moveDownTime2 > DOWNDELAY and isValidMove(board2, fallingPiece2, adjY = 1):
            fallingPiece2['y'] += 1

        level,speed = generateLevelAndSpeed(score)
        
        if time.time() - fallTime > speed:
            if not isValidMove(board,fallingPiece,adjY = 1):
                addToBoard(fallingPiece,board)
                fallingPiece = None
            else:
                fallingPiece['y'] += 1
                fallTime = time.time()

        level2,speed2 = generateLevelAndSpeed(score2)
        
        if time.time() - fallTime2 > speed2:
            if not isValidMove(board2, fallingPiece2, adjY = 1):
                addToBoard(fallingPiece2, board2)
                fallingPiece2 = None
            else:
                fallingPiece2['y'] += 1
                fallTime2 = time.time()

        
        score += checkCompleteLine(board)
        score2 += checkCompleteLine(board2)
        
        drawBG(1)
        drawBoard(board, level % len(LEVELCOLOR))
        drawBoard(board2, level2 % len(LEVELCOLOR), player = 2)
        drawScoreAndLevel(score, level)
        drawScoreAndLevel(score2, level2, 2)
        drawNextPiece(nextPiece, 1)
        drawNextPiece(nextPiece2, 2)
        if fallingPiece != None:
            drawPiece(piece = fallingPiece, player = 1)
        if fallingPiece2 != None:
            drawPiece(piece = fallingPiece2, player = 2)
        pygame.display.update()
        clockFPS.tick(20)
        
def coopMode():
    score = 0
    board = getNewBoard(True)
    fallingPiece, fallingPiece2 = None, None
    nextPiece, nextPiece2 = getNewPiece(True, 1), getNewPiece(True, 2)
    fallTime, fallTime2 = time.time(), time.time()
    moveRight, moveLeft, moveDown = False, False, False
    moveRight2, moveLeft2, moveDown2 = False, False, False
    moveLeftRightTime, moveDownTime, moveLeftRightTime2, moveDownTime2 = 0, 0, 0, 0

    pygame.mixer.music.load('Tetris - Bradinsky.mid')
    if MUSIC == 'MUSIC : ON':
        pygame.mixer.music.play(-1,0.0)

    while True:
        if fallingPiece == None:
            fallingPiece = nextPiece
            nextPiece = getNewPiece(True, 1)
            if not isValidMove(board,fallingPiece,coop = True):
                drawText('GAME OVER')
                pygame.display.update()
                time.sleep(0.5)
                pygame.event.get()
                waitForPressAKey()

                score = 0
                board = getNewBoard(True)
                fallingPiece, fallingPiece2 = None, None
                nextPiece, nextPiece2 = getNewPiece(True, 1), getNewPiece(True, 2)
                fallTime, fallTime2 = time.time(), time.time()
                moveRight, moveLeft, moveDown = False, False, False
                moveRight2, moveLeft2, moveDown2 = False, False, False
                moveLeftRightTime, moveDownTime, moveLeftRightTime2, moveDownTime2 = 0, 0, 0, 0
                if MUSIC == 'MUSIC : ON':
                    pygame.mixer.music.play(-1,0.0)

        if fallingPiece2 == None:
            fallingPiece2 = nextPiece2
            nextPiece2 = getNewPiece(True, 2)
            if not isValidMove(board,fallingPiece2, coop = True):
                drawText('GAME OVER')
                pygame.display.update()
                time.sleep(0.5)
                pygame.event.get()
                waitForPressAKey()

                score = 0
                board = getNewBoard(True)
                fallingPiece, fallingPiece2 = None, None
                nextPiece, nextPiece2 = getNewPiece(True, 1), getNewPiece(True, 2)
                fallTime, fallTime2 = time.time(), time.time()
                moveRight, moveLeft, moveDown = False, False, False
                moveRight2, moveLeft2, moveDown2 = False, False, False
                moveLeftRightTime, moveDownTime, moveLeftRightTime2, moveDownTime2 = 0, 0, 0, 0
                if MUSIC == 'MUSIC : ON':
                    pygame.mixer.music.play(-1,0.0)

        checkForQuit()
        for event in pygame.event.get():

            if event.type == KEYUP:
                if event.key == K_a:
                    moveLeft = False
                if event.key == K_d:
                    moveRight = False
                if event.key == K_s:
                    moveDown = False

                if event.key == K_LEFT:
                    moveLeft2 = False
                if event.key == K_RIGHT:
                    moveRight2 = False
                if event.key == K_DOWN:
                    moveDown2 = False

                if event.key == K_ESCAPE:
                    pauseMenu()
                                        
            if event.type == KEYDOWN:
                if event.key == K_a and isValidMove(board,fallingPiece,adjX = -1, coop = True) and not isCollideBrick(fallingPiece, fallingPiece2, adjX = -1):
                    fallingPiece['x'] -= 1
                    moveRight = False
                    moveLeft  = True
                    moveLeftRightTime = time.time() 
                if event.key == K_d and isValidMove(board,fallingPiece,adjX = 1, coop = True) and not isCollideBrick(fallingPiece, fallingPiece2, adjX = 1):
                    fallingPiece['x'] += 1
                    moveRight = True
                    moveLeft  = False
                    moveLeftRightTime = time.time()
                if event.key == K_s and isValidMove(board,fallingPiece,adjY = 1, coop = True) and not isCollideBrick(fallingPiece, fallingPiece2, adjY = 1):
                    fallingPiece['y'] += 1
                    moveDown = True
                    moveDownTime = time.time()
                if event.key == K_w:
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % (len(PIECES[fallingPiece['shape']]))
                    if not isValidMove(board, fallingPiece, coop = True) or isCollideBrick(fallingPiece, fallingPiece2):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % (len(PIECES[fallingPiece['shape']]))
                if event.key == K_SPACE:
                    for y in range(0,BOARDHEIGHT - 1):
                        if not isValidMove(board, fallingPiece, adjY = y, coop = True) or isCollideBrick(fallingPiece, fallingPiece2, adjX = y):
                            break
                    fallingPiece['y'] += y - 1


                if event.key == K_LEFT and isValidMove(board,fallingPiece2,adjX = -1, coop = True) and not isCollideBrick(fallingPiece2, fallingPiece, adjX = -1):
                    fallingPiece2['x'] -= 1
                    moveRight2 = False
                    moveLeft2  = True
                    moveLeftRightTime2 = time.time() 
                if event.key == K_RIGHT and isValidMove(board,fallingPiece2,adjX = 1, coop = True) and not isCollideBrick(fallingPiece2, fallingPiece, adjX = 1):
                    fallingPiece2['x'] += 1
                    moveRight2 = True
                    moveLeft2  = False
                    moveLeftRightTime2 = time.time()
                if event.key == K_DOWN and isValidMove(board,fallingPiece2,adjY = 1, coop = True) and not isCollideBrick(fallingPiece2, fallingPiece, adjY = 1):
                    fallingPiece2['y'] += 1
                    moveDown2 = True
                    moveDownTime2 = time.time()
                if event.key == K_UP:
                    fallingPiece2['rotation'] = (fallingPiece2['rotation'] + 1) % (len(PIECES[fallingPiece2['shape']]))
                    if not isValidMove(board, fallingPiece2, coop = True) or isCollideBrick(fallingPiece2, fallingPiece):
                        fallingPiece2['rotation'] = (fallingPiece2['rotation'] - 1) % (len(PIECES[fallingPiece2['shape']]))
                if event.key == K_RETURN:
                    for y in range(0,BOARDHEIGHT - 1):
                        if not isValidMove(board, fallingPiece2, adjY = y, coop = True) or isCollideBrick(fallingPiece2, fallingPiece, adjY = y):
                            break
                    fallingPiece2['y'] += y - 1

        if(moveLeft or moveRight ) and time.time() - moveLeftRightTime > LRFEQ:
            if moveLeft and isValidMove(board, fallingPiece, adjX = -1, coop = True) and not isCollideBrick(fallingPiece, fallingPiece2, adjX = -1):
                fallingPiece['x'] -= 1
            elif moveRight and isValidMove(board, fallingPiece, adjX = 1, coop = True) and not isCollideBrick(fallingPiece, fallingPiece2, adjX = 1):
                fallingPiece['x'] += 1
            moveLeftRightTime = time.time()
            
        if moveDown and isValidMove(board, fallingPiece, adjY = 1, coop = True) and not isCollideBrick(fallingPiece, fallingPiece2, adjY = 1) and time.time() - moveDownTime > DOWNDELAY:
            fallingPiece['y'] += 1
        
        if(moveLeft2 or moveRight2) and time.time() - moveLeftRightTime2 > LRFEQ:
            if moveLeft2 and isValidMove(board, fallingPiece2, adjX = -1, coop = True) and not isCollideBrick(fallingPiece2, fallingPiece, adjX = -1):
                fallingPiece2['x'] -= 1
            elif moveRight2 and isValidMove(board, fallingPiece2, adjX = 1, coop = True) and not isCollideBrick(fallingPiece2, fallingPiece, adjX = 1):
                fallingPiece2['x'] += 1
            moveLeftRightTime2 = time.time()

        if moveDown2 and isValidMove(board, fallingPiece2, adjY = 1, coop = True) and not isCollideBrick(fallingPiece2, fallingPiece, adjY = 1) and time.time() - moveDownTime2 > DOWNDELAY:
                fallingPiece2['y'] += 1
                
        level,speed = generateLevelAndSpeed(score)
        
        if time.time() - fallTime > speed:
            if not isValidMove(board,fallingPiece,adjY = 1, coop = True):
                addToBoard(fallingPiece,board)
                fallingPiece = None
            else:
                fallingPiece['y'] += 1
                fallTime = time.time()

        if time.time() - fallTime2 > speed:
            if not isValidMove(board,fallingPiece2,adjY = 1, coop = True):
                addToBoard(fallingPiece2,board)
                fallingPiece2 = None
            else:
                fallingPiece2['y'] += 1
                fallTime2 = time.time()
        
        score += checkCompleteLine(board, True)
        
        drawBG(3, True)
        drawBoard(board, level % len(LEVELCOLOR), coop = True)
        #drawScoreAndLevel(score, level)
        drawNextPiece(nextPiece, 1, coop = True)
        drawNextPiece(nextPiece2, 2, coop = True)
        if fallingPiece != None:
            drawPiece(piece = fallingPiece, player = 1, coop = True)
        if fallingPiece2 != None:
            drawPiece(piece = fallingPiece2, player = 2, coop = True)
        pygame.display.update()
        clockFPS.tick(20)

def coopModeSplitScreen():
    
    score = 0
    board = getNewBoard()
    fallingPiece, fallingPiece2 = None, None
    nextPiece, nextPiece2 = getNewPiece(), getNewPiece()
    fallTime, fallTime2 = time.time(), time.time()
    moveRight, moveLeft, moveDown = False, False, False
    moveRight2, moveLeft2, moveDown2 = False, False, False
    moveLeftRightTime, moveDownTime, moveLeftRightTime2, moveDownTime2 = 0, 0, 0, 0

    pygame.mixer.music.load('Tetris - Troika.mid')
    if MUSIC == 'MUSIC : ON':
        pygame.mixer.music.play(-1,0.0)

    while True:
        if fallingPiece == None:
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            if not isValidMove(board,fallingPiece):
                drawText('GAME OVER')
                pygame.display.update()
                time.sleep(0.5)
                pygame.event.get()
                waitForPressAKey()

                score = 0
                board = getNewBoard()
                fallingPiece, fallingPiece2 = None, None
                nextPiece, nextPiece2 = getNewPiece(), getNewPiece()
                fallTime, fallTime2 = time.time(), time.time()
                moveRight, moveLeft, moveDown = False, False, False
                moveRight2, moveLeft2, moveDown2 = False, False, False
                moveLeftRightTime, moveDownTime, moveLeftRightTime2, moveDownTime2 = 0, 0, 0, 0
                if MUSIC == 'MUSIC : ON':
                    pygame.mixer.music.play(-1,0.0)
                
        if fallingPiece2 == None:
            fallingPiece2 = nextPiece2
            nextPiece2 = getNewPiece()
            if not isValidMove(board,fallingPiece2):
                drawText('GAME OVER')
                pygame.display.update()
                time.sleep(0.5)
                pygame.event.get()
                waitForPressAKey()

                score = 0
                board = getNewBoard()
                fallingPiece, fallingPiece2 = None, None
                nextPiece, nextPiece2 = getNewPiece(), getNewPiece()
                fallTime, fallTime2 = time.time(), time.time()
                moveRight, moveLeft, moveDown = False, False, False
                moveRight2, moveLeft2, moveDown2 = False, False, False
                moveLeftRightTime, moveDownTime, moveLeftRightTime2, moveDownTime2 = 0, 0, 0, 0
                if MUSIC == 'MUSIC : ON':
                    pygame.mixer.music.play(-1,0.0)
                
        checkForQuit()
        for event in pygame.event.get():

            if event.type == KEYUP:
                if event.key == K_a:
                    moveLeft = False
                if event.key == K_d:
                    moveRight = False
                if event.key == K_s:
                    moveDown = False

                if event.key == K_LEFT:
                    moveLeft2 = False
                if event.key == K_RIGHT:
                    moveRight2 = False
                if event.key == K_DOWN:
                    moveDown2 = False

                if event.key == K_ESCAPE:
                    pauseMenu()
                                        
            if event.type == KEYDOWN:
                if event.key == K_a and isValidMove(board,fallingPiece,adjX = -1):
                    fallingPiece['x'] -= 1
                    moveRight = False
                    moveLeft  = True
                    moveLeftRightTime = time.time() 
                if event.key == K_d and isValidMove(board,fallingPiece,adjX = 1):
                    fallingPiece['x'] += 1
                    moveRight = True
                    moveLeft  = False
                    moveLeftRightTime = time.time()
                if event.key == K_s and isValidMove(board,fallingPiece,adjY = 1):
                    fallingPiece['y'] += 1
                    moveDown = True
                    moveDownTime = time.time()
                if event.key == K_w:
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % (len(PIECES[fallingPiece['shape']]))
                    if not isValidMove(board,fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % (len(PIECES[fallingPiece['shape']]))
                if event.key == K_SPACE:
                    for y in range(0,BOARDHEIGHT - 1):
                        if not isValidMove(board, fallingPiece, adjY = y):
                            break
                    fallingPiece['y'] += y - 1


                if event.key == K_LEFT and isValidMove(board,fallingPiece2,adjX = -1):
                    fallingPiece2['x'] -= 1
                    moveRight2 = False
                    moveLeft2  = True
                    moveLeftRightTime2 = time.time() 
                if event.key == K_RIGHT and isValidMove(board,fallingPiece2,adjX = 1):
                    fallingPiece2['x'] += 1
                    moveRight2 = True
                    moveLeft2  = False
                    moveLeftRightTime2 = time.time()
                if event.key == K_DOWN and isValidMove(board,fallingPiece2,adjY = 1):
                    fallingPiece2['y'] += 1
                    moveDown2 = True
                    moveDownTime2 = time.time()
                if event.key == K_UP:
                    fallingPiece2['rotation'] = (fallingPiece2['rotation'] + 1) % (len(PIECES[fallingPiece2['shape']]))
                    if not isValidMove(board,fallingPiece2):
                        fallingPiece2['rotation'] = (fallingPiece2['rotation'] - 1) % (len(PIECES[fallingPiece2['shape']]))
                if event.key == K_RETURN:
                    for y in range(0,BOARDHEIGHT - 1):
                        if not isValidMove(board, fallingPiece2, adjY = y):
                            break
                    fallingPiece2['y'] += y - 1

        if(moveLeft or moveRight) and time.time() - moveLeftRightTime > LRFEQ:
            if moveLeft and isValidMove(board, fallingPiece, adjX = -1):
                fallingPiece['x'] -= 1
            elif moveRight and isValidMove(board, fallingPiece, adjX = 1):
                fallingPiece['x'] += 1
            moveLeftRightTime = time.time()

        if moveDown and time.time() - moveDownTime > DOWNDELAY and isValidMove(board, fallingPiece, adjY = 1):
            fallingPiece['y'] += 1

        if(moveLeft2 or moveRight2) and time.time() - moveLeftRightTime2 > LRFEQ:
            if moveLeft2 and isValidMove(board, fallingPiece2, adjX = -1):
                fallingPiece2['x'] -= 1
            elif moveRight2 and isValidMove(board, fallingPiece2, adjX = 1):
                fallingPiece2['x'] += 1
            moveLeftRightTime2 = time.time()

        if moveDown2 and time.time() - moveDownTime2 > DOWNDELAY and isValidMove(board, fallingPiece2, adjY = 1):
            fallingPiece2['y'] += 1
        
        level,speed = generateLevelAndSpeed(score)
        
        if time.time() - fallTime > speed:
            if not isValidMove(board,fallingPiece,adjY = 1):
                addToBoard(fallingPiece,board)
                fallingPiece = None
            else:
                fallingPiece['y'] += 1
                fallTime = time.time()


        if time.time() - fallTime2 > speed:
            if not isValidMove(board, fallingPiece2, adjY = 1):
                addToBoard(fallingPiece2, board)
                fallingPiece2 = None
            else:
                fallingPiece2['y'] += 1
                fallTime2 = time.time()
        
        score += checkCompleteLine(board)
        
        drawBG(2)
        drawBoard(board, level % len(LEVELCOLOR))
        drawBoard(board, level % len(LEVELCOLOR) , player = 2)
        drawScoreAndLevel(score, level)
        drawScoreAndLevel(score, level, 2)
        drawNextPiece(nextPiece, 1)
        drawNextPiece(nextPiece2, 2)
        if fallingPiece != None:
            drawPiece(piece = fallingPiece, player = 1)
        if fallingPiece2 != None:
            drawPiece(piece = fallingPiece2, player = 2)
        pygame.display.update()
        clockFPS.tick(20)

def pauseMenu():
    global MUSIC
    
    FONT = pygame.font.Font('fontMenu.TTF', 20)
    FONTCOLOR = WHITE
    BOXWIDTH = 200
    BOXHEIGHT = 50

    selection = ['resume', 'music', 'backToMenu', 'quit']
    pauseBG = pygame.Surface(windowSurface.get_size())
    pauseBG = pauseBG.convert_alpha()
    r, g, b = BLACK
    pauseBG.fill((r, g, b, 200))
    
    resumeButton = pygame.Rect(WINDOWWIDTH / 2 - BOXWIDTH / 2, 120, BOXWIDTH, BOXHEIGHT)
    musicButton = pygame.Rect(WINDOWWIDTH / 2 - BOXWIDTH / 2, 195, BOXWIDTH, BOXHEIGHT)
    backToMenuButton = pygame.Rect(WINDOWWIDTH / 2 - BOXWIDTH / 2, 270, BOXWIDTH, BOXHEIGHT)
    quitButton = pygame.Rect(WINDOWWIDTH / 2 - BOXWIDTH / 2, 345, BOXWIDTH, BOXHEIGHT)

    resumeSurf = FONT.render('RESUME', True, FONTCOLOR)
    resumeRect = resumeSurf.get_rect()
    resumeRect.center = resumeButton.center

    backToMenuSurf = FONT.render('BACK TO MENU', True, FONTCOLOR)
    backToMenuRect = backToMenuSurf.get_rect()
    backToMenuRect.center = backToMenuButton.center

    quitSurf = FONT.render('QUIT', True, FONTCOLOR)
    quitRect = quitSurf.get_rect()
    quitRect.center = quitButton.center
    
    originalSurf = windowSurface.copy()
    choice = 0
    select = None

    while True:

        musicSurf = FONT.render(MUSIC, True, FONTCOLOR)
        musicRect = musicSurf.get_rect()
        musicRect.center = musicButton.center

        windowSurface.blit(originalSurf, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    choice = (choice - 1) % len(selection)
                elif event.key == K_DOWN:
                    choice = (choice + 1) % len(selection)
                elif event.key == K_RETURN:
                    select = choice
            if event.type == MOUSEMOTION:
                posX,posY = event.pos[0],event.pos[1]
                if resumeButton.collidepoint(posX, posY):
                    choice = 0
                elif musicButton.collidepoint(posX, posY):
                    choice = 1
                elif backToMenuButton.collidepoint(posX, posY):
                    choice = 2
                elif quitButton.collidepoint(posX, posY):
                    choice = 3
                else:
                    mouseMotion = None
            if event.type == MOUSEBUTTONUP:
                posX, posY = event.pos[0], event.pos[1]
                if resumeButton.collidepoint(posX, posY):
                    select = 0
                elif musicButton.collidepoint(posX, posY):
                    select = 1
                elif backToMenuButton.collidepoint(posX, posY):
                    select = 2
                elif quitButton.collidepoint(posX, posY):
                    select = 3
        if select == 0:
            return
        elif select == 1:
            if MUSIC == 'MUSIC : ON':
                MUSIC = 'MUSIC : OFF'
                pygame.mixer.music.stop()
            elif MUSIC == 'MUSIC : OFF':
                MUSIC = 'MUSIC : ON'
                pygame.mixer.music.play(-1, 0.0)
            select = None
        elif select == 2:
            game()
        elif select == 3:
            terminate()
        windowSurface.blit(pauseBG, (0, 0))

        pygame.draw.rect(windowSurface, BLUE,(250, 100, 345, 310),5)
        pygame.draw.rect(windowSurface, BLACK,(250, 100, 345, 310))

        pygame.draw.rect(windowSurface, RED, resumeButton)
        pygame.draw.rect(windowSurface, RED, musicButton)
        pygame.draw.rect(windowSurface, RED, backToMenuButton)
        pygame.draw.rect(windowSurface, RED, quitButton)

        windowSurface.blit(resumeSurf, resumeRect)
        windowSurface.blit(musicSurf, musicRect)
        windowSurface.blit(backToMenuSurf, backToMenuRect)
        windowSurface.blit(quitSurf, quitRect)
        
        if choice == 0:
            pygame.draw.rect(windowSurface, WHITE,(WINDOWWIDTH / 2 - BOXWIDTH / 2 - 3, 120 - 3, BOXWIDTH +6, BOXHEIGHT + 6), 3)
        elif choice == 1:
            pygame.draw.rect(windowSurface, WHITE,(WINDOWWIDTH / 2 - BOXWIDTH / 2 - 3, 195 - 3, BOXWIDTH +6, BOXHEIGHT + 6), 3)
        elif choice == 2:
            pygame.draw.rect(windowSurface, WHITE,(WINDOWWIDTH / 2 - BOXWIDTH / 2 - 3, 270 - 3, BOXWIDTH +6, BOXHEIGHT + 6), 3)
        elif choice == 3:
            pygame.draw.rect(windowSurface, WHITE,(WINDOWWIDTH / 2 - BOXWIDTH / 2 - 3, 345 - 3, BOXWIDTH +6, BOXHEIGHT + 6), 3)
        pygame.display.update()

def game():
    FONT = pygame.font.Font('fontMenu.TTF',20)
    TETRISFONT = pygame.font.Font('tetris.TTF',120)
    MENUBGCOLOR = BLACK
    BORDERBOXCOLOR = YELLOW
    BOXBGCOLOR = RED
    BOXWIDTH = 200
    BOXHEIGHT = 50

    pygame.mixer.music.load('Tetris - Title Screen.mid')
    if MUSIC == 'MUSIC : ON':
        pygame.mixer.music.play(-1, 0.0)
    
    selection = ['1 Player Mode',
                 '2 Player Mode',
                 'Coop Mode',
                 'Coop Mode (2 Box)',
                 'Quit Game']
    choice = 0
    select = None
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key in (K_DOWN, K_s):
                    choice = (choice + 1) % len(selection)
                elif event.key in (K_UP, K_w):
                    choice = (choice - 1) % len(selection)
                elif event.key == K_RETURN:
                    select = choice
            if event.type == MOUSEMOTION:
                posX, posY = event.pos[0], event.pos[1]
                pixelY = 150
                for box in range(len(selection)):
                    X = WINDOWWIDTH / 2 - BOXWIDTH / 2
                    Y = pixelY
                    BOX = pygame.Rect(X, Y, BOXWIDTH, BOXHEIGHT)
                    pixelY += 65
                    if BOX.collidepoint(posX, posY):
                        choice = box
                        break
            if event.type == MOUSEBUTTONUP:
                posX, posY = event.pos[0], event.pos[1]
                pixelY = 150
                for box in range(len(selection)):
                    X = WINDOWWIDTH / 2 - BOXWIDTH / 2
                    Y = pixelY
                    BOX = pygame.Rect(X, Y, BOXWIDTH, BOXHEIGHT)
                    pixelY += 65
                    if BOX.collidepoint(posX, posY):
                        select = box
                        break
    
        if select == 0:
            onePlayerMode()
        elif select == 1:
            twoPlayerMode()
        elif select == 2:
            coopMode()
        elif select == 3:
            coopModeSplitScreen()
        elif select == 4:
            terminate()

        windowSurface.fill(MENUBGCOLOR)

        tetrisSurf = TETRISFONT.render('T.E.T.R.I.S', 1, WHITE)
        tetrisRect = tetrisSurf.get_rect()
        tetrisRect.center = (WINDOWWIDTH / 2, TOPMARGIN * 2 / 3)
        windowSurface.blit(tetrisSurf,tetrisRect)

        pixelY = 150
        for box in range(len(selection)):
            X = WINDOWWIDTH / 2 - BOXWIDTH / 2
            Y = pixelY
            pygame.draw.rect(windowSurface,BOXBGCOLOR,(X, Y, BOXWIDTH, BOXHEIGHT))

            textSurf = FONT.render(selection[box], 1, WHITE)
            textRect = textSurf.get_rect()
            textRect.center = (X + BOXWIDTH / 2, Y + BOXHEIGHT / 2)
            windowSurface.blit(textSurf,textRect)
            
            if box == choice:
                pygame.draw.rect(windowSurface,BORDERBOXCOLOR,(X - 3, Y, BOXWIDTH + 5, BOXHEIGHT + 3),4)

            pixelY += 65
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
            
def generateLevelAndSpeed(score):
    level = int(score / 30) + 1 
    speed = 0.5 - 0.02 * level
    return level, speed 
    
    
def getNewPiece(coop = False, player = 0):
    if (player == 1 or player == 2) and coop:
        width = COOPBOARDWIDTH
        if player == 1:
            adjX = -2
        elif player == 2:
            adjX = 2
    else:
        width = BOARDWIDTH
        adjX = 0
    shape = random.choice(list(PIECES.keys()))
    piece = {
             'x' : int(width / 2) - int(TEMPLATEWIDTH / 2) - 1 + adjX,
             'y' : -2,
             'shape' : shape,
             'rotation' : random.randint(0,len(PIECES[shape]) - 1),
             'color' : random.randint(0,len(COLOR) - 1)
            }
    return piece

def getNewBoard(coop = False):
    board = []
    width = BOARDWIDTH
    height = BOARDHEIGHT
    if coop:
        width = COOPBOARDWIDTH
        height = COOPBOARDHEIGHT
    for x in range(width):
        col = [BLANK] * height
        board.append(col)
    return board

def addToBoard(piece,board):
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']

def isCollideBrick(piece, piece2, adjX = 0, adjY = 0):
    if piece2 != None:
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if piece['y'] + y + adjY < 0 or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                    continue
                for i in range(TEMPLATEWIDTH):
                    for j in range(TEMPLATEHEIGHT):
                        if piece2['y'] + j < 0 or PIECES[piece2['shape']][piece2['rotation']][j][i] == BLANK:
                            continue
                        if piece['x'] + x + adjX == piece2['x'] + i and piece['y'] + y + adjY == piece2['y'] + j:
                            return True
        return False
    else:
        return False
def isValidMove(board, piece, adjX = 0, adjY = 0, coop = False):
    if coop:
        width = COOPBOARDWIDTH
        height = COOPBOARDHEIGHT
    else:
        width = BOARDWIDTH
        height = BOARDHEIGHT
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if piece['y'] + y + adjY < 0 or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            else :
                if piece['x'] + x + adjX == -1 or piece['x'] + x + adjX == width or piece['y'] + y + adjY  >= height -1 :
                    return False
                if board[piece['x'] + x + adjX][piece['y'] + y + adjY] != BLANK:
                    return False
    return True

def isCompleteLine(board, y, coop = False):
    if coop:
        width = COOPBOARDWIDTH
    else:
        width = BOARDWIDTH
    for x in range(width):
        if board[x][y] == BLANK:
            return False
    return True

def checkCompleteLine(board, coop = False):
    if coop:
        width = COOPBOARDWIDTH
        height = COOPBOARDHEIGHT
    else:
        width = BOARDWIDTH
        height = BOARDHEIGHT
    y = height - 1
    addScore = 0
    while y >= 0:
        if isCompleteLine(board,y):
            for pullDownY in range(y, 0, -1):
                for x in range(width):
                    board[x][pullDownY] = board[x][pullDownY - 1]
            for x in range(width):
                board[x][0] = BLANK
            addScore += 1    
        else:
            y -= 1
    return addScore
def getPixelCoords(boxx, boxy , coop = False):
    if coop:
        pixelx = COOPXMARGIN + (BOXSIZE + BOXGAP) * boxx
        pixely = TOPMARGIN + (BOXSIZE + BOXGAP) * boxy 
    else:
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
    
def drawPiece(piece , player = 1, pixelx = None, pixely = None, coop = False):
    if coop == False:
        if pixelx == None and pixely == None:
            pixelx, pixely = getPixelCoords(piece['x'], piece['y'])

        if player == 1:
            for x in range(TEMPLATEWIDTH):
                for y in range(TEMPLATEHEIGHT):
                    if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                        drawBox(0, 0, piece['color'],pixelx + x * (BOXSIZE + BOXGAP), pixely + y * (BOXSIZE + BOXGAP))
        else:
            for x in range(TEMPLATEWIDTH):
                for y in range(TEMPLATEHEIGHT):
                    if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                        drawBox(0, 0, piece['color'],pixelx + BOARDGAP + BOARDWIDTH * BOXSIZE + x * (BOXSIZE + BOXGAP), pixely + y * (BOXSIZE + BOXGAP))
    else:
        if pixelx == None and pixely == None:
            pixelx, pixely = getPixelCoords(piece['x'], piece['y'], True)

        if player == 1:
            for x in range(TEMPLATEWIDTH):
                for y in range(TEMPLATEHEIGHT):
                    if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                        drawBox(0, 0, piece['color'],pixelx + x * (BOXSIZE + BOXGAP), pixely + y * (BOXSIZE + BOXGAP))
        else:
            for x in range(TEMPLATEWIDTH):
                for y in range(TEMPLATEHEIGHT):
                    if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                        drawBox(0, 0, piece['color'],pixelx + x * (BOXSIZE + BOXGAP), pixely + y * (BOXSIZE + BOXGAP))
        
def drawBoardBox(boxx, boxy, level = 0 , pixelx = None, pixely = None):
    if pixelx == None and pixely == None:
        pixelx, pixely = getPixelCoords(boxx,boxy)
    pygame.draw.rect(windowSurface, LEVELCOLOR[level], (pixelx, pixely, BOXSIZE, BOXSIZE))
    pygame.draw.rect(windowSurface, LEVELCOLOR2[level], (pixelx, pixely, BOXSIZE - 4, BOXSIZE - 4))

def TETRISdraw():
    FONT = pygame.font.Font('tetris.TTF', 60)
    FONTCOLOR = RED
    
    pygame.draw.rect(windowSurface,BOARDBGCOLOR,(WINDOWWIDTH / 2 - 30 - 3, TOPMARGIN - 3, 66,400), 3)    
    pygame.draw.rect(windowSurface,BOARDBGCOLOR,(WINDOWWIDTH / 2 - 30, TOPMARGIN, 60,399))

    T_surf  = FONT.render('T', 1, FONTCOLOR)
    T1_rect = T_surf.get_rect()
    T1_rect.center = (XMARGIN + BOXSIZE * BOARDWIDTH + BOARDGAP / 2, TOPMARGIN + 30)
    windowSurface.blit(T_surf, T1_rect)
        
    E_surf  = FONT.render('E', 1, FONTCOLOR)
    E_rect  = E_surf.get_rect()
    E_rect.center = (XMARGIN + BOXSIZE * BOARDWIDTH + BOARDGAP / 2, TOPMARGIN + 90)
    windowSurface.blit(E_surf, E_rect)
    
    T2_rect = T_surf.get_rect()
    T2_rect.center = (XMARGIN + BOXSIZE * BOARDWIDTH + BOARDGAP / 2, TOPMARGIN + 150)
    windowSurface.blit(T_surf, T2_rect)
    
    R_surf  = FONT.render('R', 1, FONTCOLOR)
    R_rect  = R_surf.get_rect()
    R_rect.center = (XMARGIN + BOXSIZE * BOARDWIDTH + BOARDGAP / 2, TOPMARGIN + 210)
    windowSurface.blit(R_surf, R_rect)
    
    I_surf  = FONT.render('I', 1, FONTCOLOR)
    I_rect  = I_surf.get_rect()
    I_rect.center = (XMARGIN + BOXSIZE * BOARDWIDTH + BOARDGAP / 2, TOPMARGIN + 270)
    windowSurface.blit(I_surf, I_rect)
    
    S_surf  = FONT.render('S', 1, FONTCOLOR)
    S_rect  = I_surf.get_rect()
    S_rect.center = (XMARGIN + BOXSIZE * BOARDWIDTH + BOARDGAP / 2 - 10, TOPMARGIN + 330)
    windowSurface.blit(S_surf, S_rect)

def drawBG(choice, coop = False):
    selection = ['1 Player Mode',
                 '2 Player Mode',
                 'Coop Mode',
                 'Coop Mode (2 Box)',
                 'Quit Game']
    
    windowSurface.fill(BGCOLOR[choice])

    if not coop:
        TETRISdraw()

    FONT = pygame.font.Font('fontMenu.TTF', 50)
    drawText(selection[choice], WINDOWWIDTH / 2, 30, FONT, color = choice)
    
def drawBoard(board, level = 0, player = 1, coop = False):
    if coop:
        borderWidth = COOPBOARDWIDTH * BOXSIZE
        borderHeight = COOPBOARDHEIGHT * BOXSIZE
        pygame.draw.rect(windowSurface,BORDERCOLOR,((WINDOWWIDTH - borderWidth) / 2 - 3,TOPMARGIN - 3, borderWidth + 18, borderHeight + 3),3)
        pygame.draw.rect(windowSurface,BOARDBGCOLOR,((WINDOWWIDTH - borderWidth) / 2, TOPMARGIN , borderWidth + 12, borderHeight - 3))
                
        for x in range(COOPBOARDWIDTH):
            for y in range(COOPBOARDHEIGHT):
                if board[x][y] != BLANK:
                    X = COOPXMARGIN + x * (BOXSIZE + BOXGAP)
                    Y = TOPMARGIN + y * (BOXSIZE + BOXGAP)
                    drawBoardBox(0, 0, level, X, Y)
    else:
        borderWidth = BOARDWIDTH * BOXSIZE
        borderHeight = BOARDHEIGHT * BOXSIZE

        if player == 2:
            boardX = XMARGIN + BOARDGAP + borderWidth
            boardY = TOPMARGIN 
        else:
            boardX = XMARGIN
            boardY = TOPMARGIN

        pygame.draw.rect(windowSurface,BORDERCOLOR,(boardX - 3,boardY - 3, borderWidth + 15, borderHeight + 3),3)
        pygame.draw.rect(windowSurface,BOARDBGCOLOR,(boardX, boardY , borderWidth + 9, borderHeight - 3))

        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                if board[x][y] != BLANK:
                    drawBoardBox(0, 0, level, boardX + x * (BOXSIZE + BOXGAP), boardY  + y * (BOXSIZE + BOXGAP))
                    
def drawScoreAndLevel(score, level, player = 1):
    if player == 2:
        scoreX = (WINDOWWIDTH - BOXSIZE * BOARDWIDTH - BOARDGAP ) / 2
        scoreY = 10
        levelX = (WINDOWWIDTH - BOXSIZE * BOARDWIDTH - BOARDGAP ) / 2
        levelY = 50
    else:
        scoreX = (WINDOWWIDTH + BOXSIZE * BOARDWIDTH + BOARDGAP ) / 2
        scoreY = 10
        levelX = (WINDOWWIDTH + BOXSIZE * BOARDWIDTH + BOARDGAP ) / 2
        levelY = 50
    scoreSurf = BASICFONT.render('Score : %d' %score, 1,WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.center = (scoreX, scoreY)
    windowSurface.blit(scoreSurf, scoreRect)

    levelSurf = BASICFONT.render('Level : %d' %level, 1,WHITE)
    levelRect = levelSurf.get_rect()
    levelRect.center = (levelX , levelY)
    windowSurface.blit(levelSurf, levelRect)

def drawNextPiece(piece, player = 1, coop = False):
    if coop and player == 1:
        boxX = (WINDOWWIDTH - COOPBOARDWIDTH * BOXSIZE) / 2 - 150
        boxY = 100
    elif coop and player == 2:
        boxX = (WINDOWWIDTH + COOPBOARDWIDTH * BOXSIZE) / 2  + 150 - BOXSIZE * TEMPLATEWIDTH
        boxY = 100        
    elif player == 1:
        boxX = WINDOWWIDTH / 2 - 150
        boxY = 100
    elif player == 2:
        boxX = WINDOWWIDTH / 2 + 150 - BOXSIZE * TEMPLATEWIDTH
        boxY = 100
        
    pygame.draw.rect(windowSurface,BOARDBGCOLOR,(boxX, boxY, BOXSIZE * TEMPLATEWIDTH, BOXSIZE * TEMPLATEHEIGHT))
    pygame.draw.rect(windowSurface,BORDERCOLOR,(boxX - 3, boxY - 3, BOXSIZE * TEMPLATEWIDTH + 6, BOXSIZE * TEMPLATEHEIGHT + 6),4)
    drawPiece(piece, 1, boxX, boxY)
        
def drawText(text, pixelx = None, pixely = None, FONT = None, color = 4): # 4 la SILVER trong LEVELCOLOR2
    if pixelx == None and pixely == None: #mac dinh ve o giua man hinh
        pixelx = int(WINDOWWIDTH / 2)
        pixely = int(WINDOWHEIGHT / 2)
    if FONT == None:
        FONT = pygame.font.SysFont(None, 100)

    textSurf = FONT.render(text, 1, LEVELCOLOR2[color])
    textRect = textSurf.get_rect()
    textRect.centerx, textRect.centery = pixelx, pixely
    windowSurface.blit(textSurf, textRect)

    textSurf2 = FONT.render(text, 1, LEVELCOLOR[color])
    textRect2 = textSurf.get_rect()
    textRect2.centerx, textRect2.centery = pixelx - 3, pixely - 3
    windowSurface.blit(textSurf2, textRect2)


##################################################### VE LOGOBOARD CHO CHE DO ONEPLAYERMODE
    
def drawLogoBoard(logoBoard):
    LOGOBOARDCOLOR = BLACK
    LOGOBORDERBOARDCOLOR = AQUA
    BOXLOGOSIZE = 5
    BOXLOGOGAP = 1
    LOGOGAP = (int(WINDOWWIDTH - BOARDGAP - XMARGIN) / 2 - (BOARDWIDTH * BOXSIZE))

    logoX = int((WINDOWWIDTH + BOARDGAP)/ 2)
    logoY = WINDOWHEIGHT - TEMPLATEHEIGHT * BOXLOGOSIZE - 5

    scoreX = int((WINDOWWIDTH + BOARDGAP)/ 2) + 2 * (BOXLOGOSIZE + BOXLOGOGAP)
    scoreY = WINDOWHEIGHT - TEMPLATEHEIGHT * BOXLOGOSIZE - 15 

    color = 0

    pygame.draw.rect(windowSurface, LOGOBOARDCOLOR, (logoX - 12, TOPMARGIN, BOARDWIDTH * BOXSIZE, BOARDHEIGHT * BOXSIZE))
    pygame.draw.rect(windowSurface, LOGOBORDERBOARDCOLOR, (logoX - 12 - 3, TOPMARGIN - 3, BOARDWIDTH * BOXSIZE + 6, BOARDHEIGHT * BOXSIZE + 3), 3)
    for shape in PIECES:

        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if PIECES[shape][0][y][x] != BLANK:
                    box = pygame.Rect(logoX + x * (BOXLOGOSIZE + BOXLOGOGAP), logoY + y * (BOXLOGOSIZE + BOXLOGOGAP) , BOXLOGOSIZE, BOXLOGOSIZE)
                    pygame.draw.rect(windowSurface, COLOR[color], box)
        if logoBoard[shape] > 340: #ve toi da 340 pixel
            logoBoard[shape] = 340
        score = pygame.Rect(scoreX, scoreY - logoBoard[shape], BOXLOGOSIZE, logoBoard[shape])
        pygame.draw.rect(windowSurface, COLOR[color], score)

        logoX += LOGOGAP
        scoreX += BOXLOGOSIZE * TEMPLATEWIDTH
        color += 1

def getNewLogoBoard():
    board = {}
    for piece in list(PIECES.keys()):
        board.update({piece : 1})
    return board

##################################################### VE LOGOBOARD CHO CHE DO ONEPLAYERMODE

if __name__ == '__main__':
    main()

    
