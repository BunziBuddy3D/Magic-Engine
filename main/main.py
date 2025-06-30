import pygame
from time import sleep
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
pygame.init()
display = (800,600)
screen = pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()
running = True:
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill((0, 171,255))
 # code of program for nican of Kian (: 
 #--------------------------------------------------
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.67, 1.0, 1.0)
    
 #--------------------------------------------------
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
