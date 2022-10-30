import pygame
from pygame.draw import *
import random
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 800))
'''set screen resolution'''

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
'''make colors list'''

objects_list = []

def draw_objects(objl):
    return

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    '''main program work'''
    clock.tick(FPS)
    for event in pygame.event.get():
        '''proc input'''
        if event.type == pygame.QUIT:
            finished = True

    draw_objects(objects_list)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()