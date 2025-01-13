import pygame
import sys

pygame.init()
pygame.display.set_caption('Conways Game of Life')

WIDTH  = 500
HEIGHT = 500
ROWS   = 20
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (255, 255, 255) # Black


def draw_grid(surface, background_color, rows, width, cell_width, cell_height):
    x = 0
    y = 0

    for _ in range(rows):
        x += cell_width
        y += cell_height

        pygame.draw.line(surface, background_color, (x, 0), (x, width))
        pygame.draw.line(surface, background_color, (0, y), (width, y))


def main():
    while True:
        draw_grid(SCREEN, BACKGROUND_COLOR, ROWS, WIDTH, WIDTH/ROWS, HEIGHT/ROWS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()