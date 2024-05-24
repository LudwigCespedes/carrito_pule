import sys
import pygame
from car import Car

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
CARSIZE = 40 # size of CAR height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels
BOARDWIDTH = 6 # number of columns of icons
BOARDHEIGHT = 6 # number of rows of icons

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

CAR1 = 'donut'
CAR2 = 'square'
CAR3 = 'diamond'
CAR4 = 'lines'
CAR5 = Car("5",2,"V",1,)


ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLCAR = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT,\
      "Board is too big for the number of shapes/colors defined."