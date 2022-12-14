import pygame
import math
from pygame.draw import *
from random import *

pygame.init()

FPS = 30
screen_resolution = (1200, 800)
screen = pygame.display.set_mode(screen_resolution)
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

circle_move_speed = 30
romb_move_speed = 40
objects_list = []


def set_speed(obj_speed):
    angle = math.pi * 2 * random()
    speed = (math.sin(angle) * obj_speed, math.cos(angle) * obj_speed)
    return speed


def create_circle():
    """Add to objects list circle object with:
    [0]: type = 'circle'
    [1]: Color
    [2]: start coordinates (x, y)
    [3]: radius if circle
    [4]: movespeed on coords (x, y)
    """
    circle_obj = []

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
    circle_obj.append(set_speed(circle_move_speed))
    '''[4]'''
    objects_list.append(circle_obj)

def create_romb():
    """Add to objects list circle object with:
        [0]: type = 'romb'
        [1]: Color
        [2]: start coordinates (x, y)
        [3]: romb radius
        [4]: movespeed on coords (x, y)
        """
    romb_obj = []

    romb_obj.append('romb')
    '''[0]'''
    color = COLORS[randint(0, len(COLORS)) - 1]
    romb_obj.append((color))
    '''[1]'''
    x = randint(100, 700)
    y = randint(100, 500)
    romb_obj.append((x, y))
    '''[2]'''
    r = randint(30, 50)
    romb_obj.append(r)
    '''[3]'''
    romb_obj.append(set_speed(romb_move_speed))
    '''[4]'''
    objects_list.append(romb_obj)

create_circle()
create_circle()
create_romb()


def move_obj():
    for obj in objects_list:

        if obj[2][0] - obj[3] < 0:
            get_speed = set_speed(circle_move_speed)
            if get_speed[0] < 0:
                get_speed = get_speed[0] * -1, get_speed[1]
            obj[4] = get_speed
        if obj[2][0] + obj[3] > screen_resolution[0]:
            get_speed = set_speed(circle_move_speed)
            if get_speed[0] > 0:
                get_speed = get_speed[0] * -1, get_speed[1]
            obj[4] = get_speed
        if obj[2][1] - obj[3] < 0:
            get_speed = set_speed(circle_move_speed)
            if get_speed[1] < 0:
                get_speed = get_speed[0], get_speed[1] * -1
            obj[4] = get_speed
        if obj[2][1] + obj[3] > screen_resolution[1]:
            get_speed = set_speed(circle_move_speed)
            if get_speed[1] > 0:
                get_speed = get_speed[0], get_speed[1] * -1
            obj[4] = get_speed

        x = obj[2][0] + obj[4][0]
        y = obj[2][1] + obj[4][1]
        obj[2] = (x, y)


def draw_objects():
    for obj in objects_list:
        if obj[0] == 'circle':
            circle(screen, obj[1], obj[2], obj[3])
        if obj[0] == 'romb':
            dot1 = [obj[2][0] + obj[3], obj[2][1]]
            dot2 = [obj[2][0], obj[2][1] + obj[3]]
            dot3 = [obj[2][0] - obj[3], obj[2][1]]
            dot4 = [obj[2][0], obj[2][1] - obj[3]]
            polygon(screen, obj[1], [dot1, dot2, dot3, dot4])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    '''main program work'''
    clock.tick(FPS)
    move_obj()
    for event in pygame.event.get():
        '''procesing input'''
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in objects_list:
                dis_to_obj_x = obj[2][0] - event.pos[0]
                dis_to_obj_y = obj[2][1] - event.pos[1]
                if obj[0] == 'circle':
                    dis_to_obj = dis_to_obj_x ** 2 + dis_to_obj_y ** 2
                    if dis_to_obj < obj[3] ** 2:
                        create_circle()
                        objects_list.remove(obj)
                        play_score += 100
                elif obj[0] == 'romb':
                    dis_to_obj = abs(dis_to_obj_x) + abs(dis_to_obj_y)
                    if dis_to_obj < obj[3]:
                        create_romb()
                        objects_list.remove(obj)
                        play_score += 139


    draw_objects()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

print(play_score)
