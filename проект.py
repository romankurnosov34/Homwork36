# import tkinter as tk
# import random
#
# Cell_size = 20
# Width, Height = 800, 700
#
#
# class GameOfLife:
#     def __init__(self, master, width, height, cell_size):
#         self.master = master
#         self.width = width
#         self.height = height
#         self.cell_size = cell_size
#         self.rows = self.height // self.cell_size
#         self.cols = self.width // self.cell_size
#         self.cells = [[random.choice([0, 1]) for _ in range(self.cols)] for _ in range(self.rows)]
#
#         self.canvas = tk.Canvas(self.master, width=self.width, height=self.height)
#         self.canvas.pack()
#
#         self.draw_cells()
#
#     def draw_cells(self):
#         self.canvas.delete('cell')
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 if self.cells[row][col]:
#                     x0, y0 = col * self.cell_size, row * self.cell_size
#                     x1, y1 = x0 + self.cell_size, y0 + self.cell_size
#                     self.canvas.create_rectangle(x0, y0, x1, y1, fill="black", tags='cell')
#
#     def update(self):
#         new_cells = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 alive_neighbors = sum([self.cells[i][j] for i in range(row - 1, row + 2) for j in range(col - 1, col + 2)
#                 if(i != row or j != col) and 0 <= i < self.rows and 0 <= j < self.cols])
#                 if self.cells[row][col]:
#                     new_cells[row][col] = 1 if 2 <= alive_neighbors <= 3 else 0
#                 else:
#                     new_cells[row][col] = 1 if alive_neighbors == 3 else 0
#         self.cells = new_cells
#         self.draw_cells()
#         self.master.after(100, self.update)
#
#
# root = tk.Tk()
# game = GameOfLife(root, Width, Height, Cell_size)
# game.update()
# root.mainloop()


# import tkinter as tk
# import random
#
# Cell_size = 20
# Width, Height = 800, 700
#
#
# class GameOfLife:
#     def __init__(self, master, width, height, cell_size):
#         self.master = master
#         self.width = width
#         self.height = height
#         self.cell_size = cell_size
#         self.rows = self.height // self.cell_size
#         self.cols = self.width // self.cell_size
#         self.cells = [[random.choice([0, 1]) for _ in range(self.cols)] for _ in range(self.rows)]
#
#         self.canvas = tk.Canvas(self.master, width=self.width, height=self.height)
#         self.canvas.pack()
#
#         # Создание кнопок для меню
#         self.start_button = tk.Button(self.master, text="Start", command=self.start_simulation)
#         self.start_button.pack(side=tk.LEFT)
#         self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_simulation)
#         self.stop_button.pack(side=tk.LEFT)
#         self.exit_button = tk.Button(self.master, text="Exit", command=self.exit_game)
#         self.exit_button.pack(side=tk.LEFT)
#
#         self.draw_cells()
#
#     def draw_cells(self):
#         self.canvas.delete('cell')
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 if self.cells[row][col]:
#                     x0, y0 = col * self.cell_size, row * self.cell_size
#                     x1, y1 = x0 + self.cell_size, y0 + self.cell_size
#                     self.canvas.create_rectangle(x0, y0, x1, y1, fill="black", tags='cell')
#
#     def update(self):
#         new_cells = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 alive_neighbors = sum([self.cells[i][j] for i in range(row - 1, row + 2) for j in range(col - 1, col + 2)
#                                        if (i != row or j != col) and 0 <= i < self.rows and 0 <= j < self.cols])
#                 if self.cells[row][col]:
#                     new_cells[row][col] = 1 if 2 <= alive_neighbors <= 3 else 0
#                 else:
#                     new_cells[row][col] = 1 if alive_neighbors == 3 else 0
#         self.cells = new_cells
#         self.draw_cells()
#         self.master.after(100, self.update)
#
#     # Методы для управления симуляцией
#     def start_simulation(self):
#         self.update()
#
#     def stop_simulation(self):
#         self.master.after_cancel(self.update)
#
#     def exit_game(self):
#         self.master.destroy()
#
#
# root = tk.Tk()
# game = GameOfLife(root, Width, Height, Cell_size)
# root.mainloop()


import pygame
import random

Cell_size = 10
Width, Height = 800, 700
WHITE = (0, 0, 0)
BLACK = (255, 255, 0)
GREEN = (255, 255, 255)
RED = (255, 255, 255)

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

        self.font = pygame.font.SysFont(None, 30)
        self.start_button_rect = pygame.Rect(10, 10, 100, 50)
        self.stop_button_rect = pygame.Rect(120, 10, 100, 50)
        self.exit_button_rect = pygame.Rect(230, 10, 100, 50)

    def draw_cells(self):
        self.screen.fill(WHITE)
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col]:
                    pygame.draw.rect(self.screen, BLACK, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

    def draw_buttons(self):
        pygame.draw.rect(self.screen, GREEN, self.start_button_rect)
        pygame.draw.rect(self.screen, RED, self.stop_button_rect)
        pygame.draw.rect(self.screen, RED, self.exit_button_rect)

        start_text = self.font.render("Start", True, BLACK)
        stop_text = self.font.render("Stop", True, BLACK)
        exit_text = self.font.render("Exit", True, BLACK)

        self.screen.blit(start_text, (self.start_button_rect.centerx - start_text.get_width() // 2, self.start_button_rect.centery - start_text.get_height() // 2))
        self.screen.blit(stop_text, (self.stop_button_rect.centerx - stop_text.get_width() // 2, self.stop_button_rect.centery - stop_text.get_height() // 2))
        self.screen.blit(exit_text, (self.exit_button_rect.centerx - exit_text.get_width() // 2, self.exit_button_rect.centery - exit_text.get_height() // 2))

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
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.start_button_rect.collidepoint(pos):
                        self.running = True
                    elif self.stop_button_rect.collidepoint(pos):
                        self.running = False
                    elif self.exit_button_rect.collidepoint(pos):
                        pygame.quit()
                        quit()

    def run(self):
        while True:
            self.handle_events()
            if self.running:
                self.update()
            self.draw_cells()
            self.draw_buttons()
            pygame.display.flip()
            self.clock.tick(10)


game = GameOfLife(Width, Height, Cell_size)
game.run()