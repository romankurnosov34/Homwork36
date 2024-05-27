import pygame
from pygame.locals import *

pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Вращение изображения")

clock = pygame.time.Clock()

image = pygame.image.load("bird.png")
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True
rotating = False
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                rotating = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:  # Левая кнопка мыши
                rotating = False

    if rotating:
        mouse_pos = pygame.mouse.get_pos()
        angle = -pygame.math.Vector2(mouse_pos[0] - image_rect.centerx, mouse_pos[1] - image_rect.centery).angle_to(
            (1, 0)
        )
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_rect = rotated_image.get_rect(center=image_rect.center)
        screen.blit(rotated_image, rotated_rect)
    else:
        screen.blit(image, image_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()