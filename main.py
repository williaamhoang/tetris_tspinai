import pygame
import sys
from grid import Grid

# Game constants
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")

    # Initialize grid
    grid = Grid(GRID_WIDTH, GRID_HEIGHT, CELL_SIZE)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Exit game loop if window is closed

        # Draw the grid
        grid.draw(screen)

        # Update the display
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
