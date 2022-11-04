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

class Stars:
    amount = 30
    move_speed = 4
    def __init__(self):
        self.star_layer = []
        for layer in range(3):
            self.stars_list = []
            for a in range(self.amount):
                x = random.randint(0, screen_size[0])
                y = random.randint(0, screen_size[1])
                self.stars_list.append((x, y))
            self.star_layer.append(self.stars_list)
    def move(self):
        new_star_layer = []
        counter = 0
        for layer in self.star_layer:
            counter += 1
            new_cord = []
            for cord in layer:
                x = cord[0]
                y = cord[1] + self.move_speed * 2 ** counter
                if y > screen_size[1]:
                    y -= screen_size[1]
                new_cord.append((x, y))
            new_star_layer.append(new_cord)
        self.star_layer = new_star_layer

    def draw(self):
        for layer in self.star_layer:
            for star_cord in layer:
                pygame.draw.circle(screen, (255, 255, 255), star_cord, 1, 1)

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
background = Stars()

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

    background.move()
    background.draw()
    player.move(move)
    player.draw()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()