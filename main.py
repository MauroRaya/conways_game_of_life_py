import pygame
import sys

pygame.init()
pygame.display.set_caption('Conways Game of Life')

BACKGROUND_COLOR = (100, 100, 100) # Black
GRID_COLOR       = (255, 255, 255) # White
POPULATION_COLOR = (30, 30, 255)   # Blue

ROWS = 15
GRID = [[BACKGROUND_COLOR for _ in range(ROWS)] for _ in range(ROWS)]

WIDTH  = 600
HEIGHT = 600

CELL_WIDTH  = WIDTH  / ROWS
CELL_HEIGHT = HEIGHT / ROWS

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_grid(surface, rows, cell_width, cell_height):
    global GRID

    for row in range(rows):
        for col in range(rows):
            rect = (row * cell_width, col * cell_height, cell_width, cell_height)
            pygame.draw.rect(surface, GRID[row][col], rect) # Draws the color of the cell
            pygame.draw.rect(surface, GRID_COLOR, rect, 1)  # Draws the border



def handle_mouse_click(pos):
    global POPULATION_COLOR
    x, y = pos

    try:
        row = int(x // CELL_WIDTH)
        col = int(y // CELL_HEIGHT)

        GRID[row][col] = POPULATION_COLOR

    except ValueError:
        print('Error: converting into an integer coordinate')
        pygame.quit()
        sys.exit()

    except IndexError:
        print('Error: grid index out of range')
        pygame.quit()
        sys.exit()


def main():
    while True:
        draw_grid(SCREEN, ROWS, CELL_WIDTH, CELL_HEIGHT)

        for event in pygame.event.get():
            # Prevents window from crashing... no clue why
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(event.pos)

        pygame.display.update()


if __name__ == '__main__':
    main()