import pygame
import sys
import time

pygame.init()
pygame.display.set_caption('Conway\'s Game of Life')

BACKGROUND_COLOR = (100, 100, 100) # Black
GRID_COLOR       = (255, 255, 255) # White
POPULATION_COLOR = (30, 30, 255)   # Blue

ROWS = 15
CURRENT_GENERATION = [[BACKGROUND_COLOR for _ in range(ROWS)] for _ in range(ROWS)]
SIMULATION_RUNNING = False

WIDTH  = 600
HEIGHT = 600

CELL_WIDTH  = WIDTH  / ROWS
CELL_HEIGHT = HEIGHT / ROWS

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_grid(surface, rows, cell_width, cell_height):
    for row in range(rows):
        for col in range(rows):
            rect = (row * cell_width, col * cell_height, cell_width, cell_height)
            pygame.draw.rect(surface, CURRENT_GENERATION[row][col], rect) # Draws the color of the cell
            pygame.draw.rect(surface, GRID_COLOR, rect, 1)                # Draws the border


# Mouse click = new cell in the grid
def handle_mouse_click(pos):
    x, y = pos

    row = int(x // CELL_WIDTH)
    col = int(y // CELL_HEIGHT)

    CURRENT_GENERATION[row][col] = POPULATION_COLOR if CURRENT_GENERATION[row][col] == BACKGROUND_COLOR else BACKGROUND_COLOR


def is_cell_filled(grid_cell_value: list[list[tuple]]):
    return grid_cell_value != BACKGROUND_COLOR


def count_neighbors(row, col) -> int:
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            r, c = row + i, col + j
            
            if 0 <= r < ROWS and 0 <= c < ROWS and CURRENT_GENERATION[r][c] == POPULATION_COLOR:
                count += 1
    
    return count


def handle_next_generation():
    global CURRENT_GENERATION
    NEXT_GENERATION = CURRENT_GENERATION

    for row in range(ROWS):
        for col in range(ROWS):
            neighbor_count = count_neighbors(row, col)

            if neighbor_count < 2 or neighbor_count > 3:
                NEXT_GENERATION[row][col] = BACKGROUND_COLOR

            if neighbor_count == 3 and CURRENT_GENERATION[row][col] == BACKGROUND_COLOR:
                NEXT_GENERATION[row][col] = POPULATION_COLOR
    
    CURRENT_GENERATION = NEXT_GENERATION
            


def main():
    global SIMULATION_RUNNING
    clock = pygame.time.Clock()

    while True:
        SCREEN.fill(BACKGROUND_COLOR)
        draw_grid(SCREEN, ROWS, CELL_WIDTH, CELL_HEIGHT)

        if SIMULATION_RUNNING:
            handle_next_generation()

        for event in pygame.event.get():
            # Prevents window from crashing... no clue why
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # Create population cells on the grid cells
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(event.pos)

            # Detect key to toggle simulation
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()

                if key_pressed[pygame.K_0]:
                    SIMULATION_RUNNING = not SIMULATION_RUNNING

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()