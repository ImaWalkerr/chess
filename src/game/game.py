import pygame

from game.const import (
    WIDTH,
    HEIGHT,
    ROWS,
    COLUMNS,
    SQSIZE,
)


class Game:

    def __init__(self):
        pass

    # show methods
    def show_backgrounds(self, surface):
        for row in range(ROWS):
            for column in range(COLUMNS):
                if (row + column) % 2 == 0:
                    color = (255, 215, 0)  # gold
                else:
                    color = (210, 105, 30)  # chocolate

                rectangle = (column * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rectangle)
