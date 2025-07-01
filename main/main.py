import pygame
from pygame.locals import *
from time import sleep
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
pygame.init()
display = (800,600)
screen = pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0,0.0, -5)
clock = pygame.time.Clock()
running = True
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill((0, 171,255))
 # code of program for nikan of Kian (: 
 #--------------------------------------------------
    glRotatef(1, 3, 1, 1)
    glClearColor(23/255.0 , 125/255.0 , 144/255.0 , 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    
 #--------------------------------------------------
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
# END Of Code :)
