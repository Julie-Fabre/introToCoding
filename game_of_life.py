"""
Conway's Game of Life
"""

import sys
import random
import pygame

# === Constants ===
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS

ALIVE_COLOR = "white"
DEAD_COLOR = "black"
GREY = "grey"  # Grid lines

# === Initialize pygame ===
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")


def empty_grid():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]


def block():
    grid = empty_grid()
    grid[10][10] = 1
    grid[10][11] = 1
    grid[11][10] = 1
    grid[11][11] = 1
    return grid


def blinker():
    grid = empty_grid()
    grid[10][10] = 1
    grid[10][11] = 1
    grid[10][12] = 1
    return grid


def glider():
    grid = empty_grid()
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1
    return grid


def two_gliders():
    grid = empty_grid()

    # First glider (top-left)
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

    # Second glider (bottom-right)
    # Placed far enough so they move toward each other
    grid[10][25] = 1
    grid[11][26] = 1
    grid[12][24] = 1
    grid[12][25] = 1
    grid[12][26] = 1

    grid[20][25] = 1
    grid[21][26] = 1
    grid[22][24] = 1
    grid[22][25] = 1
    grid[22][26] = 1

    return grid


def four_gliders():
    grid = empty_grid()

    # Top-left glider
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

    # Top-right glider (flipped horizontally)
    grid[1][COLS - 3] = 1
    grid[2][COLS - 4] = 1
    grid[3][COLS - 6] = 1
    grid[3][COLS - 5] = 1
    grid[3][COLS - 4] = 1

    # Bottom-left glider (flipped vertically)
    grid[ROWS - 4][2] = 1
    grid[ROWS - 3][3] = 1
    grid[ROWS - 2][1] = 1
    grid[ROWS - 2][2] = 1
    grid[ROWS - 2][3] = 1

    # Bottom-right glider (flipped both horizontally and vertically)
    grid[ROWS - 4][COLS - 3] = 1
    grid[ROWS - 3][COLS - 4] = 1
    grid[ROWS - 2][COLS - 6] = 1
    grid[ROWS - 2][COLS - 5] = 1
    grid[ROWS - 2][COLS - 4] = 1

    return grid


def toad():
    grid = empty_grid()
    grid[10][11] = 1
    grid[10][12] = 1
    grid[10][13] = 1
    grid[11][10] = 1
    grid[11][11] = 1
    grid[11][12] = 1
    return grid


def beacon():
    grid = empty_grid()
    grid[10][10] = 1
    grid[10][11] = 1
    grid[11][10] = 1
    grid[11][11] = 1
    grid[12][12] = 1
    grid[12][13] = 1
    grid[13][12] = 1
    grid[13][13] = 1
    return grid


def pentadecathlon():
    grid = empty_grid()
    row = 10
    cols = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for c in cols:
        grid[row][c] = 1
    grid[row - 1][12] = 1
    grid[row - 1][19] = 1
    grid[row + 1][12] = 1
    grid[row + 1][19] = 1
    return grid


def random_pattern(prob_alive=0.3):
    grid = empty_grid()
    for row in range(ROWS):
        for col in range(COLS):
            grid[row][col] = 1 if random.random() < prob_alive else 0
    return grid


# Map pattern names to functions
patterns = {
    "block": block,
    "blinker": blinker,
    "glider": glider,
    "toad": toad,
    "beacon": beacon,
    "pentadecathlon": pentadecathlon,
    "four gliders": four_gliders,
    "random": random_pattern,
}


def draw_grid(grid):
    for row in range(ROWS):
        for col in range(COLS):
            color = ALIVE_COLOR if grid[row][col] == 1 else DEAD_COLOR
            pygame.draw.rect(
                screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    # Draw grid lines
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GREY, (0, y), (WIDTH, y))


def count_live_neighbors(grid, row, col):
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            r = (row + i) % ROWS
            c = (col + j) % COLS
            count += grid[r][c]
    return count


def next_generation(grid):
    new_grid = []
    for row in range(ROWS):
        new_row = []
        for col in range(COLS):
            live_neighbors = count_live_neighbors(grid, row, col)
            cell = grid[row][col]
            if cell == 1:  # currently alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_row.append(0)
                else:
                    new_row.append(1)
            else:  # currently dead
                if live_neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        new_grid.append(new_row)
    return new_grid


def print_usage():
    print("Usage: python game_of_life.py [pattern]")
    print("Available patterns:")
    for p in patterns.keys():
        print(f"  - {p}")
    print("Example: python game_of_life.py glider")


def main():
    if len(sys.argv) < 2:
        print("No pattern specified, defaulting to 'glider'.")
        pattern_name = "glider"
    else:
        pattern_name = sys.argv[1].lower()
        if pattern_name not in patterns:
            if pattern_name != "help":
                print(f"Unknown pattern '{pattern_name}'.")
            print_usage()
            sys.exit(1)

    grid = patterns[pattern_name]()

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(5)  # speed in frames per seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(DEAD_COLOR)
        draw_grid(grid)
        pygame.display.flip()

        grid = next_generation(grid)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
