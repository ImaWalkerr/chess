import pygame
from drawing.board import Board
from game.const import (
    WIDTH,
    HEIGHT,
    ROWS,
    COLUMNS,
    SQSIZE,
)
from move.dragger import Dragger


class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

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

    # show figures on pieces
    def show_pieces(self, surface):
        for row in range(ROWS):
            for column in range(COLUMNS):
                if self.board.squares[row][column].has_piece():
                    piece = self.board.squares[row][column].piece

                    img = pygame.image.load(piece.texture)
                    img_center = column * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)
