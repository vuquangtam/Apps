import pygame, sys, time, random
from pygame.locals import *

WINDOWWIDTH = 400
WINDOWHEIGHT = 600
LANDHEIGHT = 100
AIRWIDTH = WINDOWWIDTH
AIRHEIGHT = WINDOWHEIGHT - LANDHEIGHT
BIRDSIZE = 30
TREEGAPSIZE = 200
TREEWIDTH = 70

COLOR = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    global WINDOWSURFACE ,FPSCLOCK
    WINDOWSURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    FPSCLOCK = pygame.time.Clock()
    birdX, birdY = getNewBird()
    trees = []
    timeToAppendTree = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    birdY -= 100
        bird = pygame.Rect(birdX, birdY, BIRDSIZE, BIRDSIZE)
        birdY += 10

        if time.time() - timeToAppendTree > 1:
            TREETOPHEIGHT = random.randint(20,AIRHEIGHT - TREEGAPSIZE - 20)
            TREEBOTTOMHEIGHT = AIRHEIGHT - TREETOPHEIGHT - TREEGAPSIZE
            treeTop = pygame.Rect(AIRWIDTH, 0, TREEWIDTH, TREETOPHEIGHT)
            treeBottom = pygame.Rect(AIRWIDTH, AIRHEIGHT- TREEBOTTOMHEIGHT, TREEWIDTH, TREEBOTTOMHEIGHT)
            trees.append([treeTop,treeBottom])
            timeToAppendTree = time.time()

        
        for obj in trees:
            for tree in obj:
                if bird.colliderect(tree):
                    while True:
                        for event in pygame.event.get(KEYDOWN):
                            if event.key == K_ESCAPE:
                                terminate()
                tree.left -= 10            
        WINDOWSURFACE.fill(BLACK)
        for obj in trees:
            pygame.draw.rect(WINDOWSURFACE, COLOR, obj[0])
            pygame.draw.rect(WINDOWSURFACE, COLOR, obj[1])
        pygame.draw.line(WINDOWSURFACE, COLOR,(0, WINDOWHEIGHT - LANDHEIGHT),(WINDOWWIDTH, WINDOWHEIGHT - LANDHEIGHT), 10)
        pygame.draw.rect(WINDOWSURFACE, COLOR, bird)
        pygame.display.update()
        FPSCLOCK.tick(30)

def terminate():
    pygame.quit()
    sys.exit()

def getNewBird():
    return int(AIRWIDTH / 4), int(AIRHEIGHT / 2)

main()
