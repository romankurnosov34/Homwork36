import pygame as pg
from pygame.locals import *
import math

text_map = [
    'WWWWWWWWWWWW',
    'W..........W',
    'W..........W',
    'W....WW....W',
    'W..........W',
    'W....WW....W',
    'W..........W',
    'WWWWWWWWWWWW',
]

TILE = 100

world_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
SIZE = W, H = 1200, 800
HALF_W, HALF_H = W //2, H // 2
FPS = 60
WHITE = 'white'
RED = 'red'
BLACK = 'black'
BLUE = 'blue'
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)

FOV = math.pi / 3
HALF_FOV = FOV / 2
MAX_RAYS = 50
MAX_DEPTH = 800
DELTA_ANGLE = FOV / MAX_RAYS

DIST = MAX_RAYS / (2 * math.tan(HALF_FOV))

PROJ_COEF = 3 * DIST * TILE

SCALE = W // MAX_RAYS

player_pos = [HALF_W, HALF_H]
player_angle = 0
player_speed = 2

class Player:
    def __init__(self, pos, angle):
        self.x = pos[0]
        self.y = pos[1]
        self.angle = angle

    @property
    def pos(self):
        return self.x, self.y

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys_pressed[K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys_pressed[K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys_pressed[K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys_pressed[K_LEFT]:
            self.angle -= 0.02
        if keys_pressed[K_RIGHT]:
            self.angle += 0.02

def raycating(screen, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xcopy, ycopy = player_pos
    for ray in range(MAX_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xcopy + depth * cos_a
            y = ycopy + depth * sin_a
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_h = PROJ_COEF / depth
                c = 255 / (1 + depth * depth * 1e-4)
                color = (c, c, c)
                pg.draw.rect(screen, color,
                             (ray * SCALE, HALF_H - proj_h // 2, SCALE, proj_h))
                break
        cur_angle += DELTA_ANGLE

pg.init()

screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()
player = Player(player_pos, player_angle)

running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    player.move()
    screen.fill(BLACK)
    raycating(screen, player.pos, player.angle)
    pg.display.update()
    clock.tick(FPS)
pg.quit()