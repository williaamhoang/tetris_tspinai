import pygame

# Colors for grid display
GRID_COLOR = (50,50,50)
BACKGROUND_COLOR = (0,0,0)

class Grid:
    def __init__(self, width, height, cell_size):
        # Initializes grid for the game
        # width = number of blocks horizontally
        # height = number of blocks vertically
        # cell_size = size of each block in pixels

        self.width = width
        self.height = height 
        self.cell_size = cell_size

    def draw(self, screen):
        # Draws grid on screen

        # Fill the background
        screen.fill(BACKGROUND_COLOR)

        # Draw grid lines
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, GRID_COLOR, rect, 1)