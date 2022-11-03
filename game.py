import pygame
from pygame.draw import *
import random
pygame.init()

FPS = 30
screen_size = (1200, 800)
screen = pygame.display.set_mode(screen_size)
'''set screen resolution'''

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (175, 175, 175)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
'''make colors list'''

class Player:
    start_position = (screen_size[0] / 2, screen_size[1] - 150)
    ship_shape = [[25, 15], [0, - 25], [-25, 15], [0, 0]]
    ss = 30
    start_shield_hp = 1
    start_speed = 30

    def __init__(self):
        self.pos = self.start_position
        self.speed = self.start_speed
        self.shield_hp = self.start_shield_hp

    def draw(self):
        dots = []
        for a in self.ship_shape:
            x_pos = a[0] + self.pos[0]
            y_pos = a[1] + self.pos[1]
            dots.append([x_pos, y_pos])
        pygame.draw.polygon(screen, GRAY, dots)

        shield_cords = (self.pos[0] - self.ss, self.pos[1] - self.ss * 2, self.ss * 2, self.ss * 4)
        pygame.draw.ellipse(screen, BLUE, shield_cords, self.shield_hp)

    def move(self, move):
        self.pos = (self.pos[0] + move * self.speed, self.pos[1])

    def fire(self):
        pass

class Bullet:
    pass

class Level:
    def __init__(self):
        objects_list = []
        player = Player
    def objects_move(self):
        pass
    def objects_drow(self):
        pass


pygame.display.update()
clock = pygame.time.Clock()
finished = False

player = Player()

while not finished:
    '''main program work'''
    clock.tick(FPS)
    move = 0
    for event in pygame.event.get():
        '''proc input'''
        if event.type == pygame.QUIT:
            finished = True

    key = pygame.key.get_pressed()
    move = key[pygame.K_d] - key[pygame.K_a]

    player.move(move)
    player.draw()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()