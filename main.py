import pygame
import sys

pygame.init()
pygame.display.set_caption('Conway\'s Game of Life')

# Colors
BACKGROUND_COLOR = (100, 100, 100) # Black
GRID_COLOR       = (255, 255, 255) # White
ALIVE_COLOR      = (30, 30, 255)   # Blue

# Grid settings
GRID_SIZE          = 15
current_grid       = [[BACKGROUND_COLOR for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
simulation_running = False

# Screen settings
WIDTH       = 600
HEIGHT      = 600
CELL_WIDTH  = WIDTH  / GRID_SIZE
CELL_HEIGHT = HEIGHT / GRID_SIZE
screen      = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_grid(surface):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = (row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(surface, current_grid[row][col], rect) # Cell color
            pygame.draw.rect(surface, GRID_COLOR, rect, 1)          # Grid border


def toggle_cell_state(pos):
    x, y = pos

    row = int(x // CELL_WIDTH)
    col = int(y // CELL_HEIGHT)

    current_grid[row][col] = ALIVE_COLOR if current_grid[row][col] == BACKGROUND_COLOR else BACKGROUND_COLOR


def count_neighbors(row, col) -> int:
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            r, c = row + i, col + j
            
            if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and current_grid[r][c] == ALIVE_COLOR:
                count += 1
    
    return count


def update_generation():
    global current_grid
    next_grid = [[BACKGROUND_COLOR for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            neighbors = count_neighbors(row, col)

            if neighbors == 3 or (neighbors == 2 and current_grid[row][col] == ALIVE_COLOR):
                next_grid[row][col] = ALIVE_COLOR
            else:
                next_grid[row][col] = BACKGROUND_COLOR
    
    current_grid = next_grid
            

def main():
    global simulation_running
    clock = pygame.time.Clock()

    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_grid(screen)

        if simulation_running:
            update_generation()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                toggle_cell_state(event.pos)

            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_0]:
                    simulation_running = not simulation_running

        pygame.display.update()
        clock.tick(8)


if __name__ == '__main__':
    main()