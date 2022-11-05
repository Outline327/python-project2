import pygame

WIDTH, HEIGHT = 1535, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
WHITE = (255, 255, 255)
pygame.display.set_caption("The game")


def window_draw():
    pygame.display.update()
    WIN.fill(WHITE)


def main(run=True):
    run.py = True
    while run.py:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                pygame.quit()


if __name__ == "__main__":
    main()
