# import pygame as pg
# from pygame.locals import *
# from pygame.sprite import Sprite
#
# SIZE = 640, 320
#
# class Player(Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pg.image.load('player.png')
#         self.rect = self.image.get_rect()
#         self.rect.centerx = 100
#         self.rect.bottom = 100
#
# pg.init()
# screen = pg.display.set_mode(SIZE, 0, 32)
# pg.display.set_caption('Light 3')
#
# light = pg.image.load('light.png')
# light = pg.transform.scale(light, (200, 100))
# player = Player()
#
# light_on = False
#
# running = True
# while running:
#     for event in pg.event.get():
#         if event.type == QUIT:
#             running = False
#         if event.type == KEYDOWN:
#             if event.key == K_f:
#                 light_on = True
#             if event.key == K_a:
#                 player.rect.x -= 5
#             if event.key == K_d:
#                 player.rect.x += 5
#         if event.type == KEYUP:
#             if event.key == K_f:
#                 light_on = False
#     screen.fill('black')
#     light_filter = pg.Surface(SIZE)
#     light_filter.fill('white')
#     if light_on:
#         light_filter.blit(light, (player.rect.x, player.rect.y))
#     screen.blit(light_filter, (0, 0),
#                 special_flags=BLEND_RGB_ADD)
#     screen.blit(player.image, player.rect)
#     pg.display.flip()
#
# pg.quit()


import pygame as pg
from pygame.locals import *
from pygame.sprite import Sprite

SIZE = 640, 320

class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = 100

pg.init()
screen = pg.display.set_mode(SIZE, 0, 32)
pg.display.set_caption('Light 3')

light = pg.image.load('light.png')
light = pg.transform.scale(light, (200, 100))
player = Player()

light_on = False

running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_f:
                light_on = True
            if event.key == K_a:
                player.rect.x -= 5
            if event.key == K_d:
                player.rect.x += 5
        if event.type == KEYUP:
            if event.key == K_f:
                light_on = False
    screen.fill('black')
    light_filter = pg.Surface(SIZE)
    light_filter.fill('white')
    if light_on:
        light_filter.blit(light, (player.rect.x, player.rect.y))
    screen.blit(light_filter, (0, 0),
                special_flags=BLEND_RGB_ADD)
    screen.blit(player.image, player.rect)
    pg.display.flip()

pg.quit()


