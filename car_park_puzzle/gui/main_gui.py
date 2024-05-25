
import sys
import pygame
from ..car import Car
from ..game_board import Board
from pygame.locals import *



FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
CARSIZE = 40 # size of CAR height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels
BOARDWIDTH = 10 # number of columns of icons
BOARDHEIGHT = 7 # number of rows of icons

assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0\
    ,'Board needs to have an even number of boxes for pairs of matches.'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (CARSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (CARSIZE + GAPSIZE))) / 2)

GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

CAR1 = Car('1', 2, 'H', 2, 2)
CAR2 = Car('2', 2, 'H', 3, 3)
CAR3 = Car('3', 3, 'V', 0, 0)
CAR4 = Car('4', 2, 'H', 0, 3)
CAR5 = Car('5', 2, 'V', 3, 1)


ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLCAR = (CAR1, CAR2, CAR3, CAR4, CAR5)
assert len(ALLCOLORS) * len(ALLCAR) * 2 >= BOARDWIDTH * BOARDHEIGHT,\
      "Board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event    
    pygame.display.set_caption("Carrito Pule")
    
    mainBoard=Board(BOARDHEIGHT,BOARDWIDTH).board
    print(mainBoard)
    DISPLAYSURF.fill(BGCOLOR)
    
    while True:
        mouseClicked = False
        DISPLAYSURF.fill(BGCOLOR) # drawing the window
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True   

