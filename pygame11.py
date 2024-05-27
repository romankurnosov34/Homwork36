import pygame as pg
from pygame.locals import *
from random import randint

SIZE = 500, 500
BACKGROUND = 30, 30, 30
FPS = 120
PARTICLE_EVENT = pg.USEREVENT + 1

#----------------------------
class ParticleManager:
    def __init__(self, screen, nyancat):
        self.particles = []
        self.screen = screen
        self.size = 12
        self.nyancat = nyancat

    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x -= 1
                pg.draw.rect(self.screen, particle[1], particle[0])
        self.draw_nyancat()

    def add_particles(self, offset, color):
        pos = list(pg.mouse.get_pos())
        pos[1] += offset
        radius = 10
        rect = pg.Rect(pos[0] - self.size / 2, pos[1] - self.size / 2,
                       self.size, self.size)
        self.particles.append((rect, color))

    def draw_nyancat(self):
        mouse = pg.mouse.get_pos()
        rect = self.nyancat.get_rect(center=mouse)
        self.screen.blit(self.nyancat, rect)

    def delete_particles(self):
        self.particles = [p for p in self.particles if p[0].x > 0]


pg.init()

screen = pg.display.set_mode(SIZE)
pg.display.set_caption('Particles')

pg.time.set_timer(PARTICLE_EVENT, 1)

nyan_cat = pg.image.load('nyan_cat.png').convert_alpha()
nyan_cat = pg.transform.scale(nyan_cat, (200, 100))

particle = ParticleManager(screen, nyan_cat)

clock = pg.time.Clock()
running = True

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == PARTICLE_EVENT:
            particle.add_particles(0, 'red')
            particle.add_particles(8, 'orange')
            particle.add_particles(16, 'yellow')
            particle.add_particles(24, 'green')
            particle.add_particles(32, 'lightblue')
            particle.add_particles(40, 'blue')
            particle.add_particles(48, 'fuchsia')

    screen.fill(BACKGROUND)
    particle.emit()
    pg.display.update()
    clock.tick(FPS)

pg.quit()