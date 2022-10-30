import pygame
import math
from pygame.draw import *
from random import *
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

def create_circle():
    '''Add to objects list circle object with:
    [0]: type = 'circle'
    [1]: Color
    [2]: start coordinates (x, y)
    [3]: radius if circle
    [4]: movespeed on coords (x, y)
    '''
    circle_obj = []
    circle_move_speed = 3

    circle_obj.append('circle')
    '''[0]'''
    color = COLORS[randint(0, len(COLORS)) - 1]
    circle_obj.append((color))
    '''[1]'''
    x = randint(100, 700)
    y = randint(100, 500)
    circle_obj.append((x, y))
    '''[2]'''
    r = randint(30, 50)
    circle_obj.append(r)
    '''[3]'''
    x_speed = circle_move_speed * randint(-5, 5)
    y_speed = circle_move_speed * randint(-5, 5)
    circle_obj.append((x_speed, y_speed))
    '''[4]'''
    objects_list.append(circle_obj)

create_circle()

def move_obj():
    for obj in objects_list:
        x = obj[2][0] + obj[4][0]
        y = obj[2][1] + obj[4][1]
        obj[2] = (x, y)

def upd_obj():
    return

def draw_objects():
    for obj in objects_list:
        if obj[0] == 'circle':
            circle(screen, obj[1], obj[2], obj[3])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    '''main program work'''
    clock.tick(FPS)
    #upd_obj(objects_list)
    for event in pygame.event.get():
        '''proc input'''
        if event.type == pygame.QUIT:
            finished = True
    move_obj()
    draw_objects()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()