import pygame
import sys
from game.const import WIDTH, HEIGHT
from game import Game


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        screen = self.screen
        game = self.game
        dragger = self.game.dragger

        while True:
            game.show_backgrounds(screen)
            game.show_pieces(screen)

            for event in pygame.event.get():
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    pass

                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass

                # quit game
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
