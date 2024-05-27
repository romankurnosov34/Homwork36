import pygame as pg
from pygame.locals import *
from random import randint

SIZE = 500, 500
BACKGROUND = 'black'
pg.init()

def light_surface(radius, color):
    surf = pg.Surface((radius * 2, radius * 2))
    pg.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey('black')
    return surf

screen = pg.display.set_mode(SIZE, 0, 32)
pg.display.set_caption('Light 1')
clock = pg.time.Clock()

particles = []

running = True
while running:
    screen.fill(BACKGROUND)
    x, y = pg.mouse.get_pos()
    particles.append(
        [[x, y], [randint(0, 20) / 10 - 1, -5],
                 randint(6, 11)
        ]
    )
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.15

        if particle[2] <= 0:
            particles.remove(particle)

        radius = particle[2] * 2
        xParticle = (particle[0][0] - radius)
        yParticle = (particle[0][1] - radius)
        center = [xParticle, yParticle]
        # pg.draw.circle(screen, 'white', center, radius)
        light = light_surface(radius, (20, 60, 60))
        screen.blit(light, center, special_flags=BLEND_RGB_ADD)

    for event in pg.event.get():
        if event.type == QUIT or event.type == KEYDOWN and \
                event.key == K_ESCAPE:
            running = False

    pg.display.update()
    clock.tick(60)

pg.quit()

# import pygame as pg
# from pygame.locals import *
# from random import randint
#
# SIZE = 500, 500
# BACKGROUND = 'black'
# pg.init()
#
# def light_surface(radius, color):
#     surf = pg.Surface((radius * 2, radius * 2))
#     pg.draw.circle(surf, color, (radius, radius), radius)
#     surf.set_colorkey('black')
#     return surf
#
# screen = pg.display.set_mode(SIZE, 0, 32)
# pg.display.set_caption('Light 1')
# clock = pg.time.Clock()
#
# particles = []
#
# running = True
# while running:
#     screen.fill(BACKGROUND)
#     x, y = pg.mouse.get_pos()
#     particles.append(
#         [[x, y], [randint(0, 20) / 10 - 1, -5],
#                  randint(6, 11)
#         ]
#     )
#     for particle in particles:
#         particle[0][0] += particle[1][0]
#         particle[0][1] += particle[1][1]
#         particle[2] -= 0.1
#         particle[1][1] += 0.15
#
#         if particle[2] <= 0:
#             particles.remove(particle)
#
#         radius = particle[2] * 2
#         xParticle = (particle[0][0] - radius)
#         yParticle = (particle[0][1] - radius)
#         center = [xParticle, yParticle]
#         # pg.draw.circle(screen, 'white', center, radius)
#         light = light_surface(radius, (20, 60, 60))
#         screen.blit(light, center, special_flags=BLEND_RGB_ADD)
#
#     for event in pg.event.get():
#         if event.type == QUIT or event.type == KEYDOWN and \
#                 event.key == K_ESCAPE:
#             running = False
#
#     pg.display.update()
#     clock.tick(60)
#
# pg.quit()