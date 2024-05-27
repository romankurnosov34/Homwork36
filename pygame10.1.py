import pygame as pg
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640, 480

pg.init()

light = pg.image.load('light.png')

screen = pg.display.set_mode(SIZE, 0, 32)
pg.display.set_caption('Light 2')

running = True
while running:
    mouse  =pg.mouse.get_pos()
    pg.mouse.set_visible(False)


    for event in pg.event.get():
        if event.type == QUIT:
            running = False
    else:
        screen.fill('red')
        for x in range(0, WIDTH, 20):
            pg.draw.line(screen, 'green', (x, 0),
                         (x, HEIGHT), 3)
        light_filter = pg.Surface(SIZE)
        light_filter.fill('gray')
        light_filter.blit(light, mouse)
        screen.blit(light_filter, (0, 0),
                    special_flags=BLEND_RGB_ADD)
        pg.display.flip()

pg.quit()
# import pygame
# import pygame as pg
# import random
# from pygame.locals import *
#
# from pygame10 import clock
#
# # Размеры окна игры
# SIZE = WIDTH, HEIGHT = 640, 480
#
# # Инициализация Pygame
# pg.init()
#
# # Загрузка изображения для освещения
# light = pg.image.load('light.png')
#
# # Создание игрового окна
# screen = pg.display.set_mode(SIZE, 0, 32)
# pg.display.set_caption('Light 2')
#
# # Создание персонажа и его начальных координат
# character_x, character_y = WIDTH // 2, HEIGHT // 2
#
# # Создание списка частиц для эффекта освещения
# particles = []
# for _ in range(300):
#     if _ % 2 > 0:
#         col = (0, 0, 0)  # черный цвет для нечетных частиц
#     else:
#         col = (128, 128, 128)  # серый цвет для четных частиц
#     particles.append([515, 500, col])
#
# running = True
#
# while running:
#     # Обработка событий
#     for event in pg.event.get():
#         if event.type == QUIT:
#             running = False
#
#     # Получение текущей позиции мыши
#     mouse_x, mouse_y = pg.mouse.get_pos()
#
#     # Скрытие указателя мыши на экране
#     pg.mouse.set_visible(False)
#
#     # Заполняем экран красным цветом (фон)
#     screen.fill((255, 0, 0))
#
#     # Отрисовка персонажа (прямоугольник в данном случае)
#     character_rect = pg.Rect(character_x - 10, character_y - 10, 20, 20)
#     pg.draw.rect(screen, (255, 255, 255), character_rect)
#
#     # Отрисовка вертикальных линий на экране (зеленого цвета)
#     for x in range(0, WIDTH, 20):
#         pg.draw.line(screen, (0, 255, 0), (x, 0), (x, HEIGHT), 3)
#
#         # Создание поверхности с эффектом освещения и отображение её на экране с использованием "BLEND_RGB_ADD"
#     light_filter = pg.Surface(SIZE)
#     light_filter.fill((128, 128, 128))
#     light_filter.blit(light, (mouse_x - light.get_width() // 2, mouse_y - light.get_height() // 2))
#     screen.blit(light_filter, (0, 0), special_flags=BLEND_RGB_ADD)
#
#     # Отрисовка частиц освещения в виде кругов на экране
#     for p in particles:
#         pygame.draw.circle(screen, p[2], (p[0], p[1]), 2)
#         p[1] -= 1
#         if p[1] < 0:
#             p[1] = 500
#             p[0] = 515 + (random.randint(-2, 3))
#
#         # Обновление содержимого окна и показ его содержимого на экране
#     pg.display.flip()
#
#     # Ограничение количества кадров в секунду до 50 FPS
#     clock.tick(50)
#
# # Завершение работы Pygame при выходе из цикла игры
# pg.quit()