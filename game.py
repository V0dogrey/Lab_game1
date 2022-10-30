import pygame
from pygame.draw import *
import random
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 800))
'''set screen resolution'''
play_score = 0

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

circle_obj = []

def create_obj():
    return

def move_obj():
    return

def upd_obj():
    if len(objects_list) < 1:
        create_obj()
    return

def draw_objects(objl):
    return

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    '''main program work'''
    clock.tick(FPS)
    upd_obj(objects_list)
    for event in pygame.event.get():
        '''proc input'''
        if event.type == pygame.QUIT:
            finished = True

    draw_objects(objects_list)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()