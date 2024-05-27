import pygame as pg
from pygame.locals import *
from pygame.sprite import Sprite
import random

SIZE = 640, 320


class Particle(Sprite):
    def __init__(self, startx, starty, col):
        super().__init__()
        self.image = pg.Surface((2, 2))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.x = startx
        self.rect.y = random.randint(0, starty)
        self.sx = startx
        self.sy = starty

    def move(self):
        if self.rect.y < 0:
            self.rect.x = self.sx
            self.rect.y = self.sy
        else:
            self.rect.y -= 1
            self.rect.x += random.randint(-2, 2)


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = 100


pg.init()
screen = pg.display.set_mode(SIZE, 0, 32)
pg.display.set_caption('Light')
light = pg.image.load('light.png')
light = pg.transform.scale(light, (200, 100))
player = Player()
particles = [Particle(515, SIZE[1], (0, 0, 0 if i % 2 == 0 else (128, 128, 128))) for i in range(300)]
light_on = False

running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_f:
                light_on ^= True  # Toggle light state
            elif event.key == K_a:
                player.rect.x -= 5
            elif event.key == K_d:
                player.rect.x += 5

    screen.fill((255, 255, 255))

    for particle in particles:
        particle.move()
        screen.blit(particle.image, particle.rect.topleft)

    if light_on:
        light_filter_surf = pg.Surface(SIZE)
        light_filter_surf.fill((255, 255, 255))
        light_filter_surf.blit(light, (player.rect.x - light.get_width() // 2, player.rect.y - light.get_height() // 2))
        screen.blit(light_filter_surf, (0, 0), special_flags=BLEND_RGB_ADD)

    screen.blit(player.image, player.rect)

    pg.display.flip()
    clock.tick(50)

pg.quit()