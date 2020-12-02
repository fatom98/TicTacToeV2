import pygame
from module.constants import WIDTH, HEIGHT, FPS, PADDING, SQUARE_SIZE, WHITE, SECOND, GREEN
from module.game import Game

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


def main():
    run = True
    TIME = 0
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        dt = clock.tick(FPS)

        if not game.end:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if game.turn == game.human:
                        x, y = event.pos

                        r = x//SQUARE_SIZE
                        c = y//SQUARE_SIZE

                        game.human_move((r, c))

            game.update()

        else:

            TIME += dt

            if TIME >= 3 * SECOND:
                TIME = 0
                game.again()

            elif TIME >= 1.5 * SECOND:
                WIN.fill(WHITE)
                font = pygame.font.SysFont("arial", 48)
                text = font.render(f"{game.winner} Won!!!", True, GREEN)
                WIN.blit(text, ((WIDTH - text.get_width())//2, (HEIGHT - text.get_height())//2))

            pygame.display.update()


if __name__ == "__main__":
    main()
