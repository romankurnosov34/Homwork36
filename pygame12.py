import pygame as pg
from pygame.locals import *
import numpy as np
import math

SIZE = W, H = 800, 600
SCALE = 100
angle = 0

circle_pos = [W//2, H//2]

def connect_points(i, j, points, screen):
    pg.draw.line(screen, 'black',
                 (points[i][0], points[i][1]),
                 (points[j][0], points[j][1]))

pg.init()

screen = pg.display.set_mode(SIZE)
pg.display.set_caption('3D')

points = []
for i in range(-1, 2, 2):
    for j in range(-1, 2, 2):
        for k in range(-1, 2, 2):
            points.append(np.matrix([[i], [j], [k]]))

proj_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

rotation_z = np.matrix([
    [math.cos(angle), -math.sin(angle), 0],
    [math.sin(angle), math.cos(angle), 0],
    [0, 0, 1]
])

rotation_x = np.matrix([
    [1, 0, 0],
    [0, math.cos(angle), -math.sin(angle)],
    [0, math.sin(angle), math.cos(angle)]
])

rotation_y = np.matrix([
    [math.cos(angle), 0, -math.sin(angle)],
    [0, 1, 0],
    [-math.sin(angle), 0, math.cos(angle)]
])

proj_points = [
    [n, n] for n in range(len(points))
]

clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    rotation_z = np.matrix([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ])

    rotation_y = np.matrix([
        [math.cos(angle), 0, -math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ])

    angle += 0.1

    screen.fill('white')

    i = 0
    for point in points:
        rotation_2d = np.dot(rotation_z, point.reshape((3, 1)))

        rotation_2d = np.dot(rotation_y, rotation_2d)

        proj_2d = np.dot(proj_matrix, rotation_2d)

        x0, y0, = circle_pos
        x = x0 + int(proj_2d[0][0] * SCALE)

        y = y0 + int(proj_2d[1][0] * SCALE)

        proj_points[i] = [x, y]

        pg.draw.circle(screen, 'blue', [x, y], 5)

        i += 1

    for p in range(4):
        connect_points(p, (p + 1) % 4, proj_points, screen)
        connect_points(p + 4, ((p + 1) % 4) + 4, proj_points, screen)
        connect_points(p, p + 4, proj_points, screen)

    pg.display.update()
    clock.tick(20)

pg.quit()