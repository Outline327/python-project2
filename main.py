import pygame
import os

WIDTH, HEIGHT = 1535, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
GUN_1 = pygame.image.load(os.path.join('venv', 'gun1.png'))
WHITE = (255, 255, 255)
pygame.display.set_caption("The game")




def window_draw():
    WIN.fill(WHITE)
    WIN.blit(GUN_1, (0, 0))
    pygame.display.update()


def main(run=True, clock=None):
    runpy = True
    while runpy:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                pygame.quit()


if __name__ == "__main__":
    main()
