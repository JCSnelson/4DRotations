import pygame
from pygame.locals import *
import numpy as np
import math
from time import sleep
#function to apply matrix transformations to points
def multiply(m1,m2):
    columns = len(m2[0])
    thing = len(m2)
    output = [0 for x in range(columns)]
    for y in range(columns):
        value = 0
        for z in range(thing):
            value += m1[z]*m2[z][y]
        output[y] = value
    return output

#initialize game         
pygame.init()
screen = pygame.display.set_mode((800,450))


#points of the tesseract
points = [
        [50, 50, 50, 50], [ -50, 50, 50, 50], [-50,  -50,   50, 50], [50, -50,  50, 50],[50, 50,   -50, 50], [ -50, 50,   -50, 50], [-50,  -50,   -50, 50], [50, -50,  -50, 50],
        [50, 50, 50, -50], [ -50, 50, 50, -50], [-50,  -50,   50, -50], [50, -50,  50, -50],[50, 50,   -50, -50], [ -50, 50,   -50, -50], [-50,  -50,   -50, -50], [50, -50,  -50, -50]
    ]


def drawTesseract(points):
    #outer
    pygame.draw.line(screen,(255,0,0),p[0],p[1],t)
    pygame.draw.line(screen,(0,0,255),p[1],p[2],t)
    pygame.draw.line(screen,(255,0,0),p[2],p[3],t)
    pygame.draw.line(screen,(0,0,255),p[3],p[0],t)

    pygame.draw.line(screen,(255,0,0),p[4],p[5],t)
    pygame.draw.line(screen,(0,0,255),p[5],p[6],t)
    pygame.draw.line(screen,(255,0,0),p[6],p[7],t)
    pygame.draw.line(screen,(0,0,255),p[7],p[4],t)

    pygame.draw.line(screen,(0,255,0),p[0],p[4],t)
    pygame.draw.line(screen,(0,255,0),p[1],p[5],t)
    pygame.draw.line(screen,(0,255,0),p[2],p[6],t)
    pygame.draw.line(screen,(0,255,0),p[3],p[7],t)

    #inner
    pygame.draw.line(screen,(255,0,0),p[0+8],p[1+8],t)
    pygame.draw.line(screen,(0,0,255),p[1+8],p[2+8],t)
    pygame.draw.line(screen,(255,0,0),p[2+8],p[3+8],t)
    pygame.draw.line(screen,(0,0,255),p[3+8],p[0+8],t)

    pygame.draw.line(screen,(255,0,0),p[4+8],p[5+8],t)
    pygame.draw.line(screen,(0,0,255),p[5+8],p[6+8],t)
    pygame.draw.line(screen,(255,0,0),p[6+8],p[7+8],t)
    pygame.draw.line(screen,(0,0,255),p[7+8],p[4+8],t)

    pygame.draw.line(screen,(0,255,0),p[0+8],p[4+8],t)
    pygame.draw.line(screen,(0,255,0),p[1+8],p[5+8],t)
    pygame.draw.line(screen,(0,255,0),p[2+8],p[6+8],t)
    pygame.draw.line(screen,(0,255,0),p[3+8],p[7+8],t)

    #joining
    pygame.draw.line(screen,(0,0,0),p[0],p[8],t)
    pygame.draw.line(screen,(0,0,0),p[1],p[9],t)
    pygame.draw.line(screen,(0,0,0),p[2],p[10],t)
    pygame.draw.line(screen,(0,0,0),p[3],p[11],t)
    pygame.draw.line(screen,(0,0,0),p[4],p[12],t)
    pygame.draw.line(screen,(0,0,0),p[5],p[13],t)
    pygame.draw.line(screen,(0,0,0),p[6],p[14],t)
    pygame.draw.line(screen,(0,0,0),p[7],p[15],t)


    
#scale factor for enlarging and shrinking
sf = 5

#rate of change of enlargement
rateofenlargement = 0
def rotationXY(angle):
    angle = angle*math.pi/180
    s = math.sin(angle)#
    c = math.cos(angle)
    matrix = [
        [c,-s,0,0],
        [s,c,0,0],
        [0,0,1,0],
        [0,0,0,1]
    ]
    return matrix

def rotationXZ(angle):
    angle = angle*math.pi/180
    s = math.sin(angle)#
    c = math.cos(angle)
    matrix = [
        [c,0,-s,0],
        [0,1,0,0],
        [s,0,c,0],
        [0,0,0,1]
    ]
    return matrix

def rotationXW(angle):
    angle = angle*math.pi/180
    s = math.sin(angle)#
    c = math.cos(angle)
    matrix = [
        [c,0,0,-s],
        [0,0,0,0],
        [0,0,1,0],
        [s,0,0,c]
    ]
    return matrix

def rotationYZ(angle):
    angle = angle*math.pi/180
    s = math.sin(angle)#
    c = math.cos(angle)
    matrix = [
        [1,0,0,0],
        [0,c,-s,0],
        [0,s,c,0],
        [0,0,0,1]
    ]
    return matrix

def rotationYW(angle):
    angle = angle*math.pi/180
    s = math.sin(angle)#
    c = math.cos(angle)
    matrix = [
        [1,0,0,0],
        [0,c,0,-s],
        [0,0,1,0],
        [0,s,0,c]
    ]
    return matrix

def rotationZW(angle):
    angle = angle*math.pi/180
    s = math.sin(angle)#
    c = math.cos(angle)
    matrix = [
        [1,0,0,0],
        [0,1,-0,0],
        [0,0,c,-s],
        [0,0,s,c]
    ]
    return matrix

I = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

#declares rotation amounts and gets matrices for them
rotationxy = rotationXY(0.1)
rotationxz = rotationXZ(0.11)
rotationxw = rotationXW(0.12)
rotationyz = rotationYZ(0.13)
rotationyw = rotationYW(0.14)
rotationzw = rotationZW(0.15)
distance = 2

#gets the width and height of the display
width, height = pygame.display.get_surface().get_size()

#declares line thickness
t = 2

running = True
while running:
    #resets the screen before drawing on the frame
    screen.fill((255,255,255))

    #exit conditions
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False


    #rotating the points using the 3 rotation matrices
    rotatedpoints = []
    for x in points:
        rotated  = multiply(multiply(multiply(multiply(multiply(multiply(x,rotationzw),I),rotationyz),I),rotationxz),I)
        rotatedpoints.append(rotated)
    points = rotatedpoints

    #changes scale factor in order to shrink and grow with a min and max scale factor
    if sf == 1:
        rateofenlargement = 0
    elif sf == 5:
        rateofenlargement = 0
    sf = round(sf + rateofenlargement,2)


    #giving the points perspective projection onto the 2D plane
    perspective = True
    if perspective:
        projectedpoints3 = []
        for x in points:
            w = 1/(distance - x[3]/100)
            projectedpoints3.append([x[0]*w,x[1]*w,x[2]*w,0])
        projectedpoints2 = []
        for x in projectedpoints3:
            z = 1 / (distance - (x[2]/100))
            projectedpoints2.append([x[0]*z*sf,x[1]*z*sf,0,0])
    else:
        projectedpoints2 = points

    #making sure the points are centered in the screen
    p = []
    for x in projectedpoints2:
        transformed = x
        p.append([transformed[0]+(width/2),transformed[1]+(height/2)])
    
    #drawing lines
    drawTesseract(p)

    pygame.display.update()
    sleep(0.01)