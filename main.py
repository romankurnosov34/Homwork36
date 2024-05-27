import pygame
from pygame.locals import *
import random
import sys

Cell_size = 10
Width, Height = 800, 700
WHITE = (0, 0, 0)
BLACK = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 255, 255)
# rd = random.randint(0, 255)
# gr = random.randint(0, 255)
# bl = random.randint(0, 255)
# clr_of_cells = (rd, gr, bl)


class StartScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load('0601c6f8f558643e07bc7cec970268ea.jpg').convert()

        self.font = pygame.font.SysFont(None, 30)
        self.start_button_rect = pygame.Rect(300, 300, 200, 50)
        self.exit_button_rect = pygame.Rect(300, 400, 200, 50)

    def draw_buttons(self):
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, GREEN, self.start_button_rect)
        pygame.draw.rect(self.screen, RED, self.exit_button_rect)

        start_text = self.font.render("Начать", True, BLACK)
        exit_text = self.font.render("Выйти", True, BLACK)

        self.screen.blit(start_text, (self.start_button_rect.centerx - start_text.get_width() // 2, self.start_button_rect.centery - start_text.get_height() // 2))
        self.screen.blit(exit_text, (self.exit_button_rect.centerx - exit_text.get_width() // 2, self.exit_button_rect.centery - exit_text.get_height() // 2))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.start_button_rect.collidepoint(pos):
                        self.start_game()
                    elif self.exit_button_rect.collidepoint(pos):
                        pygame.quit()
                        sys.exit()

    def start_game(self):
        pygame.quit()
        game = GameOfLife(Width, Height, Cell_size)
        game.run()

class GameOfLife:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.rows = self.height // self.cell_size
        self.cols = self.width // self.cell_size
        self.cells = [[random.choice([0, 1]) for _ in range(self.cols)] for _ in range(self.rows)]
        self.running = False

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

    def draw_cells(self):
        self.screen.fill(WHITE)
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col]:
                    pygame.draw.rect(self.screen, BLACK, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

    def update(self):
        new_cells = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                alive_neighbors = sum([self.cells[i][j] for i in range(row - 1, row + 2) for j in range(col - 1, col + 2)
                                       if (i != row or j != col) and 0 <= i < self.rows and 0 <= j < self.cols])
                if self.cells[row][col]:
                    new_cells[row][col] = 1 if 2 <= alive_neighbors <= 3 else 0
                else:
                    new_cells[row][col] = 1 if alive_neighbors == 3 else 0
        self.cells = new_cells

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw_cells()
            pygame.display.flip()
            self.clock.tick(10)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        pygame.quit()
                        sys.exit()

            if not any(cell for row in self.cells for cell in row):
                self.screen.fill(WHITE)
                font = pygame.font.SysFont(None, 50)
                text = font.render("Игра окончена", True, BLACK)
                text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
                self.screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.delay(2000)
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    start_screen = StartScreen(Width, Height)
    while True:
        start_screen.handle_events()
        start_screen.draw_buttons()
        pygame.display.flip()
        start_screen.clock.tick(10)