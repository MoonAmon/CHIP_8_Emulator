import pygame


class Screen:
    def __init__(self, width, height, scale):
        self.scale = scale
        self.display = [[0 for _ in range(width)] for _ in range(height)]
        pygame.init()
        self.window = pygame.display.set_mode((width * scale, height * scale))

    def set_pixel(self, x, y, value):
        self.display[y][x] = value

    def get_pixel(self, x, y):
        return self.display[y][x]

    def draw(self):
        for y, row in enumerate(self.display):
            for x, pixel in enumerate(row):
                color = (255, 255, 255) if pixel == 1 else (0, 0, 0)
                pygame.draw.rect(self.window, color, pygame.Rect(x * self.scale, y * self.scale, self.scale, self.scale))
        pygame.display.flip()

    def clear(self):
        self.display = [[0 for _ in range(len(self.display[0]))] for _ in range(len(self.display))]
