import pygame
from time import sleep
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
pygame.init()
display = (800,600)
screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
clock = pygame.time.Clock()
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill((0, 171,255))
 # code of program for nican of Kian (: 
 #-------------------------------------------------
    print("Kian Is Best!!!!!")

    
 #--------------------------------------------------
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
